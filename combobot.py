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
end = datetime.now()
current_time = end.strftime("%H:%M %p")
current_hrs = end.strftime("%H")

start_year = today.year - 1
start_year = '{}-{}-01'.format(start_year,today.month)

yearly = '{}-01-01'.format(today.year)
monthly = '{}-{}-01'.format(today.year,today.month)

prevmo = today.month -1
if today.month >= 4:
    prevm = '{}-{}-01'.format(today.year,prevmo)
    endvm = '{}-{}-30'.format(today.year,prevmo)
elif today.month == 3:
    prevm = '{}-{}-01'.format(today.year,prevmo)
    endvm = '{}-{}-25'.format(today.year,prevmo)
elif today.month == 2:
    prevm = '{}-{}-01'.format(today.year,prevmo)
    endvm = '{}-{}-30'.format(today.year,prevmo)
else:
    prevY = today.year - 1
    prevm = '{}-12-01'.format(prevY)
    endvm = '{}-12-30'.format(prevY)

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

    # try:        
    if 'สวัสดี' in text_from_user:    
        text_list = [
            'สวัสดีจ้า คุณ {} สนใจหุ้นตัวไหน'.format(disname),
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

        set50 = ['ADVANC','AOT','AWC', 'BAM', 'BBL', 'BDMS', 'BEM','BGRIM','BH','BJC','BTS','CBG',
                'COM7', 'CPALL','CPF','CPN','CRC','DELTA','DTAC','EA', 'EGCO','GLOBAL', 'GPSC',
                'GULF','HMPRO', 'INTUCH','IVL','KBANK','KTB','KTC','LH','MINT', 'MTC','OR',
                'OSP','PTT', 'PTTEP', 'PTTGC', 'RATCH','SAWAD', 'SCB','SCC','SCGP','TISCO','TMB',
                'TOA','TOP','TRUE','TU', 'VGI']

        set100 = ['ACE','AEONTS', 'AMATA', 'AP','BANPU','BCH','BCP','BCPG','BEC','BPP','CENTEL','CHG',
                'CK','CKP','DOHOME','EPG','ESSO','GFPT','GUNKUL','HANA','JAS','IRPC','JMART', 'JMT',
                'KCE', 'KKP', 'MAJOR','MBK','MEGA','ORI','PLANB','PRM','PTG','QH','RBF','RS','SPALI',
                'STA','STEC','SUPER','TCAP','THANI','TASCO', 'TISCO','TMB','TOA','TPIPP','TQM','TTW',
                'TVO','WHA','WHAUP' ]

        class stock:
            def __init__(self,stock):
                self.stock = stock
            def ticket(self):
                end = datetime.now()
                start = datetime(end.year,end.month,end.day)
                list = self.stock

                try:
                    dfY = data.DataReader(f'{list}', data_source="yahoo", start=yearly, end=end)
                except ValueError:
                    dfY = data.DataReader(f'{list}', data_source="yahoo", start=start_year, end=end)
                try:
                    preM = data.DataReader(f'{list}', data_source="yahoo", start=prevm, end=endvm)
                except ValueError:
                    preM = data.DataReader(f'{list}', data_source="yahoo", start=start_year, end=end)

                list = list.replace('.bk','')

                st = checkmarket(code)
                stock = f'{list}'
                dfY.dropna(inplace=True)
    
                try:
                    Close = float(st[1])
                except ValueError:
                    Close = dfY['Close'].iloc[-1]
                Close  = '%.2f'%Close

                OpenY = dfY['Open'].iloc[0]
                OpenY  = '%.2f'%OpenY

                ChgY = ((float(Close) - float(OpenY)) / float(OpenY) )*100
                ChgY = '%.2f'%ChgY

                OpenD = dfY['Open'].iloc[-1]
                OpenD  = '%.2f'%OpenD

                try:
                    today_chg = float(st[2])
                except ValueError:
                    today_chg = float(dfall['Close'].iloc[-1]) - float(dfall['Close'].iloc[-2])
                today_chg  = '%.2f'%today_chg

                comvlue = float(st[3])
                comvluee = str(st[4])

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

                min_Yp = ((float(min_Y) - float(Close))/float(Close))*100
                min_Yp = '%.2f'%min_Yp

                max_Y = dfall.nlargest(1, columns='High')
                max_Y = max_Y['High'].iloc[-1]
                max_Y = '%.2f'%max_Y

                max_Yp = ((float(max_Y) - float(Close))/float(Close))*100
                max_Yp = '%.2f'%max_Yp

                HpreM = preM.nlargest(1, columns='Close')
                HpreM = HpreM['Close'].iloc[-1]
                HpreM = '%.2f'%HpreM

                HpreMp = ((float(Close) - float(HpreM))/float(HpreM))*100
                HpreMp = '%.2f'%HpreMp

                dfall['max_Y'] = float(max_Y)
                dfall['min_Y'] = float(min_Y)
                dfY['HpreM'] = float(HpreM)

                if (stock in set50):
                    inline = f'SET50'
                elif (stock in set100):
                    inline = f'SET100'
                else:
                    inline = ' '

                if float(ChgY) >= 0 :
                    trendAll = '▲'
                else:
                    trendAll = '▼'
                            
                text_return = f'{list} H {HpreM} ({HpreMp}%) > {Close} ({today_chg}) \nOpen {OpenD}'
                linechat(text_return)

                text = st[0]
                price_now = str(Close) 
                change = str(today_chg)
                chgp = str(ChgY)
                re_avg = f'Hp {max_Y} {max_Yp}% \nLp {min_Y} {min_Yp}%'

                if float(Close) > float(HpreM):
                    if float(OpenD) >= float(HpreM) :
                        notice = f'H {HpreM} ({HpreMp}%)'
                        start = f'OD {OpenD}'
                        stop = f' '
                        target = f'{inline}'
                    else:
                        notice = f'H {HpreM} ({HpreMp}%)'
                        start = f'OD {OpenD}'
                        stop = f' '
                        target = f'{inline}'
                else:
                    notice = f'H {HpreM} ({HpreMp}%)'
                    start = f'OD {OpenD}'
                    stop = f' '
                    target = f'{inline}'

                word_to_reply = str('{}'.format(text_return))
                print(word_to_reply)
                bubbles = []
                bubble = flex_stock(text,price_now,change,chgp,notice,start,stop,target,re_avg)
                
                flex_to_reply = SetMessage_Object(bubble)
                reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
                return 'OK'

        for symbol in symbols:
            stock(symbol).ticket()

    # except:
    #     text_list = [
    #         'หุ้น {} ไม่แสดงข้อมูล'.format(text_from_user),
    #         '{} สะกด {} ไม่ถูกต้อง'.format(disname, text_from_user),]

    #     from random import choice
    #     word_to_reply = choice(text_list)
    #     text_to_reply = TextSendMessage(text = word_to_reply)
    #     line_bot_api.reply_message(event.reply_token, messages=[text_to_reply])

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