richdata ={
  "size": {
    "width": 2500,
    "height": 843
  },
  "selected": True,
  "name": "startup",
  "chatBarText": "startup",
  "areas": [
    {
      "bounds": {
        "x": 945,
        "y": 114,
        "width": 614,
        "height": 628
      },
      "action": {
        "type": "message",
        "text": "สวัสดี"
      }
    }
  ]
}

import json

import requests

channel_secret = 'afe7ec6bede0dde581d0a61b6447653b'
channel_access_token = 'hkU+OYWsepq11sc+uM6bAE/ECjFb8+NUiTvjfQI1WUrXzKiUZvHU5YAv+AEG4I6ZZuJPflQ/v5Gp2XH5m5TtLeUkPpX3JUjqTKFWahSOIqWheppXpKvFyE+olbJyAGvg9f8pciPntSGZnLbfyAIoyQdB04t89/1O/w1cDnyilFU='



def RegisRich(Rich_json,channel_access_token):

    url = 'https://api.line.me/v2/bot/richmenu'

    Rich_json = json.dumps(Rich_json)

    Authorization = 'Bearer {}'.format(channel_access_token)


    headers = {'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': Authorization}

    response = requests.post(url,headers = headers , data = Rich_json)

    print(str(response.json()['richMenuId']))

    return str(response.json()['richMenuId'])

def CreateRichMenu(ImageFilePath,Rich_json,channel_access_token):


    richId = RegisRich(Rich_json = Rich_json,channel_access_token = channel_access_token)

    url = ' https://api.line.me/v2/bot/richmenu/{}/content'.format(richId)

    Authorization = 'Bearer {}'.format(channel_access_token)

    headers = {'Content-Type': 'image/jpeg',
    'Authorization': Authorization}

    img = open(ImageFilePath,'rb').read()

    response = requests.post(url,headers = headers , data = img)

    print(response.json())

CreateRichMenu(ImageFilePath='Resource/richmenu.jpg',Rich_json=richdata,channel_access_token=channel_access_token)