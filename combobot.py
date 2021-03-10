# https://cryptobott.herokuapp.com/callback

import os
import sys

from flask import Flask, request, abort, send_from_directory, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,FollowEvent,QuickReply,QuickReplyButton,MessageAction
from line_notify import LineNotify
from reply import reply_msg , SetMessage_Object
from flex_crypto import *
from dialogflow_uncle import detect_intent_texts
from datetime import datetime,date


app = Flask(__name__)

channel_secret = 'afe7ec6bede0dde581d0a61b6447653b'
channel_access_token = 'hkU+OYWsepq11sc+uM6bAE/ECjFb8+NUiTvjfQI1WUrXzKiUZvHU5YAv+AEG4I6ZZuJPflQ/v5Gp2XH5m5TtLeUkPpX3JUjqTKFWahSOIqWheppXpKvFyE+olbJyAGvg9f8pciPntSGZnLbfyAIoyQdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

today = date.today()

start_year = today.year - 1
start_year = '{}-{}-01'.format(start_year,today.month)

yearly = '{}-01-01'.format(today.year)
monthly = '{}-{}-01'.format(today.year,today.month)

def linechat(text):
    ACCESS_TOKEN = "12CiN1mDzj3q93N5aTYvtWX63XlQOqDs6FWizTRUx1y"
    notify = LineNotify(ACCESS_TOKEN)
    notify.send(text)

