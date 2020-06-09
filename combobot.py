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
    
    ACCESS_TOKEN = "oK2sk4w1eidfRyOVfgIcln38TBS8JmL0PgfbbQ8t0Zv"

    notify = LineNotify(ACCESS_TOKEN)

    notify.send(text)

@app.route("/callback", methods=['POST'])
def callback():
	signature = request.headers['X-Line-Signature']
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)
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
        if action == "Welcome_response":
            all_text = []
            for each in response:
                text = TextSendMessage(text=each)
                all_text.append(text)
            line_bot_api.reply_message(reply_token,messages=all_text) #reply messageกลับไป
            return 'OK'

        elif 'สวัสดี' in text_from_user:    
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

        elif action == "crypto_response":
            from urllib.request import Request, urlopen
            from bs4 import BeautifulSoup as soup 
            from pandas_datareader import data
            from datetime import datetime
            
            text_from_user = text_from_user.upper()
            code = [text_from_user]
            codes = list(map(lambda e: e + '-USD', code))

            class crypto:
                def __init__(self,code):
                    self.code = code
                def ticket(self):
                    end = datetime.now()
                    start = datetime(end.year,end.month,end.day)
                    list = self.code

                    dfY = data.DataReader(f'{list}', data_source="yahoo", start=yearly, end=end)
                    dfM = data.DataReader(f'{list}', data_source="yahoo", start=monthly, end=end)
                    #2020-01-01 = Y M D

                    OpenY = dfY['Open'].iloc[1]
                    OpenY  = '%.2f'%OpenY
                    OpenY = str(OpenY)

                    OpenM = dfM['Open'].iloc[1]
                    OpenM  = '%.2f'%OpenM
                    OpenM = str(OpenM)

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

                    barM = ((float(Close) - float(OpenM)) / float(OpenM) )*100
                    barM = '%.2f'%barM
                    barM = float(barM)

                    LongY = float(OpenM) * 1.01
                    LongY = '%.2f'%LongY
                    LongY = str(LongY) 

                    stop_longY = float(OpenM) * 0.985
                    stop_longY = '%.2f'%stop_longY
                    stop_longY = str(stop_longY)

                    exit_long1 = float(OpenD) * 1.04
                    exit_long1 = '%.2f'%exit_long1
                    exit_long1 = str(exit_long1)

                    exit_long2 = float(OpenD) * 1.08
                    exit_long2 = '%.2f'%exit_long2
                    exit_long2 = str(exit_long2)

                    exit_long3 = float(OpenD) * 1.15
                    exit_long3 = '%.2f'%exit_long3
                    exit_long3 = str(exit_long3)

                    shortY = float(OpenM) * 0.985
                    shortY = '%.2f'%shortY
                    shortY = str(shortY) 

                    stop_shortY = float(OpenM) * 1.01
                    stop_shortY = '%.2f'%stop_shortY
                    stop_shortY = str(stop_shortY)

                    exit_short1 = float(OpenD) * 0.96
                    exit_short1 = '%.2f'%exit_short1
                    exit_short1 = str(exit_short1)

                    exit_short2 = float(OpenD) * 0.92
                    exit_short2 = '%.2f'%exit_short2
                    exit_short2 = str(exit_short2)

                    exit_short3 = float(OpenD) * 0.88
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

                    alert1 = 'Long'
                    alert2 = 'Short'

                    text = code
                    price_now = float(Close) 
                    change = str(change) 

                    if barM >= 0:
                        notice = alert1
                        start = OpenM
                        buy = LongY
                        stop = stop_longY
                        target = text1
                        number = '1'
                    else:
                        notice = alert2
                        start = OpenM
                        buy = shortY
                        stop = stop_shortY
                        target = text2 
                        number = '2'

                    word_to_reply = '{}'.format(text) + '\n' + 'now {} {} ({}%)'.format(price_now,change,chgp)
                    result = 'Position: {}'.format(notice) + '\n' + 'Range: {} - {} '.format(start,buy) + '\n' + 'Stop: {}'.format(stop) + '\n' + 'Target: {}'.format(target)
                    print(result)
                    print(number)
                    bubble = flex_crypto(text,price_now,change,chgp,notice,start,buy,stop,target)
                    
                    flex_to_reply = SetMessage_Object(bubble)
                    reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
                    return 'OK'

            for code in codes:
                crypto(code).ticket()

        else:
            from bs4 import BeautifulSoup as soup
            from urllib.request import urlopen as req
            from pandas_datareader import data
            from datetime import datetime, date
                    
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

            class stock:
                def __init__(self,stock):
                    self.stock = stock
                def ticket(self):
                    end = datetime.now()
                    start = datetime(end.year,end.month,end.day)
                    list = self.stock

                    dfY = data.DataReader(f'{list}', data_source="yahoo", start=yearly, end=end)
                    dfQ = data.DataReader(f'{list}', data_source="yahoo", start=quarter, end=end)
                    dfM = data.DataReader(f'{list}', data_source="yahoo", start=monthly, end=end)
                    # dfM = data.DataReader(f'{list}', data_source="yahoo", start='2020-04-01', end=end)

                    list = list.replace('.bk','')
                                
                    OpenY = dfY['Open'].iloc[0]
                    OpenY  = '%.2f'%OpenY
                    OpenY = str(OpenY)

                    OpenQ = dfQ['Open'].iloc[0]
                    OpenQ  = '%.2f'%OpenQ
                    OpenQ = str(OpenQ)

                    p_OpenQ = ((float(OpenQ) - float(OpenY)) / float(OpenY))*100
                    p_OpenQ  = '%.2f'%p_OpenQ
                    p_OpenQ = str(p_OpenQ)

                    OpenM = dfM['Open'].iloc[0]
                    OpenM  = '%.2f'%OpenM
                    OpenM = str(OpenM)

                    Close = float(f'{r[1]}')
                    Close  = '%.2f'%Close
                    Close = str(Close)

                    barY = ((float(Close) - float(OpenY)) / float(OpenY) )*100
                    barY = '%.2f'%barY
                    barY = float(barY)

                    barQ = ((float(Close) - float(OpenQ)) / float(OpenQ) )*100
                    barQ = '%.2f'%barQ
                    barQ = float(barQ)

                    barM = ((float(Close) - float(OpenM)) / float(OpenM) )*100
                    barM = '%.2f'%barM
                    barM = float(barM)

                    Volume1 = dfY['Volume'].iloc[-1]
                    Volume2 = dfY['Volume'].iloc[-2]

                    Volume = (float(Volume1)+float(Volume2))/2
                    Volume  = '%.0f'%Volume
                    Volume = str(Volume)

                    value = float(Volume) * float(Close)
                    value  = '%.2f'%value
                    value = str(value)

                    request_val = float(value) 
                    request_val  = '{:,.0f}'.format(request_val)
                    request_val = str(request_val)
                    
                    exit1 = float(OpenQ) * 1.20
                    exit1 = '%.2f'%exit1
                    exit1 = str(exit1)

                    exit2 = float(OpenQ) * 1.40
                    exit2 = '%.2f'%exit2
                    exit2 = str(exit2)

                    exit3 = float(OpenQ) * 1.60
                    exit3 = '%.2f'%exit3
                    exit3 = str(exit3)

                    max_value = dfY.nlargest(1, columns = 'High')
                    max_value = max_value['High'].iloc[0]
                    max_value = '%.2f'%max_value
                    max_value = str(max_value) 
                    
                    max_Qvalue = dfQ.nlargest(1, columns = 'High')
                    max_Qvalue = max_Qvalue['High'].iloc[0]
                    max_Qvalue = '%.2f'%max_Qvalue
                    max_Qvalue = str(max_Qvalue) 

                    pmax_value = ((float(max_value) - float(OpenY)) / float(OpenY)) * 100
                    pmax_value = '%.2f'%pmax_value
                    pmax_value = str(pmax_value)  

                    min_value = dfY.nsmallest(1, columns = 'Low')
                    min_value = min_value['Low'].iloc[0]
                    min_value = '%.2f'%min_value
                    min_value = str(min_value) 

                    pmin_value = ((float(min_value) - float(OpenY)) / float(OpenY)) * 100
                    pmin_value = '%.2f'%pmin_value
                    pmin_value = str(pmin_value)

                    support1 = float(max_value) * 0.90
                    support1 = '%.2f'%support1
                    support1 = str(support1)

                    pfibo_Q1 = (((float(Close) - float(support1))/float(support1)))*100  
                    pfibo_Q1  = '%.2f'%pfibo_Q1
                    pfibo_Q1 = str(pfibo_Q1) 

                    support2 = float(max_value) * 0.80
                    support2 = '%.2f'%support2
                    support2 = str(support2)

                    pfibo_Q2 = (((float(Close) - float(support2))/float(support2)))*100     
                    pfibo_Q2 = '%.2f'%pfibo_Q2
                    pfibo_Q2 = str(pfibo_Q2) 

                    support3 = float(max_value) * 0.70
                    support3 = '%.2f'%support3
                    support3 = str(support3)

                    pfibo_Q3 = (((float(Close) - float(support3))/float(support3)))*100     
                    pfibo_Q3  = '%.2f'%pfibo_Q3
                    pfibo_Q3 = str(pfibo_Q3) 

                    support4 = float(max_value) * 0.60
                    support4 = '%.2f'%support4
                    support4 = str(support4)

                    pfibo_Q4 = (((float(Close) - float(support4))/float(support4)))*100     
                    pfibo_Q4  = '%.2f'%pfibo_Q4
                    pfibo_Q4 = str(pfibo_Q4)

                    support5 = float(max_value) * 0.50
                    support5 = '%.2f'%support5
                    support5 = str(support5)

                    pfibo_Q5 = (((float(Close) - float(support5))/float(support5)))*100     
                    pfibo_Q5  = '%.2f'%pfibo_Q5
                    pfibo_Q5 = str(pfibo_Q5)

                    support6 = float(max_value) * 0.40
                    support6 = '%.2f'%support6
                    support6 = str(support6)

                    pfibo_Q6 = (((float(Close) - float(support6))/float(support6)))*100     
                    pfibo_Q6  = '%.2f'%pfibo_Q6
                    pfibo_Q6 = str(pfibo_Q6)

                    ChgY = ((float(r[1]) - float(OpenY))/ float(OpenY))*100
                    ChgY  = '%.2f'%ChgY
                    ChgY = str(ChgY)

                    ChgQ = ((float(r[1]) - float(OpenQ))/ float(OpenQ))*100
                    ChgQ  = '%.2f'%ChgQ
                    ChgQ = str(ChgQ)

                    ChgM = ((float(r[1]) - float(OpenM)) / float(OpenM) )*100
                    ChgM = '%.2f'%ChgM
                    ChgM = float(ChgM)	
                    
                    text1 = exit1 + ' | ' + exit2 + ' | ' + exit3 

                    alert2 = 'ไปต่อ'
                    alert3 = 'ซื้อ Y / Q'
                    alert4 = 'เปลี่ยนตัว'
                    alert5 = 'ขายแล้วรอ'
                    alert7 = 'ซื้อ'
                    alert8 = 'ลงต่อ'
                    alert9 = 'Vol น้อย'
                    alert10 = 'ดูตลาด'

                    text = r[0]
                    price_now = r[1] 
                    change = r[2] 
                    chgp = str(ChgQ)
                    re_avg = 'Q {} ({}%) | M {}'.format(OpenQ,p_OpenQ,OpenM) + '\n' + 'Y {} ({}%)'.format(OpenY,barY)+ '\n' + 'H {} | L {}({}%)'.format(max_Qvalue,min_value,pmin_value)

                    if float(value) > 7500000:
                        if  barY > 0.00:
                            if barQ >= 0.00:
                                if barM > 0.00:
                                    if 0.00 < float(barY) < 3.00:
                                        notice = alert3
                                        start = OpenY
                                        stop = 'H {} | L {}'.format(max_Qvalue,min_value)
                                        target = text1
                                        avg = re_avg
                                    elif 0.00 < float(barQ) < 3.00:
                                        notice = alert7
                                        start = OpenQ
                                        stop = 'H {} | L {}'.format(max_Qvalue,min_value)
                                        target = text1
                                        avg = re_avg
                                    else:
                                        notice = alert2
                                        start = OpenQ
                                        stop = 'H {} | L {}'.format(max_Qvalue,min_value)
                                        target = text1
                                        avg = re_avg
                                else:
                                    if 0.00 < float(barY) < 3.00:
                                        notice = alert5
                                        start = OpenY
                                        stop = 'H {} | L {}'.format(max_Qvalue,min_value)
                                        target = text1
                                        avg = re_avg
                                    elif 0.00 < float(barQ) < 3.00:
                                        notice = alert5
                                        start = OpenQ
                                        stop = 'H {} | L {}'.format(max_Qvalue,min_value)
                                        target = text1
                                        avg = re_avg
                                    else:
                                        notice = alert10
                                        start = OpenQ
                                        stop = 'H {} | L {}'.format(max_Qvalue,min_value)
                                        target = text1
                                        avg = re_avg
                            else:
                                notice = alert4
                                start = OpenQ
                                stop = 'H {} | L {}'.format(max_Qvalue,min_value)
                                target = text1
                                avg = re_avg
                        else:
                            if barQ >= 0.00:
                                if float(Close) >= float(support1):
                                    if barM > 0.00:
                                        notice = alert7
                                        start = float(support1)
                                        stop = text1
                                        target = '{} | {} | {}'.format(support3,support2,support1)
                                        avg = re_avg
                                    else:
                                        notice = alert5
                                        start = float(support1)
                                        stop = text1
                                        target = '{} | {} | {}'.format(support3,support2,support1)
                                        avg = re_avg
                                elif float(Close) >= float(support2):
                                    if barM > 0.00:
                                        notice = alert7
                                        start = float(support2)
                                        stop = text1
                                        target = '{} | {} | {}'.format(support4,support3,support2)
                                        avg = re_avg   
                                    else:
                                        notice = alert5
                                        start = float(support2)
                                        stop = text1
                                        target = '{} | {} | {}'.format(support4,support3,support2)
                                        avg = re_avg
                                elif float(Close) >= float(support3):
                                    if barM > 0.00:
                                        notice = alert7
                                        start = float(support3)
                                        stop = text1
                                        target = '{} | {} | {}'.format(support5,support4,support3)
                                        avg = re_avg
                                    else:
                                        notice = alert5
                                        start = float(support3)
                                        stop = text1
                                        target = '{} | {} | {}'.format(support5,support4,support3)
                                        avg = re_avg  
                                elif float(Close) >= float(support4):
                                    if barM > 0.00:
                                        notice = alert7
                                        start = float(support4)
                                        stop = text1
                                        target = '{} | {} | {}'.format(support6,support5,support4)
                                        avg = re_avg
                                    else:
                                        notice = alert5
                                        start = float(support4) 
                                        stop = text1
                                        target = '{} | {} | {}'.format(support6,support5,support4)
                                        avg = re_avg 
                                elif float(Close) >= float(support5):
                                    if barM > 0.00:
                                        notice = alert7
                                        start = float(support5)
                                        stop = text1
                                        target = '{} | {} | {}'.format(support6,support5,support4)
                                        avg = re_avg
                                    else:
                                        notice = alert5
                                        start = float(support5) 
                                        stop = text1
                                        target = '{} | {} | {}'.format(support6,support5,support4)
                                        avg = re_avg 
                                elif float(Close) >= float(support6):
                                    if barM > 0.00:
                                        notice = alert7
                                        start = float(support6)
                                        stop = text1
                                        target = '{} | {} | {}'.format(support6,support5,support4)
                                        avg = re_avg
                                    else:
                                        notice = alert5
                                        start = float(support6) 
                                        stop = text1
                                        target = '{} | {} | {}'.format(support6,support5,support4)
                                        avg = re_avg 
                                else:
                                    notice = alert4
                                    start = OpenQ
                                    stop = 'H {} | L {}'.format(max_Qvalue,min_value)
                                    target = text1
                                    avg = re_avg
                            else:
                                notice = alert4
                                start = OpenQ
                                stop = 'H {} | L {}'.format(max_Qvalue,min_value)
                                target = text1
                                avg = re_avg
                    else:
                        notice = alert9
                        start = OpenQ
                        stop = 'H {} ~ L {}'.format(max_Qvalue,min_value)
                        target = text1
                        avg = re_avg 

                    word_to_reply = str('{} {}'.format(text,notice))
                    print(word_to_reply)
                    bubbles = []
                    bubble = flex_stock(text,price_now,change,chgp,notice,start,stop,target,avg)
                    
                    flex_to_reply = SetMessage_Object(bubble)
                    reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
                    return 'OK'

            for symbol in symbols:
                stock(symbol).ticket()

    except:
        text_list = [
            'คุณ {} กำลังค้นหา {} ในฐานข้อมูล'.format(disname, text_from_user),
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