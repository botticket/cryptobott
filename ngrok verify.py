from utils.csvFinder import csvFinder
from utils.dialogflow_uncle import detect_intent_texts

import os
import sys
from flask import Flask, request, abort, send_from_directory, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,FollowEvent,QuickReply,QuickReplyButton,MessageAction

app = Flask(__name__)

Channel_secret = 'afe7ec6bede0dde581d0a61b6447653b'
Channel_access_token = 'hkU+OYWsepq11sc+uM6bAE/ECjFb8+NUiTvjfQI1WUrXzKiUZvHU5YAv+AEG4I6ZZuJPflQ/v5Gp2XH5m5TtLeUkPpX3JUjqTKFWahSOIqWheppXpKvFyE+olbJyAGvg9f8pciPntSGZnLbfyAIoyQdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(Channel_access_token)
handler = WebhookHandler(Channel_secret)

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
    request_text= (' ticket'+'\n' + '>> {} : {}').format(disname,text_from_user)
    print(request_text)


if __name__ == '__main__':
    port = int(os.getenv('PORT', 2000))
    #print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)