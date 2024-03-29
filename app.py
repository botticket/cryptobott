import os
import sys

from config import line_secret, line_access_token
from flask import Flask, request, abort, send_from_directory, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,FollowEvent,QuickReply,QuickReplyButton,MessageAction
from line_notify import LineNotify
from datetime import datetime,date
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

line_secret = "11116494ef78727c367cab0cd4584b9c"
line_access_token = "dOt/F1F30Np2lf95rvGpYlj7w6WVVWKfK66IKtwL1jbD/sMCYcqOeRUiUuO/P6zWGvCr+v3Nf6mfYihfARJyUKvA32Jt/LCL7Im373bQABD0PttiBLkUnVYMp1SVKrYe7FoKEcvsjhkJD/j4hMXZ6wdB04t89/1O/w1cDnyilFU="

channel_secret = line_secret
channel_access_token = line_access_token
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

today = date.today()
yearly = '{}-01-01'.format(today.year)
monthly = '{}-{}-01'.format(today.year,today.month)

if today.month >= 10 :
    quarter = '{}-10-01'.format(today.year)
    tfex_code = 'S50Z20'
elif today.month >= 7:
    quarter = '{}-07-01'.format(today.year)
    tfex_code = 'S50U20'
elif today.month >= 4 :
    quarter = '{}-04-01'.format(today.year)
    tfex_code = 'S50M20'
else:
    quarter = '{}-01-01'.format(today.year)
    tfex_code = 'S50H20'

def linechat(text):
    
    ACCESS_TOKEN = "12CiN1mDzj3q93N5aTYvtWX63XlQOqDs6FWizTRUx1y"
    notify = LineNotify(ACCESS_TOKEN)
    notify.send(text)

def sendimage(filename):
    file = {'imageFile':open(filename,'rb')}
    payload = {'message': 'update'}
    return _lineNotify(payload,file)

def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'fzU5NggivM0rgd8sDfJjdAP3kMCzU0JzmvbPJGLxZMZ'	#EDIT
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)

