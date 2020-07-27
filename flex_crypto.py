def flex_crypto(text,price_now,change,chgp,notice,start,buy,stop,target):
    Change_color = ['#EE0000' if '-' in str(change) else '#23D500'][0]
    bubble ={
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "bubble",
        "size": "kilo",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "filler"
                }
                ],
                "flex": 1,
                "backgroundColor": "#3c3c3c",
                "height": "32%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "filler"
                }
                ],
                "flex": 2,
                "height": "75%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://mystickermania.com/scale/resize/256/256?format=png&quality=80&crop=true&progressive=true&url=/cdn/stickers/star-wars/previews.png",
                    "aspectMode": "cover"
                }
                ],
                "borderWidth": "3px",
                "borderColor": "#FFFFFF",
                "cornerRadius": "55px",
                "position": "absolute",
                "offsetTop": "3%",
                "offsetStart": "3%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(text),
                        "weight": "bold",
                        "color": "#F8F9F9",
                        "wrap": True,
                        "size": "lg",
                        "align": "end"
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(price_now),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "lg"
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(change),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "md",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "({}%)".format(chgp),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "md",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                }
                ],
                "width": "100%",
                "position": "absolute",
                "flex": 3
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "35%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(notice),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "40%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Open Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "47%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{} ~ {}".format(start,buy),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "52%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Close Position",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "59%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(stop),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "64%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Target",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "71%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(target),
                    "flex": 3,
                    "size": "lg",
                    "wrap": True
                }
                ],
                "position": "absolute",
                "offsetTop": "76%",
                "offsetStart": "5%",
                "width": "95%"
            }
            ],
            "height": "400px",
            "paddingAll": "0px"
            }
        }
    }
    return bubble

def flex_stock(text,price_now,change,chgp,notice,start,stop,target,avg):
    Change_color = ['#EE0000' if '-' in str(change) else '#23D500'][0]
    trend = ['#EE0000' if '-' in str(avg) else '#3c3c3c'][0]
    switch = ['Quarter' if '-' in str(avg) else 'Quarter'][0]
    chgword = ['Year' if '-' in str(avg) else 'Year'][0]
    bubble ={
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "bubble",
        "size": "kilo",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "filler"
                }
                ],
                "flex": 1,
                "backgroundColor": "#3c3c3c",
                "height": "30%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "filler"
                }
                ],
                "flex": 2,
                "height": "75%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://mystickermania.com/scale/resize/256/256?format=png&quality=80&crop=true&progressive=true&url=/cdn/stickers/star-wars/previews.png",
                    "aspectMode": "cover"
                }
                ],
                "borderWidth": "3px",
                "borderColor": "#FFFFFF",
                "cornerRadius": "55px",
                "position": "absolute",
                "offsetTop": "3%",
                "offsetStart": "3%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(text),
                        "weight": "bold",
                        "color": "#F8F9F9",
                        "wrap": True,
                        "size": "lg",
                        "align": "end"
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(price_now),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "lg",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "{}".format(change),
                        "align": "end",
                        "color": "{}".format(Change_color),
                        "gravity": "center",
                        "size": "md",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "= {} %".format(chgp),
                        "align": "end",
                        "color": "#F8F9F9",
                        "gravity": "center",
                        "size": "md",
                        "wrap": True
                    }
                    ],
                    "paddingStart": "150px",
                    "paddingTop": "5px",
                    "offsetEnd": "5%"
                }
                ],
                "width": "100%",
                "position": "absolute",
                "flex": 3
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Alert",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "31%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(notice),
                    "flex": 3,
                    "color": "{}".format(trend),
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "35%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Buy",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "42%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{} + 2 ช่อง".format(start),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "47%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(chgword),
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "54%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(stop),
                    "flex": 3,
                    "size": "lg"
                }
                ],
                "position": "absolute",
                "offsetTop": "59%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(switch),
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "66%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(target),
                    "flex": 3,
                    "color": "{}".format(trend),
                    "size": "lg",
                    "wrap": True
                }
                ],
                "position": "absolute",
                "offsetTop": "71%",
                "offsetStart": "5%",
                "width": "95%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Graph",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "77%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "{}".format(avg),
                    "flex": 3,
                    "color": "{}".format(trend),
                    "size": "lg",
                    "wrap": True
                }
                ],
                "position": "absolute",
                "offsetTop": "81%",
                "offsetStart": "5%",
                "width": "95%"
            }
            ],
            "height": "400px",
            "paddingAll": "0px"
            }
        }
    }
    return bubble