@app.route("/callback", methods=['POST'])
def callback():
	# get X-Line-Signature header value
	signature = request.headers['X-Line-Signature']

	# get request body as text
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)
	# handle webhook body
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text_from_user = event.message.text
    reply_token = event.reply_token
    userid = event.source.user_id
    
    disname = line_bot_api.get_profile(user_id=userid).display_name
    request_text= ('mybot'+'\n' + '>> {} : {}').format(disname,text_from_user)

    print(request_text)
    linechat(request_text)

    result_from_dialogflow = detect_intent_texts(project_id="worldstock-iardyn",
                                        session_id=userid ,
                                        text=text_from_user , 
                                        language_code="th")
    
    action = result_from_dialogflow["action"]
    response = result_from_dialogflow["fulfillment_messages"] #as list

    print("action : " + action)
    print("response : " + str(response))

    try:        
        if 'สวัสดี' in text_from_user:    
            text_list = [
                'สวัสดีจ้า คุณ {} '.format(disname),
                'สวัสดีจ้า คุณ {} วันนี้จะเล่นตัวไหนดี'.format(disname),
            ]

            from random import choice
            word_to_reply = choice(text_list)
            text_to_reply = TextSendMessage(text = word_to_reply)
            line_bot_api.reply_message(
                    event.reply_token,
                    messages=[text_to_reply]
                )
            return 'OK'

        else:
            from bs4 import BeautifulSoup as soup
            from urllib.request import urlopen as req
            from pandas_datareader import data
            from datetime import datetime, date
            from scipy.stats import linregress
            import math
            import numpy as np
            import pandas as pd 
            
            code = text_from_user
            ticket = [text_from_user]
            symbols = list(map(lambda e: e + '.bk', ticket))
                        
            def checkmarket(code):
                url = 'https://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol={}&ssoPageId=9&selectPage=1'.format(code)
                webopen = req(url)
                page_html = webopen.read()
                webopen.close()
                data = soup(page_html, 'html.parser')
                price = data.findAll('div',{'class':'col-xs-6'})
                title = price[0].text
                stockprice = price[2].text
                stockprice = stockprice.replace('\n','')
                change = price[3].text
                change = change.replace('\n','')
                change = change.replace('\r','')
                change = change[87:]	
                comvlue = data.findAll('div',{'class':'col-xs-4'})
                comvlue = comvlue[6].text
                comvlue = comvlue.replace(',','')
                comvlue = format(float(comvlue),'')
                comvluee = format(float(comvlue),',')
                return [title,stockprice,change,comvlue,comvluee]

            def free(code):
                url = 'https://www.settrade.com/C04_05_stock_majorshareholder_p1.jsp?txtSymbol={}&ssoPageId=14&selectPage=5'.format(code)
                webopen = req(url)
                page_html = webopen.read()
                webopen.close()
                data = soup(page_html, 'html.parser')
                freefloat = data.findAll('div',{'class':'row separate-content'})
                freefloat = freefloat[0].text
                freefloat = freefloat.replace('\n','')
                freefloat = freefloat.replace('\r','')
                freefloat = freefloat[-6:]
                freefloat = freefloat.replace('%','')
                return [freefloat]

            class stock:
                def __init__(self,stock):
                    self.stock = stock
                def ticket(self):
                    end = datetime.now()
                    start = datetime(end.year,end.month,end.day)
                    list = self.stock

                    dfall = data.DataReader(f'{list}', data_source="yahoo",start=start_year, end=end)

                    try:
                        dfY = data.DataReader(f'{list}', data_source="yahoo", start=yearly, end=end)
                    except ValueError:
                        dfY = data.DataReader(f'{list}', data_source="yahoo", start=start_year, end=end)

                    try:
                        dfM = data.DataReader(f'{list}', data_source="yahoo", start=monthly, end=end)
                    except ValueError:
                        dfM = data.DataReader(f'{list}', data_source="yahoo", start=start_year, end=end)

                    list = list.replace('.bk','')

                    st = checkmarket(code)
                    fr = free(code)
                    freefloat = fr[0]

                    stock = f'{list}'
                    dfall.dropna(inplace=True)
        
                    try:
                        Close = float(st[1])
                    except ValueError:
                        Close = dfM['Close'].iloc[-1]

                    Close  = '%.2f'%Close
                    Close = str(Close) 

                    Open_all = dfall['Open'].iloc[0]
                    Open_all  = '%.2f'%Open_all
                    Open_all = str(Open_all)

                    Chg_all = ((float(Close) - float(Open_all))/ float(Open_all))*100
                    Chg_all = '%.2f'%Chg_all
                    Chg_all = str(Chg_all)

                    OpenY = dfY['Open'].iloc[0]
                    OpenY  = '%.2f'%OpenY
                    OpenY = str(OpenY)

                    ChgY = ((float(Close) - float(OpenY)) / float(OpenY) )*100
                    ChgY = '%.2f'%ChgY
                    ChgY = str(ChgY)

                    Chg_closeY = ((float(Close) - float(CloseY)) / float(CloseY) )*100
                    Chg_closeY = '%.2f'%Chg_closeY
                    Chg_closeY = str(Chg_closeY)

                    OpenM = dfM['Open'].iloc[0]
                    OpenM  = '%.2f'%OpenM
                    OpenM = str(OpenM)

                    ChgM = ((float(Close) - float(CloseM)) / float(CloseM) )*100
                    ChgM = '%.2f'%ChgM
                    ChgM = str(ChgM)

                    try:
                        today_chg = float(st[2])
                    except ValueError:
                        today_chg = float(dfall['Close'].iloc[-1]) - float(dfall['Close'].iloc[-2])

                    today_chg  = '%.2f'%today_chg
                    today_chg = str(today_chg)

                    def computeRSI (data, time_window):
                        diff = data.diff(1).dropna()
                        up_chg = 0 * diff
                        down_chg = 0 * diff

                        up_chg[diff > 0] = diff[ diff>0 ]    
                        down_chg[diff < 0] = diff[ diff < 0 ]

                        up_chg_avg   = up_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
                        down_chg_avg = down_chg.ewm(com=time_window-1 , min_periods=time_window).mean()

                        rs = abs(up_chg_avg/down_chg_avg)
                        rsi = 100 - 100/(1+rs)
                        return rsi

                    dfall['RSI'] = computeRSI(dfall['Close'], 75)
                    m_RSI = dfall['RSI'].iloc[-1]
                    m_RSI = '%.2f'%m_RSI
                    m_RSI = str(m_RSI)

                    #copy dataframeY
                    dfall = dfall.copy()
                    dfall['date_id'] = ((dfall.index.date - dfall.index.date.min())).astype('timedelta64[D]')
                    dfall['date_id'] = dfall['date_id'].dt.days + 1

                    # high trend lineY
                    dfall_mod = dfall.copy()

                    while len(dfall_mod)>3:

                        reg = linregress(x=dfall_mod['date_id'],y=dfall_mod['Close'],)
                        dfall_mod = dfall_mod.loc[dfall_mod['Close'] > reg[0] * dfall_mod['date_id'] + reg[1]]

                    reg = linregress(x=dfall_mod['date_id'],y=dfall_mod['Close'],)
                    dfall['high_trend'] = reg[0] * dfall['date_id'] + reg[1]

                    # low trend lineY
                    dfall_mod = dfall.copy()

                    while len(dfall_mod)>3:

                        reg = linregress(x=dfall_mod['date_id'],y=dfall_mod['Close'],)
                        dfall_mod = dfall_mod.loc[dfall_mod['Close'] < reg[0] * dfall_mod['date_id'] + reg[1]]

                    reg = linregress(x=dfall_mod['date_id'],y=dfall_mod['Close'],)
                    dfall['low_trend'] = reg[0] * dfall['date_id'] + reg[1]

                    min_Y = dfall.nsmallest(1, columns='Close')
                    min_Y = min_Y['Close'].iloc[-1]
                    min_Y = '%.2f'%min_Y
                    min_Y = str(min_Y)

                    min_Yp = ((float(min_Y) - float(Close))/float(Close))*100
                    min_Yp = '%.2f'%min_Yp
                    min_Yp = str(min_Yp)

                    max_Y = dfall.nlargest(1, columns='High')
                    max_Y = max_Y['High'].iloc[-1]
                    max_Y = '%.2f'%max_Y
                    max_Y = str(max_Y)

                    max_Yp = ((float(max_Y) - float(Close))/float(Close))*100
                    max_Yp = '%.2f'%max_Yp
                    max_Yp = str(max_Yp)

                    dfall['min_Y'] = float(min_Y)
                    dfall['max_Y'] = float(max_Y)
                    dfall['Open_all'] = dfall['Open'].iloc[0]
                    dfY['OpenY'] = dfY['Open'].iloc[0]
                    
                    dfall['ema35'] = dfall['Close'].rolling(35).mean()
                    dfall['ema'] = dfall['Close'].rolling(75).mean()
                    dfall['ema'] = dfall['ema'].replace(np.nan, dfall['Open'].iloc[0])

                    ema = dfall['ema'].iloc[-1]
                    ema = float(ema)
                    if ema >= 100:
                        ema = (round(ema/0.5) * 0.5)
                    elif ema >= 25:
                        ema = (round(ema/0.25) * 0.25)
                    elif ema >= 10:
                        ema = (round(ema/0.1) * 0.1)
                    elif ema >= 5:
                        ema = (round(ema/0.05) * 0.05)
                    else:
                        ema = (round(ema/0.02) * 0.02)
                    ema = '%.2f'%ema

                    max_ema = dfall.nlargest(1, columns='ema')
                    max_ema = max_ema['ema'].iloc[-1]
                    if max_ema >= 100:
                        max_ema = (round(max_ema/0.5) * 0.5)
                    elif max_ema >= 25:
                        max_ema = (round(max_ema/0.25) * 0.25)
                    elif max_ema >= 10:
                        max_ema = (round(max_ema/0.1) * 0.1)
                    elif max_ema >= 5:
                        max_ema = (round(max_ema/0.05) * 0.05)
                    else:
                        max_ema = (round(max_ema/0.02) * 0.02)
                    max_ema = '%.2f'%max_ema

                    min_ema = dfall.nsmallest(1, columns='ema')
                    min_ema = min_ema['ema'].iloc[-1]
                    if min_ema >= 100:
                        min_ema = (round(min_ema/0.5) * 0.5)
                    elif min_ema >= 25:
                        min_ema = (round(min_ema/0.25) * 0.25)
                    elif min_ema >= 10:
                        min_ema = (round(min_ema/0.1) * 0.1)
                    elif min_ema >= 5:
                        min_ema = (round(min_ema/0.05) * 0.05)
                    else:
                        min_ema = (round(min_ema/0.02) * 0.02)
                    min_ema = '%.2f'%min_ema

                    min_pema = ((float(min_ema) - float(Close)) / float(Close))*100
                    min_pema = '%.2f'%min_pema

                    avg_ema = (float(max_ema) + float(min_ema))/2
                    if avg_ema >= 100:
                        avg_ema = (round(avg_ema/0.5) * 0.5)
                    elif avg_ema >= 25:
                        avg_ema = (round(avg_ema/0.25) * 0.25)
                    elif avg_ema >= 10:
                        avg_ema = (round(avg_ema/0.1) * 0.1)
                    elif avg_ema >= 5:
                        avg_ema = (round(avg_ema/0.05) * 0.05)
                    else:
                        avg_ema = (round(avg_ema/0.02) * 0.02)
                    avg_ema = '%.2f'%avg_ema

                    pema = dfall['ema'].iloc[-1]
                    pema = ((float(Close) - float(pema)) / float(pema))*100
                    pema = '%.2f'%pema
                    pema = str(pema)

                    high_trend = dfall['high_trend'].iloc[-1]
                    if high_trend >= 100:
                        high_trend = (round(high_trend/0.5) * 0.5)
                    elif high_trend >= 25:
                        high_trend = (round(high_trend/0.25) * 0.25)
                    elif high_trend >= 10:
                        high_trend = (round(high_trend/0.1) * 0.1)
                    elif high_trend >= 5:
                        high_trend = (round(high_trend/0.05) * 0.05)
                    else:
                        high_trend = (round(high_trend/0.02) * 0.02)
                    high_trend = '%.2f'%high_trend

                    if float(ChgM) >= 0.0 :
                        trendM = ' '
                    else:
                        trendM = 'X'

                    if float(ChgY) >= 0 :
                        trendAll = '▲'
                        if float(Close) >= float(CloseM) :
                            if float(Close) >= float(ema):
                                trendY = '©'
                            else:
                                trendY = ' '
                        else:
                            trendY = ' '
                    else:
                        trendAll = '▼'
                        if float(Close) >= float(CloseM) :
                            if float(Close) >= float(ema):
                                trendY = '℗'
                            else:
                                trendY = ' '
                        else:
                            trendY = ' '

                    text_return = f'\n{list} {trendY}{trendM} oY {OpenY} {trendAll} {ChgY}%  \ne {ema} ({pema}%) > {Close} ({today_chg}) \nmin {min_ema} ({min_pema}%)'
                    linechat(text_return)

                    text = st[0]
                    price_now = str(Close) 
                    change = str(today_chg)
                    chgp = str(Chg_closeY)
                    re_avg = f'High {max_Y} {max_Yp}% \nLow {min_Y} {min_Yp}% \nRsi {m_RSI} | Free {freefloat}%'

                    if float(Close) > float(OpenY):
                        if float(Close) >= float(OpenM) :
                            if float(Close) >= float(ema):
                                notice = f'e {ema} ({pema}%)'
                                start = f'm {max_ema} a {avg_ema} m {min_ema}'
                                stop = f'oY {OpenY} {trendAll} {ChgY}%'
                                target = f'TP {high_trend}'
                            else:
                                notice = f'หลุด e {ema} ({pema}%)'
                                start = f'm {max_ema} a {avg_ema} m {min_ema}'
                                stop = f'oY {OpenY} {trendAll} {ChgY}%'
                                target = f'TP {high_trend}'
                        else:
                            notice = f'หลุดM e {ema} ({pema}%)'
                            start = f'm {max_ema} a {avg_ema} m {min_ema}'
                            stop = f'oY {OpenY} {trendAll} {ChgY}%'
                            target = f'TP {high_trend}'
                    elif float(Close) >= float(OpenM) :
                        if float(Close) >= float(ema):
                            notice = f'e {ema} ({pema}%)'
                            start = f'm {max_ema} a {avg_ema} m {min_ema}'
                            stop = f'oY {OpenY} {trendAll} {ChgY}%'
                            target = f'TP {high_trend}'
                        else:
                            notice = f'หลุด e {ema} ({pema}%)'
                            start = f'm {max_ema} a {avg_ema} m {min_ema}'
                            stop = f'oY {OpenY} {trendAll} {ChgY}%'
                            target = f'TP {high_trend}'
                    else:
                        notice = f'หลุดM e {ema} ({pema}%)'
                        start = f'm {max_ema} a {avg_ema} m {min_ema}'
                        stop = f'oY {OpenY} {trendAll} {ChgY}%'
                        target = f'TP {high_trend}'

                    word_to_reply = str('{}'.format(text_return))
                    print(word_to_reply)
                    bubbles = []
                    bubble = flex_stock(text,price_now,change,chgp,notice,start,stop,target,re_avg)
                    
                    flex_to_reply = SetMessage_Object(bubble)
                    reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
                    return 'OK'

            for symbol in symbols:
                stock(symbol).ticket()

    except:
        text_list = [
            'หุ้น {} ไม่แสดงข้อมูล'.format(text_from_user),
            '{} สะกด {} ไม่ถูกต้อง'.format(disname, text_from_user),
        ]

        from random import choice
        word_to_reply = choice(text_list)
        text_to_reply = TextSendMessage(text = word_to_reply)
        line_bot_api.reply_message(
                event.reply_token,
                messages=[text_to_reply]
            )

@handler.add(FollowEvent)
def RegisRichmenu(event):
    userid = event.source.user_id
    disname = line_bot_api.get_profile(user_id=userid).display_name
    line_bot_api.link_rich_menu_to_user(userid,'richmenu-9c78b01825c3f97ebebc0c400e74ffe7')
            
if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Credentials.json"
    os.environ["DIALOGFLOW_PROJECT_ID"] = "worldstock-iardyn"
    port = int(os.getenv('PORT', 2000))
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)