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

app = Flask(__name__)

channel_secret = 'afe7ec6bede0dde581d0a61b6447653b'
channel_access_token = 'hkU+OYWsepq11sc+uM6bAE/ECjFb8+NUiTvjfQI1WUrXzKiUZvHU5YAv+AEG4I6ZZuJPflQ/v5Gp2XH5m5TtLeUkPpX3JUjqTKFWahSOIqWheppXpKvFyE+olbJyAGvg9f8pciPntSGZnLbfyAIoyQdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

IQXGL = '1699.79'
IQXWTI = '32.87'
tfexx = '913.40'
sett = '1271.20'


def linechat(text):
    
    ACCESS_TOKEN = "oK2sk4w1eidfRyOVfgIcln38TBS8JmL0PgfbbQ8t0Zv"

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
    request_text= (' mybot'+'\n' + '>> {} : {}'+'\n' + '>> {}').format(disname,text_from_user,userid)

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
        if action == "Welcome_response":
            all_text = []
            for each in response:
                text = TextSendMessage(text=each)
                all_text.append(text)
            line_bot_api.reply_message(reply_token,messages=all_text) #reply messageกลับไป
            return 'OK'

        elif action == "crypto_response":
            from urllib.request import Request, urlopen
            from bs4 import BeautifulSoup as soup 
            from pandas_datareader import data
            from datetime import datetime
            
            text_from_user = text_from_user.upper()
            code = [text_from_user]
            codes = list(map(lambda e: e + '-USD', code))

            class usdcheck:
                def __init__(self,code):
                    self.code = code
                def ticket(self):
                    end = datetime.now()
                    start = datetime(end.year,end.month,end.day)
                    list = self.code

                    dfY = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
                    dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-03-16', end=end)
                    #2020-01-01 = Y M D

                    OpenY = dfY['Open'].iloc[1]
                    OpenY  = '%.2f'%OpenY
                    OpenY = str(OpenY)

                    OpenW = dfW['Open'].iloc[1]
                    OpenW  = '%.2f'%OpenW
                    OpenW = str(OpenW)

                    OpenD = dfY['Open'].iloc[-1]
                    OpenD  = '%.2f'%OpenD
                    OpenD = str(OpenD)

                    Close = dfY['Close'].iloc[-1]
                    Close  = '%.2f'%Close
                    Close = str(Close)

                    Prev = dfY['Close'].iloc[-2]
                    Prev  = '%.2f'%Prev
                    Prev = str(Prev)
                    
                    barY = ((float(Close) - float(OpenY)) / float(OpenY) )*100
                    barY = '%.2f'%barY
                    barY = float(barY)

                    barW = ((float(Close) - float(OpenW)) / float(OpenW) )*100
                    barW = '%.2f'%barW
                    barW = float(barW)

                    LongY = float(OpenW) * 1.01
                    LongY = '%.2f'%LongY
                    LongY = str(LongY) 

                    stop_longY = float(OpenW) * 0.985
                    stop_longY = '%.2f'%stop_longY
                    stop_longY = str(stop_longY)

                    exit_long1 = float(OpenD) * 1.07
                    exit_long1 = '%.2f'%exit_long1
                    exit_long1 = str(exit_long1)

                    exit_long2 = float(OpenD) * 1.14
                    exit_long2 = '%.2f'%exit_long2
                    exit_long2 = str(exit_long2)

                    exit_long3 = float(OpenD) * 1.21
                    exit_long3 = '%.2f'%exit_long3
                    exit_long3 = str(exit_long3)

                    shortY = float(OpenW) * 0.985
                    shortY = '%.2f'%shortY
                    shortY = str(shortY) 

                    stop_shortY = float(OpenW) * 1.01
                    stop_shortY = '%.2f'%stop_shortY
                    stop_shortY = str(stop_shortY)

                    exit_short1 = float(OpenD) * 0.93
                    exit_short1 = '%.2f'%exit_short1
                    exit_short1 = str(exit_short1)

                    exit_short2 = float(OpenD) * 0.86
                    exit_short2 = '%.2f'%exit_short2
                    exit_short2 = str(exit_short2)

                    exit_short3 = float(OpenD) * 0.79
                    exit_short3 = '%.2f'%exit_short3
                    exit_short3 = str(exit_short3)
                
                    change = float(Close) - float(Prev)
                    change = '%.2f'%change
                    change = str(change) 

                    chgp = (float(change) / float(Prev))*100
                    chgp = '%.2f'%chgp
                    chgp = str(chgp) 		
                    
                    text1 = exit_long1 + ' | ' + exit_long2 + ' | ' + exit_long3 
                    text2 = exit_short1 + ' | ' + exit_short2 + ' | ' + exit_short3 

                    alert1 = 'ชนแนวต้าน'
                    alert2 = 'Long'
                    alert3 = 'Short'
                    alert4 = 'กำลังย่อ'

                    text = code
                    price_now = float(Close) 
                    change = str(change) 

                    if barY > 0.00:
                        if barW >= 0:
                            notice = alert2
                            start = OpenW
                            buy = LongY
                            stop = stop_longY
                            target = text1
                            number = '1'
                        else:
                            notice = alert3
                            start = OpenW
                            buy = shortY
                            stop = stop_shortY
                            target = text2 
                            number = '2'
                    else:
                        if barW >= 0:
                            notice = alert2
                            start = OpenW
                            buy = LongY
                            stop = stop_longY
                            target = text1 
                            number = '3'
                        else:
                            notice = alert3
                            start = OpenW
                            buy = shortY
                            stop = stop_shortY
                            target = text2 
                            number = '4'

                    word_to_reply = '{}'.format(text) + '\n' + 'now {} {} ({}%)'.format(price_now,change,chgp)
                    result = 'Position: {}'.format(notice) + '\n' + 'Range: {} - {} '.format(start,buy) + '\n' + 'Stop: {}'.format(stop) + '\n' + 'Target: {}'.format(target)
                    print(word_to_reply)
                    print(result)
                    print(number)
                    bubble = flex_crypto(text,price_now,change,chgp,notice,start,buy,stop,target)
                    
                    flex_to_reply = SetMessage_Object(bubble)
                    reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
                    return 'OK'

            for code in codes:
                usdcheck(code).ticket()

        elif 'USDTHB' in text_from_user:
            from urllib.request import Request, urlopen
            from bs4 import BeautifulSoup as soup 
            from pandas_datareader import data
            from datetime import datetime     

            def usdcheck():
                end = datetime.now()
                start = datetime(end.year,end.month,end.day)
                dfY = data.DataReader('THB=X', data_source="yahoo", start='2020-01-01', end=end)
                dfW = data.DataReader('THB=X', data_source="yahoo", start='2020-03-16', end=end)
                #2020-01-01 = Y M D

                OpenY = dfY['Open'].iloc[1]
                OpenY  = '%.2f'%OpenY
                OpenY = str(OpenY)

                OpenW = dfW['Open'].iloc[1]
                OpenW  = '%.2f'%OpenW
                OpenW = str(OpenW)

                OpenD = dfY['Open'].iloc[-1]
                OpenD  = '%.2f'%OpenD
                OpenD = str(OpenD)

                Close = dfY['Close'].iloc[-1]
                Close  = '%.3f'%Close
                Close = str(Close)

                Prev = dfY['Close'].iloc[-2]
                Prev  = '%.2f'%Prev
                Prev = str(Prev)
                
                barY = ((float(Close) - float(OpenY)) / float(OpenY) )*100
                barY = '%.2f'%barY
                barY = float(barY)

                barW = ((float(Close) - float(OpenW)) / float(OpenW) )*100
                barW = '%.2f'%barW
                barW = float(barW)

                LongY = float(OpenW) * 1.01
                LongY = '%.2f'%LongY
                LongY = str(LongY) 

                stop_longY = float(OpenW) * 0.985
                stop_longY = '%.2f'%stop_longY
                stop_longY = str(stop_longY)

                exit_long1 = float(OpenD) * 1.05
                exit_long1 = '%.2f'%exit_long1
                exit_long1 = str(exit_long1)

                exit_long2 = float(OpenD) * 1.10
                exit_long2 = '%.2f'%exit_long2
                exit_long2 = str(exit_long2)

                exit_long3 = float(OpenD) * 1.15
                exit_long3 = '%.2f'%exit_long3
                exit_long3 = str(exit_long3)

                shortY = float(OpenW) * 0.985
                shortY = '%.2f'%shortY
                shortY = str(shortY) 

                stop_shortY = float(OpenW) * 1.01
                stop_shortY = '%.2f'%stop_shortY
                stop_shortY = str(stop_shortY)

                exit_short1 = float(OpenD) * 0.95
                exit_short1 = '%.2f'%exit_short1
                exit_short1 = str(exit_short1)

                exit_short2 = float(OpenD) * 0.90
                exit_short2 = '%.2f'%exit_short2
                exit_short2 = str(exit_short2)

                exit_short3 = float(OpenD) * 0.85
                exit_short3 = '%.2f'%exit_short3
                exit_short3 = str(exit_short3)
            
                change = float(Close) - float(Prev)
                change = '%.3f'%change
                change = str(change) 

                chgp = (float(change)/ float(Prev))*100
                chgp = '%.2f'%chgp
                chgp = str(chgp) 		
                
                text1 = exit_long1 + ' | ' + exit_long2 + ' | ' + exit_long3 
                text2 = exit_short1 + ' | ' + exit_short2 + ' | ' + exit_short3 

                alert1 = 'ชนแนวต้าน'
                alert2 = 'Long'
                alert3 = 'Short'
                alert4 = 'กำลังย่อ'

                text = text_from_user
                price_now = float(Close) 
                change = str(change) 

                if barY > 0.00:
                    if barW >= 0:
                        notice = alert2
                        start = OpenW
                        buy = LongY
                        stop = stop_longY
                        target = text1
                        number = '1'
                    else:
                        notice = alert3
                        start = OpenW
                        buy = shortY
                        stop = stop_shortY
                        target = text2 
                        number = '2'
                else:
                    if barW >= 0:
                        notice = alert2
                        start = OpenW
                        buy = LongY
                        stop = stop_longY
                        target = text1 
                        number = '3'
                    else:
                        notice = alert3
                        start = OpenW
                        buy = shortY
                        stop = stop_shortY
                        target = text2 
                        number = '4'

                word_to_reply = '{}'.format(text) + '\n' + 'now {} {} ({}%)'.format(price_now,change,chgp)
                result = 'Position: {}'.format(notice) + '\n' + 'Range: {} - {} '.format(start,buy) + '\n' + 'Stop: {}'.format(stop) + '\n' + 'Target: {}'.format(target)
                # print(word_to_reply)
                # print(number)

                bubble = flex_usdcheck(text,price_now,change,chgp,notice,start,buy,stop,target)
                flex_to_reply = SetMessage_Object(bubble)
                reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
                return 'OK'
            usdcheck()

        elif 'IQXGL' in text_from_user:
            from urllib.request import Request, urlopen
            from bs4 import BeautifulSoup as soup 

            def goldscrapt():
                req = Request('https://th.investing.com/currencies/xau-usd', headers={'User-Agent': 'Chrome/78.0'})
                webopen = urlopen(req).read()
                data = soup(webopen, 'html.parser')

                gold_now = data.findAll('div',{'class':'top bold inlineblock'})
                gold_now = gold_now[0].text
                gold_now = gold_now.replace('\n',' ')
                gold_now = gold_now.replace(',','')
                gold_now = gold_now[1:]
                gold_now = gold_now[0:8]

                goldchange = data.findAll('div',{'class':'top bold inlineblock'})
                goldchange = goldchange[0].text
                goldchange = goldchange.replace('\n',' ')
                goldchange = goldchange.replace(',','')
                goldchange = goldchange[9:]
                goldchange = goldchange[0:5]

                chgp = data.findAll('div',{'class':'top bold inlineblock'})
                chgp = chgp[0].text
                chgp = chgp.replace('\n',' ')
                chgp = chgp.replace(',','')
                chgp = chgp[18:]

                return[gold_now,goldchange,chgp]

            def goldcheck():
                gg = goldscrapt()

                exit_long1 = float(gg[0]) * 1.015
                exit_long1 = '%.2f'%exit_long1

                exit_long2 = float(gg[0]) * 1.03
                exit_long2 = '%.2f'%exit_long2

                exit_long3 = float(gg[0]) * 1.045
                exit_long3 = '%.2f'%exit_long3      

                exit_short1 = float(gg[0]) * 0.985
                exit_short1 = '%.2f'%exit_short1

                exit_short2 = float(gg[0]) * 0.97
                exit_short2 = '%.2f'%exit_short2

                exit_short3 = float(gg[0]) * 0.955
                exit_short3 = '%.2f'%exit_short3

                LongY = float(IQXGL) * 1.005
                LongY = '%.2f'%LongY

                stop_longY = float(IQXGL) * 0.995
                stop_longY = '%.2f'%stop_longY     

                shortY = float(IQXGL) * 0.995
                shortY = '%.2f'%shortY

                stop_shortY = float(IQXGL) * 1.0025
                stop_shortY = '%.2f'%stop_shortY                    

                price_now = float(gg[0])
                price_now = '%.2f'%price_now
                price_now = str(price_now)
                
                barW = float(price_now) - float(IQXGL)
                chgp = str(gg[2])

                text1 = exit_long1 + ' | ' + exit_long2 + ' | ' + exit_long3 
                text2 = exit_short1 + ' | ' + exit_short2 + ' | ' + exit_short3 

                alert1 = 'ชนแนวต้าน'
                alert2 = 'Long'
                alert3 = 'Short'
                alert4 = 'กำลังย่อ'

                text = text_from_user
                change = str(gg[1]) 

                if barW >= 0:
                    notice = alert2
                    start = IQXGL
                    buy = LongY
                    stop = stop_longY
                    target = text1
                    number = '1'
                else:
                    notice = alert3
                    start = IQXGL
                    buy = shortY
                    stop = stop_shortY
                    target = text2 
                    number = '2'
                
                word_to_reply = '{}'.format(text) + '\n' + 'now {} {} ({}%)'.format(price_now,change,chgp)
                result = 'Position: {}'.format(notice) + '\n' + 'Range: {} - {} '.format(start,buy) + '\n' + 'Stop: {}'.format(stop) + '\n' + 'Target: {}'.format(target)
                bubble = flex_goldcheck(text,price_now,change,chgp,notice,start,buy,stop,target)
                
                flex_to_reply = SetMessage_Object(bubble)
                reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
                return 'OK'
            goldcheck()

        elif 'IQXWTI' in text_from_user:
            from urllib.request import Request, urlopen
            from bs4 import BeautifulSoup as soup 

            def wtiscrapt():
                req = Request('https://th.investing.com/commodities/crude-oil', headers={'User-Agent': 'Chrome/78.0'})
                webopen = urlopen(req).read()
                data = soup(webopen, 'html.parser')

                wti_now = data.findAll('div',{'class':'top bold inlineblock'})
                wti_now = wti_now[0].text
                wti_now = wti_now.replace('\n',' ')
                wti_now = wti_now.replace(',','')
                wti_now = wti_now[1:]
                wti_now = wti_now[0:6]

                wtichange = data.findAll('div',{'class':'top bold inlineblock'})
                wtichange = wtichange[0].text
                wtichange = wtichange.replace('\n',' ')
                wtichange = wtichange.replace(',','')
                wtichange = wtichange[1:]
                wtichange = wtichange[6:11]

                chgp = data.findAll('div',{'class':'top bold inlineblock'})
                chgp = chgp[0].text
                chgp = chgp.replace('\n',' ')
                chgp = chgp.replace(',','')
                chgp = chgp[16:]
                return[wti_now,wtichange,chgp]

            def wticheck():
                wti = wtiscrapt()

                exit_long1 = float(wti[0]) * 1.05
                exit_long1 = '%.2f'%exit_long1

                exit_long2 = float(wti[0]) * 1.10
                exit_long2 = '%.2f'%exit_long2

                exit_long3 = float(wti[0]) * 1.15
                exit_long3 = '%.2f'%exit_long3      

                exit_short1 = float(wti[0]) * 0.95
                exit_short1 = '%.2f'%exit_short1

                exit_short2 = float(wti[0]) * 0.90
                exit_short2 = '%.2f'%exit_short2

                exit_short3 = float(wti[0]) * 0.85
                exit_short3 = '%.2f'%exit_short3

                LongY = float(IQXWTI) * 1.01
                LongY = '%.2f'%LongY

                stop_longY = float(IQXWTI) * 0.985
                stop_longY = '%.2f'%stop_longY     

                shortY = float(IQXWTI) * 0.985
                shortY = '%.2f'%shortY

                stop_shortY = float(IQXWTI) * 1.01
                stop_shortY = '%.2f'%stop_shortY                    

                price_now = float(wti[0])
                price_now = '%.2f'%price_now
                price_now = str(price_now)
                
                barW = float(price_now) - float(IQXWTI)
                chgp = str(wti[2])

                text1 = exit_long1 + ' | ' + exit_long2 + ' | ' + exit_long3 
                text2 = exit_short1 + ' | ' + exit_short2 + ' | ' + exit_short3 

                alert1 = 'ชนแนวต้าน'
                alert2 = 'Long'
                alert3 = 'Short'
                alert4 = 'กำลังย่อ'

                text = text_from_user
                change = str(wti[1]) 

                if barW >= 0:
                    notice = alert2
                    start = IQXWTI
                    buy = LongY
                    stop = stop_longY
                    target = text1
                    number = '1'
                else:
                    notice = alert3
                    start = IQXWTI
                    buy = shortY
                    stop = stop_shortY
                    target = text2 
                    number = '2'
                
                word_to_reply = '{}'.format(text) + '\n' + 'now {} {} ({}%)'.format(price_now,change,chgp)
                result = 'Position: {}'.format(notice) + '\n' + 'Range: {} - {} '.format(start,buy) + '\n' + 'Stop: {}'.format(stop) + '\n' + 'Target: {}'.format(target)
                bubble = flex_wticheck(text,price_now,change,chgp,notice,start,buy,stop,target)
                
                flex_to_reply = SetMessage_Object(bubble)
                reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
                return 'OK'
            wticheck()

        elif 'TFEX' in text_from_user:
            from urllib.request import Request, urlopen
            from bs4 import BeautifulSoup as soup 

            def tfexupdate():
                req = Request('https://www.tfex.co.th/tfex/dailySeriesQuotation.html?locale=th_TH&symbol=S50H20', headers={'User-Agent': 'Chrome/78.0'})
                webopen = urlopen(req).read()
                data = soup(webopen, 'html.parser')
                main = data.findAll('span',{'class':'h2'})
                
                tx = main[0].text
                tx = tx.replace('\n','')
                tx = tx.replace('\r','')
                tx = tx.replace(' ','')
                tx = tx.replace(',','')

                sub = data.findAll('span',{'class':'h3'})
                ux = sub[0].text
                ux = ux.replace('\n','')
                ux = ux.replace('\r','')
                ux = ux.replace(' ','')

                cx = sub[1].text
                cx = cx.replace('\n','')
                cx = cx.replace('\r','')
                cx = cx.replace(' ','')
                cx = cx.replace(')','')
                cx = cx.replace('(','')
                return[tx,ux,cx]

            def tfexcheck():
                tff = tfexupdate()

                exit_long1 = float(tff[0]) * 1.04
                exit_long1 = '%.2f'%exit_long1

                exit_long2 = float(tff[0]) * 1.08
                exit_long2 = '%.2f'%exit_long2

                exit_long3 = float(tff[0]) * 1.12
                exit_long3 = '%.2f'%exit_long3      

                exit_short1 = float(tff[0]) * 0.96
                exit_short1 = '%.2f'%exit_short1

                exit_short2 = float(tff[0]) * 0.92
                exit_short2 = '%.2f'%exit_short2

                exit_short3 = float(tff[0]) * 0.88
                exit_short3 = '%.2f'%exit_short3

                LongY = float(tfexx) * 1.005
                LongY = '%.2f'%LongY

                stop_longY = float(tfexx) * 0.995
                stop_longY = '%.2f'%stop_longY     

                shortY = float(tfexx) * 0.995
                shortY = '%.2f'%shortY

                stop_shortY = float(tfexx) * 1.0025
                stop_shortY = '%.2f'%stop_shortY                    

                price_now = float(tff[0])
                price_now = '%.2f'%price_now
                price_now = str(price_now)
                
                barW = float(price_now) - float(tfexx)
                chgp = str(tff[2])

                text1 = exit_long1 + ' | ' + exit_long2 + ' | ' + exit_long3 
                text2 = exit_short1 + ' | ' + exit_short2 + ' | ' + exit_short3 

                alert1 = 'ชนแนวต้าน'
                alert2 = 'Long'
                alert3 = 'Short'
                alert4 = 'กำลังย่อ'

                text = text_from_user
                change = str(tff[1]) 

                if barW >= 0:
                    notice = alert2
                    start = tfexx
                    buy = LongY
                    stop = stop_longY
                    target = text1
                    number = '1'
                else:
                    notice = alert3
                    start = tfexx
                    buy = shortY
                    stop = stop_shortY
                    target = text2 
                    number = '2'
                
                word_to_reply = '{}'.format(text) + '\n' + 'now {} {} ({}%)'.format(price_now,change,chgp)
                result = 'Position: {}'.format(notice) + '\n' + 'Range: {} - {} '.format(start,buy) + '\n' + 'Stop: {}'.format(stop) + '\n' + 'Target: {}'.format(target)
                bubble = flex_tfexcheck(text,price_now,change,chgp,notice,start,buy,stop,target)
                
                flex_to_reply = SetMessage_Object(bubble)
                reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
                return 'OK'
            tfexcheck()

        elif 'SET' in text_from_user:
            from urllib.request import Request, urlopen
            from bs4 import BeautifulSoup as soup 
        
            def setnow():
                req = Request('https://www.settrade.com/C13_MarketSummary.jsp?detail=SET', headers={'User-Agent': 'Chrome/78.0'})
                webopen = urlopen(req).read()
                data = soup(webopen, 'html.parser')
                currency = data.findAll('div',{'class':'col-xs-12'})

                st = currency[0].text
                st = st.replace('\n',' ')
                st = st.replace('\r',' ')
                st = st.replace('\n',' ')
                st = st[3316:]
                st = st[0:9]
                st = st.replace(',','')

                chg = currency[0].text
                chg = chg.replace('\n',' ')
                chg = chg.replace('\r',' ')
                chg = chg.replace('\n',' ')
                chg = chg[3325:]
                chg = chg[0:7]

                chgp = currency[0].text
                chgp = chgp.replace('\n',' ')
                chgp = chgp.replace('\r',' ')
                chgp = chgp.replace('\n',' ')
                chgp = chgp[3370:]
                chgp = chgp[0:5]
                return[st,chg,chgp]

            def setcheck():
                st = setnow()
                exit_long1 = float(st[0]) * 1.04
                exit_long1 = '%.2f'%exit_long1

                exit_long2 = float(st[0]) * 1.08
                exit_long2 = '%.2f'%exit_long2

                exit_long3 = float(st[0]) * 1.12
                exit_long3 = '%.2f'%exit_long3      

                exit_short1 = float(st[0]) * 0.96
                exit_short1 = '%.2f'%exit_short1

                exit_short2 = float(st[0]) * 0.92
                exit_short2 = '%.2f'%exit_short2

                exit_short3 = float(st[0]) * 0.88
                exit_short3 = '%.2f'%exit_short3

                LongY = float(sett) * 1.005
                LongY = '%.2f'%LongY

                stop_longY = float(sett) * 0.995
                stop_longY = '%.2f'%stop_longY     

                shortY = float(sett) * 0.995
                shortY = '%.2f'%shortY

                stop_shortY = float(sett) * 1.0025
                stop_shortY = '%.2f'%stop_shortY                    

                price_now = float(st[0])
                price_now = '%.2f'%price_now
                price_now = str(price_now)
                
                barW = float(price_now) - float(sett)
                chgp = str(st[2])

                text1 = exit_long1 + ' | ' + exit_long2 + ' | ' + exit_long3 
                text2 = exit_short1 + ' | ' + exit_short2 + ' | ' + exit_short3 

                alert1 = 'ชนแนวต้าน'
                alert2 = 'Long'
                alert3 = 'Short'
                alert4 = 'กำลังย่อ'

                text = text_from_user
                change = str(st[1]) 

                if barW >= 0:
                    notice = alert2
                    start = sett
                    buy = LongY
                    stop = stop_longY
                    target = text1
                    number = '1'
                else:
                    notice = alert3
                    start = sett
                    buy = shortY
                    stop = stop_shortY
                    target = text2 
                    number = '2'
                
                word_to_reply = '{}'.format(text) + '\n' + 'now {} {} ({}%)'.format(price_now,change,chgp)
                result = 'Position: {}'.format(notice) + '\n' + 'Range: {} - {} '.format(start,buy) + '\n' + 'Stop: {}'.format(stop) + '\n' + 'Target: {}'.format(target)
                bubble = flex_setcheck(text,price_now,change,chgp,notice,start,buy,stop,target)
                
                flex_to_reply = SetMessage_Object(bubble)
                reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
                return 'OK'
            setcheck()

        else:
            from bs4 import BeautifulSoup as soup
            from urllib.request import urlopen as req
            from pandas_datareader import data
            from datetime import datetime
                    
            code = text_from_user
            ticket = [text_from_user]
            symbols = list(map(lambda e: e + '.bk', ticket))
            
            def request(code):
                url = 'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol={}&ssoPageId=10&selectPage=2'.format(code)
                webopen = req(url)
                page_html = webopen.read()
                webopen.close()

                data = soup(page_html, 'html.parser')
                price = data.findAll('div',{'class':'col-xs-6'})
                title = price[0].text
                stockprice = price[2].text

                change = price[3].text
                change = change.replace('\n','')
                change = change.replace('\r','')
                change = change.replace('\t','')
                change = change.replace(' ','')
                change = change[11:]

                pchange = price[4].text
                pchange = pchange.replace('\n','')
                pchange = pchange.replace('\r','')
                pchange = pchange.replace(' ','')
                pchange = pchange[12:]

                update = data.findAll('span',{'class':'stt-remark'})
                stockupdate = update[0].text
                stockupdate = stockupdate[13:]
                return [title,stockprice,change,pchange,stockupdate]

            r = request(code)

            # text_request = '{} {} ({})'.format(r[0], r[1], r[2])

            class stock:
                def __init__(self,stock):
                    self.stock = stock
                def ticket(self):
                    end = datetime.now()
                    start = datetime(end.year,end.month,end.day)
                    list = self.stock

                    dfY = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
                    dfQ = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)
                    #chg for Quarter : Jan Apr Jul Sep

                    dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-03-16', end=end)
                    #2020-01-01 = Y M D

                    list = list.replace('.bk','')
                                
                    OpenY = dfY['Open'].iloc[0]
                    OpenY  = '%.2f'%OpenY
                    OpenY = str(OpenY)

                    OpenQ = dfQ['Open'].iloc[0]
                    OpenQ  = '%.2f'%OpenQ
                    OpenQ = str(OpenQ)

                    OpenW = dfQ['Open'].iloc[0]
                    OpenW  = '%.2f'%OpenW
                    OpenW = str(OpenW)

                    Close = float(f'{r[1]}')
                    Close  = '%.2f'%Close
                    Close = str(Close)

                    barY = ((float(Close) - float(OpenY)) / float(OpenY) )*100
                    barY = '%.2f'%barY
                    barY = float(barY)

                    barQ = ((float(Close) - float(OpenQ)) / float(OpenQ) )*100
                    barQ = '%.2f'%barQ
                    barQ = float(barQ)

                    barW = ((float(Close) - float(OpenW)) / float(OpenW) )*100
                    barW = '%.2f'%barW
                    barW = float(barW)

                    Volume1 = dfQ['Volume'].iloc[-1]
                    Volume2 = dfQ['Volume'].iloc[-2]
                    Volume = (float(Volume1)+float(Volume2))/2
                    Volume  = '%.0f'%Volume
                    Volume = str(Volume)

                    value = float(Volume) * float(Close)
                    value  = '%.2f'%value
                    value = str(value)

                    request_val = float(value) 
                    request_val  = '{:,.0f}'.format(request_val)
                    request_val = str(request_val)
                    
                    exit1 = float(r[1]) * 1.06
                    exit1 = '%.2f'%exit1
                    exit1 = str(exit1)

                    exit2 = float(r[1]) * 1.12
                    exit2 = '%.2f'%exit2
                    exit2 = str(exit2)

                    exit3 = float(r[1]) * 1.18
                    exit3 = '%.2f'%exit3
                    exit3 = str(exit3)

                    buyQ = float(OpenQ) * 1.01
                    buyQ = '%.2f'%buyQ
                    buyQ = str(buyQ) 

                    stopQ = float(OpenQ) * 0.985
                    stopQ = '%.2f'%stopQ
                    stopQ = str(stopQ) 

                    buyY = float(OpenY) * 1.01
                    buyY = '%.2f'%buyY
                    buyY = str(buyY) 

                    stopY = float(OpenY) * 0.985
                    stopY = '%.2f'%stopY
                    stopY = str(stopY) 

                    support1 = float(OpenY) * 0.75
                    support1 = '%.2f'%support1
                    support1 = str(support1)

                    support2 = float(OpenY) * 0.65
                    support2 = '%.2f'%support2
                    support2 = str(support2)

                    support3 = float(OpenY) * 0.50
                    support3 = '%.2f'%support3
                    support3 = str(support3)

                    chgp = str(r[3])

                    text1 = exit1 + ' | ' + exit2 + ' | ' + exit3 
                    text2 = support1 + ' | ' + support2 + ' | ' + support3  

                    alert1 = 'ชนแนวต้าน'
                    alert2 = 'ไปต่อ'
                    alert3 = 'ซื้อ'
                    alert4 = 'อย่าเพิ่งเข้า'
                    alert5 = 'กำลังย่อ'
                    alert6 = 'น่าสนใจ'
                    alert7 = 'รอเข้า'
                    alert8 = 'รอต่ำ'
                    alert9 = 'Vol น้อย'

                    text = r[0]
                    price_now = r[1] 
                    change = r[2] 

                    if float(value) > 7500000:
                        if barY > 3.00:
                            if barQ > 6.00:
                                notice = alert1
                                stop = stopQ
                                start = OpenQ
                                buy = buyQ
                                target = text1
                                avg = barQ
                            elif barQ >= 3.00:
                                if barW >= 0:
                                    notice = alert2
                                    stop = stopQ
                                    start = OpenQ
                                    buy = buyQ
                                    target = text1
                                    avg = barQ
                                else:
                                    notice = alert7
                                    stop = stopQ
                                    start = OpenQ
                                    buy = buyQ
                                    target = text1
                                    avg = barQ
                            elif barQ >= 0.00:
                                if barW >= 0:
                                    notice = alert3
                                    stop = stopQ
                                    start = OpenQ
                                    buy = buyQ
                                    target = text1
                                    avg = barQ
                                else:
                                    notice = alert7
                                    stop = stopQ
                                    start = OpenQ
                                    buy = buyQ
                                    target = text1
                                    avg = barQ
                            else:
                                notice = alert4
                                stop = stopQ
                                start = OpenQ
                                buy = buyQ
                                target = text2
                                avg = barQ
                        elif barY >= 0.00:
                            if barQ >= 0:
                                if barW > 0:
                                    notice = alert6
                                    stop = stopY
                                    start = OpenY
                                    buy = buyY
                                    target = text1
                                    avg = barY
                                else:
                                    notice = alert7
                                    stop = stopY
                                    start = OpenY
                                    buy = buyY
                                    target = text1
                                    avg = barY
                            else:
                                notice = alert5
                                stop = stopY
                                start = OpenY
                                buy = buyY
                                target = text2
                                avg = barY
                        else:
                            if barQ > 6.00:
                                notice = alert1
                                stop = stopQ
                                start = OpenQ
                                buy = buyQ
                                target = text1
                                avg = barQ
                            elif barQ >= 3.00:
                                if barW >= 0:
                                    notice = alert2
                                    stop = stopQ
                                    start = OpenQ
                                    buy = buyQ
                                    target = text1
                                    avg = barQ
                                else:
                                    notice = alert8
                                    stop = stopQ
                                    start = OpenQ
                                    buy = buyQ
                                    target = text1
                                    avg = barQ
                            elif barQ >= 0.00:
                                if barW >= 0:
                                    notice = alert3
                                    stop = stopQ
                                    start = OpenQ
                                    buy = buyQ
                                    target = text1
                                    avg = barQ
                                else:
                                    notice = alert8
                                    stop = stopQ
                                    start = OpenQ
                                    buy = buyQ
                                    target = text1
                                    avg = barQ
                            else:
                                notice = alert4
                                stop = stopQ
                                start = OpenQ
                                buy = buyQ
                                target = text2
                                avg = barQ
                    else:
                        notice = alert9
                        stop = stopQ
                        start = OpenQ
                        buy = buyQ
                        target = text2
                        avg = barQ

                    word_to_reply = str('{} {}'.format(text,notice))
                    print(word_to_reply)
                    bubbles = []
                    bubble = flex_stock(text,price_now,change,chgp,notice,start,buy,stop,target,avg)
                    
                    flex_to_reply = SetMessage_Object(bubble)
                    reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
                    return 'OK'
            for symbol in symbols:
                stock(symbol).ticket()

    except:
        text_list = [
            '{} ไม่มีในฐานข้อมูล {} ลองใหม่อีกครั้ง'.format(text_from_user,disname),
            '{} ค้นหาหุ้น {} ไม่ถูกต้อง ลองใหม่อีกครั้ง'.format(disname, text_from_user),
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

    button_1 = QuickReplyButton(action=MessageAction(lable='สวัสดี',text='สวัสดี'))
    answer_button = QuickReply(items=[button_1])
            
if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Credentials.json"
    os.environ["DIALOGFLOW_PROJECT_ID"] = "worldstock-iardyn"
    port = int(os.getenv('PORT', 2000))
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)