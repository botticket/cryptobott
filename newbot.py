import os
import sys

from flask import Flask, request, abort, send_from_directory, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,FollowEvent,QuickReply,QuickReplyButton,MessageAction
from line_notify import LineNotify
from reply import reply_msg , SetMessage_Object
from flex_stock import *
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
    
    # try:
    if 'IQXUSTB' in text_from_user:

        from urllib.request import Request, urlopen
        from bs4 import BeautifulSoup as soup 

        def usdscrapt():
            req = Request('https://th.investing.com/currencies/usd-thb', headers={'User-Agent': 'Chrome/78.0'})
            webopen = urlopen(req).read()
            data = soup(webopen, 'html.parser')

            usthbrate = data.findAll('div',{'class':'top bold inlineblock'})
            usthbrate = usthbrate[0].text
            usthbrate = usthbrate.replace('\n',' ')
            usthbrate = usthbrate.replace(',','')
            usthbrate = usthbrate[1:]
            usthbrate = usthbrate[0:6]

            xusthbrate = data.findAll('div',{'class':'top bold inlineblock'})
            xusthbrate = xusthbrate[0].text
            xusthbrate = xusthbrate.replace('\n',' ')
            xusthbrate = xusthbrate.replace(',','')
            xusthbrate = xusthbrate[1:]
            xusthbrate = xusthbrate[7:13]
            return[usthbrate,xusthbrate]

        def usdcheck():
            IQXUSTHB = '29.76'
            #chg for Quarter : Jan Apr Jul Sep
            #1.015 1.03 0.985 0.97

            uu = usdscrapt()
            targetUp_01 = float(uu[0]) * 1.015
            targetUp_01 = '%.2f'%targetUp_01

            targetUp_02 = float(uu[0]) * 1.03
            targetUp_02 = '%.2f'%targetUp_02
            
            targetDown_01 = float(uu[0]) * 0.985
            targetDown_01 = '%.2f'%targetDown_01

            targetDown_02 = float(uu[0]) * 0.97
            targetDown_02 = '%.2f'%targetDown_02

            usthbspot = float(uu[0])
            usthbspot = '%.2f'%usthbspot

            buy = float(usthbspot) + 0.02 #dif rate buy
            buy = '%.2f'%buy
            sale = float(usthbspot) - 0.06 #dif rate sale
            sale = '%.2f'%sale

            text = 'IQXUSTB' 
            text2 = 'ค่าเงินอ่อน'
            text3 = 'ค่าเงินแข็ง' 
            Percent = ' (' + uu[1] + ')'
            comment = 'ซื้อ ' + sale + ' / ขาย '+ buy + '\n' + 'X : {} / {}'.format(targetUp_01,targetUp_02)

            if float(usthbspot) >= float(IQXUSTHB):
                word_to_reply = text2
            else:
                word_to_reply = text3
            
            print(word_to_reply)

            bubbles = []
            bubble = flex_THB(text,usthbspot,Percent,word_to_reply,IQXUSTHB,comment)
            
            flex_to_reply = SetMessage_Object(bubble)
            reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
            return 'OK'

        usdcheck()  
        
    elif 'IQXWTI' in text_from_user:

        from urllib.request import Request, urlopen
        from bs4 import BeautifulSoup as soup 

        def wtiscrapt():
            req = Request('https://th.investing.com/commodities/crude-oil', headers={'User-Agent': 'Chrome/78.0'})
            webopen = urlopen(req).read()
            data = soup(webopen, 'html.parser')

            wtirate = data.findAll('div',{'class':'top bold inlineblock'})
            wtirate = wtirate[0].text
            wtirate = wtirate.replace('\n',' ')
            wtirate = wtirate.replace(',','')
            wtirate = wtirate[1:]
            wtirate = wtirate[0:6]

            xwtirate = data.findAll('div',{'class':'top bold inlineblock'})
            xwtirate = xwtirate[0].text
            xwtirate = xwtirate.replace('\n',' ')
            xwtirate = xwtirate.replace(',','')
            xwtirate = xwtirate[1:]
            xwtirate = xwtirate[6:11]
            return[wtirate,xwtirate]

        def wticheck():
            IQXWTI = '61.35'
            #chg for Quarter : Jan Apr Jul Sep

            #1.06 1.12 0.94 0.88
            wti = wtiscrapt()
            targetUp_01 = float(wti[0]) * 1.015
            targetUp_01 = '%.2f'%targetUp_01

            targetUp_02 = float(wti[0]) * 1.03
            targetUp_02 = '%.2f'%targetUp_02
            
            targetDown_01 = float(wti[0]) * 0.985
            targetDown_01 = '%.2f'%targetDown_01

            targetDown_02 = float(wti[0]) * 0.97
            targetDown_02 = '%.2f'%targetDown_02

            wtispot = float(wti[0])
            wtispot = '%.2f'%wtispot

            text = 'IQXWTI'
            text1 = 'Long' 
            text2 = 'Short'
            Percent = ' (' + wti[1] + ')'
            target_Up = 'X : {} / {}'.format(targetUp_01,targetUp_02)
            target_Down = 'X : {} / {}'.format(targetDown_01,targetDown_02)

            if float(wtispot) >= float(IQXWTI):
                word_to_reply = text1 
                comment = target_Up
            else:
                word_to_reply = text2
                comment = target_Down
            
            print(word_to_reply,comment)

            bubbles = []
            bubble = flex_WTI(text,wtispot,Percent,word_to_reply,IQXWTI,comment)
            
            flex_to_reply = SetMessage_Object(bubble)
            reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
            return 'OK'

        wticheck()

    elif 'IQXGL' in text_from_user:

        from urllib.request import Request, urlopen
        from bs4 import BeautifulSoup as soup 

        def goldscrapt():
            req = Request('https://th.investing.com/currencies/xau-usd', headers={'User-Agent': 'Chrome/78.0'})
            webopen = urlopen(req).read()
            data = soup(webopen, 'html.parser')

            goldrate = data.findAll('div',{'class':'top bold inlineblock'})
            goldrate = goldrate[0].text
            goldrate = goldrate.replace('\n',' ')
            goldrate = goldrate.replace(',','')
            goldrate = goldrate[1:]
            goldrate = goldrate[0:8]

            xgoldrate = data.findAll('div',{'class':'top bold inlineblock'})
            xgoldrate = xgoldrate[0].text
            xgoldrate = xgoldrate.replace('\n',' ')
            xgoldrate = xgoldrate.replace(',','')
            xgoldrate = xgoldrate[9:]
            xgoldrate = xgoldrate[0:5]
            return[goldrate,xgoldrate]

        def goldcheck():
            IQXGL = '1517.18'
            #chg for Quarter : Jan Apr Jul Sep

            #1.06 1.12 0.94 0.88
            gg = goldscrapt()
            targetUp_01 = float(gg[0]) * 1.03
            targetUp_01 = '%.2f'%targetUp_01

            targetUp_02 = float(gg[0]) * 1.06
            targetUp_02 = '%.2f'%targetUp_02
            
            targetDown_01 = float(gg[0]) * 0.97
            targetDown_01 = '%.2f'%targetDown_01

            targetDown_02 = float(gg[0]) * 0.94
            targetDown_02 = '%.2f'%targetDown_02

            gspot = float(gg[0])
            gspot = '%.2f'%gspot
            gspot = str(gspot)

            text = 'IQXGL' 
            text2 = 'Long' 
            text3 = 'Short' 
            Percent = ' (' + gg[1] + ')'
            target_Up = 'X : {} / {}'.format(targetUp_01,targetUp_02)
            target_Down = 'X : {} / {}'.format(targetDown_01,targetDown_02)

            if float(gspot) >= float(IQXGL):
                word_to_reply = text2    
                comment = target_Up            
            else:
                word_to_reply = text3
                comment = target_Down            

            print(word_to_reply,comment)

            bubbles = []
            bubble = flex_gold(text,gspot,Percent,word_to_reply,IQXGL,comment)
            
            flex_to_reply = SetMessage_Object(bubble)
            reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
            return 'OK'

        goldcheck()

    elif 'TFEX' in text_from_user:
        from urllib.request import urlopen as req
        from bs4 import BeautifulSoup as soup 

        def tfexcheck():
            url = 'https://www.tfex.co.th/tfex/dailySeriesQuotation.html?locale=th_TH&symbol=S50H20'
            webopen = req(url)
            page_html = webopen.read()
            webopen.close()

            data = soup(page_html, 'html.parser')
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
            return[tx,ux,cx]

        def dailytfex():
            tfexx = '1065.20'
            #chg for Quarter : Jan Apr Jul Sep
            #S50H20 S50M20 S50U20 S50Z20
            #1.007 1.015 0.993 0.986
            tff = tfexcheck()
        
            targetUp_01 = float(tff[0]) * 1.007
            targetUp_01 = '%.2f'%targetUp_01

            targetUp_02 = float(tff[0]) * 1.014
            targetUp_02 = '%.2f'%targetUp_02
            
            targetDown_01 = float(tff[0]) * 0.993
            targetDown_01 = '%.2f'%targetDown_01

            targetDown_02 = float(tff[0]) * 0.986
            targetDown_02 = '%.2f'%targetDown_02

            text3 = 'S50H20' + '\n'+ tfexx +' > '+ tff[0] +' ('+ tff[1] +') ' + '\n'+'Status : Long' + '\n' + 'X : {} / {}'.format(targetUp_01,targetUp_02)
            text4 = 'S50H20' + '\n'+ tfexx +' > '+ tff[0] +' ('+ tff[1] +') ' + '\n'+ 'Status : Short' + '\n' + 'X : {} / {}'.format(targetDown_01,targetDown_02)
            
            text = 'S50H20'
            text2 = 'Long' 
            text3 = 'Short' 
            tfex_now = tff[0] 
            Percent = ' (' + tff[1] + ')'
            target_Up = 'X : {} / {}'.format(targetUp_01,targetUp_02)
            target_Down = 'X : {} / {}'.format(targetDown_01,targetDown_02)

            float(tff[0])
            if float(tff[0]) >= float(tfexx): 
                word_to_reply = text2 
                comment = target_Up          
            else:
                word_to_reply = text3
                comment = target_Down

            print(word_to_reply)

            bubbles = []
            bubble = flex_tfex(text,tfex_now,Percent,word_to_reply,tfexx,comment)
            
            flex_to_reply = SetMessage_Object(bubble)
            reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
            return 'OK'

        dailytfex()

    elif 'SET' in text_from_user:

        from urllib.request import urlopen as req
        from bs4 import BeautifulSoup as soup 

        def setcheck():
            url = 'https://www.settrade.com/C13_MarketSummary.jsp?detail=SET'
            webopen = req(url)
            page_html = webopen.read()
            webopen.close()

            data = soup(page_html, 'html.parser')
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
            chg = chg[0:5]
            return[st,chg]

        def dailyset():
            sett = '1584.34'
            #chg for Quarter : Jan Apr Jul Sep
            #1.007 1.015 0.993 0.986
            st = setcheck()

            targetUp_01 = float(st[0]) * 1.007
            targetUp_01 = '%.2f'%targetUp_01

            targetUp_02 = float(st[0]) * 1.014
            targetUp_02 = '%.2f'%targetUp_02
            
            targetDown_01 = float(st[0]) * 0.993
            targetDown_01 = '%.2f'%targetDown_01

            targetDown_02 = float(st[0]) * 0.986
            targetDown_02 = '%.2f'%targetDown_02

            text1 = 'SET Today :' + '\n' + sett +' > '+ st[0] +' ('+st[1]+') ' + '\n' + 'Status : Buy' + '\n' + 'X : {} / {}'.format(targetUp_01,targetUp_02)
            text2 = 'SET Today :' + '\n' + sett +' > '+ st[0] +' ('+st[1]+') ' + '\n' + 'Status : Hold' + '\n' + 'X : {} / {}'.format(targetDown_01,targetDown_02)
            
            text = 'SET'
            text2 = 'Long' 
            text3 = 'Short' 
            set_now = st[0] 
            Percent = ' (' + st[1] + ')'
            target_Up = 'X : {} / {}'.format(targetUp_01,targetUp_02)
            target_Down = 'X : {} / {}'.format(targetDown_01,targetDown_02)

            float(st[0])

            if float(st[0]) >= float(sett): 
                word_to_reply = text2
                comment = target_Up          
            else:
                word_to_reply = text3
                comment = target_Down         

            print(word_to_reply, comment)
            bubbles = []
            bubble = flex_set(text,set_now,Percent,word_to_reply,sett,comment)
            
            flex_to_reply = SetMessage_Object(bubble)
            reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
            return 'OK'

        dailyset()
    
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

        text_request = '{} {} ({})'.format(r[0], r[1], r[2])

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

                dfW = data.DataReader(f'{list}', data_source="yahoo", start='2020-03-09', end=end)
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

                text1 = exit1 + ' | ' + exit2 + ' | ' + exit3 
                text2 = '----'

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
                change = ' (' + r[2] + ')'

                if float(value) > 7500000:
                    if barY > 3.00:
                        if barQ > 6.00:
                            notice = alert1
                            stop = stopQ
                            open = OpenQ
                            buy = buyQ
                            target = text1
                            avg = barQ
                        elif barQ >= 3.00:
                            if barW >= 0:
                                notice = alert2
                                stop = stopQ
                                open = OpenQ
                                buy = buyQ
                                target = text1
                                avg = barQ
                            else:
                                notice = alert7
                                stop = stopQ
                                open = OpenQ
                                buy = buyQ
                                target = text1
                                avg = barQ
                        elif barQ >= 0.00:
                            if barW >= 0:
                                notice = alert3
                                stop = stopQ
                                open = OpenQ
                                buy = buyQ
                                target = text1
                                avg = barQ
                            else:
                                notice = alert7
                                stop = stopQ
                                open = OpenQ
                                buy = buyQ
                                target = text1
                                avg = barQ
                        else:
                            notice = alert4
                            stop = stopQ
                            open = OpenQ
                            buy = buyQ
                            target = text2
                            avg = barQ
                    elif barY >= 0.00:
                        if barQ >= 0:
                            if barW > 0:
                                notice = alert6
                                stop = stopY
                                open = OpenY
                                buy = buyY
                                target = text1
                                avg = barY
                            else:
                                notice = alert7
                                stop = stopY
                                open = OpenY
                                buy = buyY
                                target = text1
                                avg = barY
                        else:
                            notice = alert5
                            stop = stopY
                            open = OpenY
                            buy = buyY
                            target = text2
                            avg = barY
                    else:
                        if barQ > 6.00:
                            notice = alert1
                            stop = stopQ
                            open = OpenQ
                            buy = buyQ
                            target = text1
                            avg = barQ
                        elif barQ >= 3.00:
                            if barW >= 0:
                                notice = alert2
                                stop = stopQ
                                open = OpenQ
                                buy = buyQ
                                target = text1
                                avg = barQ
                            else:
                                notice = alert8
                                stop = stopQ
                                open = OpenQ
                                buy = buyQ
                                target = text1
                                avg = barQ
                        elif barQ >= 0.00:
                            if barW >= 0:
                                notice = alert3
                                stop = stopQ
                                open = OpenQ
                                buy = buyQ
                                target = text1
                                avg = barQ
                            else:
                                notice = alert8
                                stop = stopQ
                                open = OpenQ
                                buy = buyQ
                                target = text1
                                avg = barQ
                        else:
                            notice = alert4
                            stop = stopQ
                            open = OpenQ
                            buy = buyQ
                            target = text2
                            avg = barQ
                else:
                    notice = alert9
                    stop = stopQ
                    open = OpenQ
                    buy = buyQ
                    target = text2
                    avg = barQ

                word_to_reply = str('{} {}'.format(text,notice))
                print(word_to_reply)
                bubble = flex_stock(text,price_now,notice,change,open,buy,stop,avg,target)
                
                flex_to_reply = SetMessage_Object(bubble)
                reply_msg(reply_token,data=flex_to_reply,bot_access_key=channel_access_token)
                return 'OK'
                
        for symbol in symbols:
            stock(symbol).ticket()

    # except:
    #     text_list = [
    #         '{} ไม่มีในฐานข้อมูล {} ลองใหม่อีกครั้ง'.format(text_from_user,disname),
    #         '{} ค้นหาหุ้น {} ไม่ถูกต้อง ลองใหม่อีกครั้ง'.format(disname, text_from_user),

    #     ]

    #     from random import choice
    #     word_to_reply = choice(text_list)
        
    #     text_to_reply = TextSendMessage(text = word_to_reply)

    #     line_bot_api.reply_message(
    #             event.reply_token,
    #             messages=[text_to_reply]
    #         )

@handler.add(FollowEvent)
def RegisRichmenu(event):
    userid = event.source.user_id
    disname = line_bot_api.get_profile(user_id=userid).display_name
    line_bot_api.link_rich_menu_to_user(userid,'richmenu-5678ea83f640c401eedb8986848a53a8')

    button_1 = QuickReplyButton(action=MessageAction(lable='IQXUSTB',text='IQXUSTB'))
    button_2 = QuickReplyButton(action=MessageAction(lable='IQXGL',text='IQXGL'))
    button_3 = QuickReplyButton(action=MessageAction(lable='IQXWTI',text='IQXWTI'))
    button_4 = QuickReplyButton(action=MessageAction(lable='SET',text='SET'))
    button_5 = QuickReplyButton(action=MessageAction(lable='TFEX',text='TFEX'))

    answer_button = QuickReply(items=[button_1,button_2,button_3,button_4,button_5])
            
if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Credentials.json"
    os.environ["DIALOGFLOW_PROJECT_ID"] = "worldstock-iardyn"
    port = int(os.getenv('PORT', 2000))
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)