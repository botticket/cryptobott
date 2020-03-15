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
    request_text= (' mybot'+'\n' + '>> {} : {}').format(disname,text_from_user)

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
        
    if action == "Welcome_response":
        all_text = []
        for each in response:
            text = TextSendMessage(text=each)
            all_text.append(text)
    
        line_bot_api.reply_message(reply_token,messages=all_text) #reply messageกลับไป
        
        return 'OK'
  
    else:

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

                dfY = data.DataReader(f'{list}', data_source="yahoo", start='2020-01-01', end=end)

                dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-03-09', end=end)
                #2020-01-01 = Y M D

                list = list.replace('.bk','')

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
            crypto(code).ticket()

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