@app.route("/webhook", methods=['POST'])
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
    Reply_token = event.reply_token

    userid = event.source.user_id
    disname = line_bot_api.get_profile(user_id=userid).display_name
    request_text= (' bullbot' + '\n' + '>> {} : {}').format(disname,text_from_user)
    
    print(request_text)
    linechat(request_text)

    try:
        if 'Hello Bot' in text_from_user:    
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

            class ticket:
                def __init__(self,stock):
                    self.stock = stock
                    list = self.stock
                def bull(self):
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
                    stock = f'{list}'
                    dfall.dropna(inplace=True)

                    st = checkmarket(stock)
                                
                    try:
                        Close = float(st[1])
                    except ValueError:
                        Close = dfall['Close'].iloc[-1]

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

                    CloseY = dfY['Close'].iloc[0]
                    CloseY  = '%.2f'%CloseY
                    CloseY = str(CloseY)

                    ChgY = ((float(Close) - float(OpenY)) / float(OpenY) )*100
                    ChgY = '%.2f'%ChgY
                    ChgY = str(ChgY)

                    Chg_closeY = ((float(Close) - float(CloseY)) / float(CloseY) )*100
                    Chg_closeY = '%.2f'%Chg_closeY
                    Chg_closeY = str(Chg_closeY)

                    OpenM = dfM['Open'].iloc[0]
                    OpenM  = '%.2f'%OpenM
                    OpenM = str(OpenM)

                    CloseM = dfM['Close'].iloc[0]
                    CloseM  = '%.2f'%CloseM
                    CloseM = str(CloseM)

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

                    dfall['RSI'] = computeRSI(dfall['Close'], 14)
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

                    high_trend = dfall['high_trend'].iloc[-1]
                    high_trend = '%.2f'%high_trend
                    high_trend = str(high_trend)

                    # low trend lineY
                    dfall_mod = dfall.copy()

                    while len(dfall_mod)>3:

                        reg = linregress(x=dfall_mod['date_id'],y=dfall_mod['Close'],)
                        dfall_mod = dfall_mod.loc[dfall_mod['Close'] < reg[0] * dfall_mod['date_id'] + reg[1]]

                    reg = linregress(x=dfall_mod['date_id'],y=dfall_mod['Close'],)
                    dfall['low_trend'] = reg[0] * dfall['date_id'] + reg[1]
                    
                    min_Y = dfall.nsmallest(1, columns='Low')
                    min_Y = min_Y['Low'].iloc[-1]
                    min_Y = '%.2f'%min_Y
                    min_Y = str(min_Y)

                    max_Y = dfall.nlargest(1, columns='High')
                    max_Y = max_Y['High'].iloc[-1]
                    max_Y = '%.2f'%max_Y
                    max_Y = str(max_Y)

                    dfall['min_Y'] = float(min_Y)
                    dfall['max_Y'] = float(max_Y)
                    
                    #copy dataframe prevQ
                    dfY = dfY.copy()
                    dfY['date_id'] = ((dfY.index.date - dfY.index.date.min())).astype('timedelta64[D]')
                    dfY['date_id'] = dfY['date_id'].dt.days + 1

                    # high trend line prevQ
                    dfY_mod = dfY.copy()

                    while len(dfY_mod)>3:

                        reg = linregress(x=dfY_mod['date_id'],y=dfY_mod['Close'],)
                        dfY_mod = dfY_mod.loc[dfY_mod['Close'] > reg[0] * dfY_mod['date_id'] + reg[1]]

                    reg = linregress(x=dfY_mod['date_id'],y=dfY_mod['Close'],)
                    dfY['high_trendQ'] = reg[0] * dfY['date_id'] + reg[1]

                    # low trend line prevQ
                    dfY_mod = dfY.copy()

                    while len(dfY_mod)>3:

                        reg = linregress(x=dfY_mod['date_id'],y=dfY_mod['Close'],)
                        dfY_mod = dfY_mod.loc[dfY_mod['Close'] < reg[0] * dfY_mod['date_id'] + reg[1]]

                    reg = linregress(x=dfY_mod['date_id'],y=dfY_mod['Close'],)
                    dfY['low_trendQ'] = reg[0] * dfY['date_id'] + reg[1]
                    dfY['low_trendQ'] = dfY['low_trendQ'].replace(np.nan, dfY['Close'].iloc[0])

                    candle_start = dfY['low_trendQ'].iloc[0]
                    candle_start = '%.2f'%candle_start
                    candle_start = str(candle_start)

                    candle_end = dfY['low_trendQ'].iloc[-1]
                    candle_end = '%.2f'%candle_end
                    candle_end = str(candle_end)

                    if float(candle_start) > float(candle_end):
                        pattern = 'Lower low'
                    else:
                        pattern = 'Lower high'

                    Volume = dfY['Volume'].iloc[-1]
                    Volume = str(Volume)

                    vol_buy = (float(budget) / float(OpenY))
                    vol_buy = round(vol_buy,-2)

                    vol_key = float(vol_buy) / 2
                    vol_key = round(vol_key,-2)
                    vol_key = str(int(vol_key))

                    trade_val = float(Close) * float(Volume)
                    trade_val = int(float(trade_val))
                    trade_value = '{:,}'.format(trade_val)

                    dfall['Open_all'] = dfall['Open'].iloc[0]
                    dfall['high_trendQ'] = dfY['high_trendQ']
                    dfall['low_trendQ'] = dfY['low_trendQ']
                    dfall['ema'] = dfall['Close'].rolling(35).mean()

                    dfY['OpenY'] = dfY['Open'].iloc[0]
                    dfY['CloseY'] = dfY['Close'].iloc[0]
                    dfM['CloseM'] = dfM['Close'].iloc[0]

                    ema = dfall['ema'].iloc[-1]			
                    ema = '%.2f'%ema
                    ema = str(ema)

                    pema = ((float(Close) - float(ema)) / float(ema))*100
                    pema = '%.2f'%pema
                    pema = str(pema)

                    high_trend = dfall['high_trend'].iloc[-1]
                    high_trend = '%.2f'%high_trend
                    high_trend = str(high_trend)

                    high_trendQ = dfall['high_trendQ'].iloc[-1]
                    high_trendQ = '%.2f'%high_trendQ
                    high_trendQ = str(high_trendQ)

                    comvlue = float(st[3])
                    comvluee = str(st[4])

                    if float(ChgM) >= 0.0 :
                        trendM = ' '
                    else:
                        trendM = 'X'

                    if float(ChgY) >= 0 :
                        trendAll = '▲'
                        if float(Close) >= float(CloseM) :
                            if float(CloseM) >= float(ema):
                                if float(candle_end) >= float(candle_start):
                                    trendY = '©'
                                else:
                                    trendY = ' '
                            else:
                                trendY = ' '
                        else:
                            trendY = ' '
                    else:
                        trendAll = '▼'
                        if float(Close) >= float(CloseM) :
                            if float(CloseM) >= float(ema):
                                if float(candle_end) >= float(candle_start):
                                    trendY = '℗'
                                else:
                                    trendY = ' '
                            else:
                                trendY = ' '
                        else:
                            trendY = ' '
			        
                    text = f'{trendY}{trendM} {list} cY{CloseY} {trendAll} {Chg_closeY}% | e {ema} {pema}% | cM{CloseM} > {Close} ({today_chg})'
                    
                    if float(Close) > float(CloseY):
                        if float(Close) >= float(CloseM) :
                            if float(CloseY) >= float(ema):
                                notice = f'Buy CloseY >> {high_trend}'
                                start = f'oM {OpenM}'
                                buy = f'cM {CloseM} | cY{CloseY}'
                                stop = f'e {ema} {pema}%'
                                target = f'H {max_Y} | L {min_Y}'
                                avg = f'$ {comvluee} \nr{m_RSI} | {pattern}'
                            elif float(CloseM) >= float(ema):
                                if float(candle_end) >= float(candle_start):
                                    notice = f'Buy CloseM >> {high_trend}'
                                    start = f'oM {OpenM}'
                                    buy = f'cY{CloseY} | cM {CloseM}'
                                    stop = f'e {ema} {pema}%'
                                    target = f'H {max_Y} | L {min_Y}'
                                    avg = f'$ {comvluee} \nr{m_RSI} | {pattern}'
                                else:
                                    notice = f'LowerL'
                                    start = f'oM {OpenM}'
                                    buy = f'cY{CloseY} | cM {CloseM}'
                                    stop = f'e {ema} {pema}%'
                                    target = f'H {max_Y} | L {min_Y}'
                                    avg = f'$ {comvluee} \nr{m_RSI} | {pattern}'
                            else:
                                notice = f'UnderEma'
                                start = f'oM {OpenM}'
                                buy = f'cY{CloseY} | cM {CloseM}'
                                stop = f'e {ema} {pema}%'
                                target = f'H {max_Y} | L {min_Y}'
                                avg = f'$ {comvluee} \nr{m_RSI} | {pattern}'
                        else:
                            notice = f'LowM'
                            start = f'oM {OpenM}'
                            buy = f'cY{CloseY} | cM {CloseM}'
                            stop = f'e {ema} {pema}%'
                            target = f'H {max_Y} | L {min_Y}'
                            avg = f'$ {comvluee} \nr{m_RSI} | {pattern}'       
                    elif float(Close) >= float(CloseM) :
                        if float(CloseM) >= float(ema):
                            if float(candle_end) >= float(candle_start):
                                notice = f'Buy CloseM >> {high_trend}'
                                start = f'oM {OpenM}'
                                buy = f'cY{CloseY} | cM {CloseM}'
                                stop = f'e {ema} {pema}%'
                                target = f'H {max_Y} | L {min_Y}'
                                avg = f'$ {comvluee} \nr{m_RSI} | {pattern}'
                            else:
                                notice = f'Lower Low'
                                start = f'oM {OpenM}'
                                buy = f'cY{CloseY} | cM {CloseM}'
                                stop = f'e {ema} {pema}%'
                                target = f'H {max_Y} | L {min_Y}'
                                avg = f'$ {comvluee} \nr{m_RSI} | {pattern}'
                        else:
                            notice = f'UnderEma'
                            start = f'oM {OpenM}'
                            buy = f'cY{CloseY} | cM {CloseM}'
                            stop = f'e {ema} {pema}%'
                            target = f'H {max_Y} | L {min_Y}'
                            avg = f'$ {comvluee} \nr{m_RSI} | {pattern}'
                    else:
                        notice = f'LowM'
                        start = f'oM {OpenM}'
                        buy = f'cY{CloseY} | cM {CloseM}'
                        stop = f'e {ema} {pema}%'
                        target = f'H {max_Y} | L {min_Y}'
                        avg = f'$ {comvluee} \n{rsi} {pattern}'

                    word_to_reply = str('{}'.format(text))
                    linechat(word_to_reply)

                    bubbles = []
                    bubble = flex_stock(text,Close,today_chg,trendAll,Chg_closeY,notice,start,buy,stop,target,avg)
                    
                    flex_to_reply = SetMessage_Object(bubble)
                    reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
                    return 'OK'
            
            for code in codes:
                ticket(code).bull()
    except:
        text_list = [
            '{} ไม่มีในฐานข้อมูล {} ลองใหม่อีกครั้ง'.format(text_from_user,disname),
            '{} พิมพ์ชื่อหุ้น {} ไม่ถูกต้อง ลองใหม่อีกครั้ง'.format(disname, text_from_user)]

        from random import choice
        word_to_reply = choice(text_list)        
        text_to_reply = TextSendMessage(text = word_to_reply)

        line_bot_api.reply_message(
                event.reply_token,
                messages=[text_to_reply])

@handler.add(FollowEvent)
def RegisRichmenu(event):
    userid = event.source.user_id
    disname = line_bot_api.get_profile(user_id=userid).display_name
    line_bot_api.link_rich_menu_to_user(userid,'richmenu-073dc85eff8bb8351e8d53769c025029')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 2000))
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)