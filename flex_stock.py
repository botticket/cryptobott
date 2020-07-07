
def flex_usdcheck(text,price_now,change,chgp,notice,start,buy,stop,target):
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
                    "url": "https://kasikornresearch.com/SiteCollectionDocuments/analysis/business/money/HardBaht_Banner.jpg",
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
                        "text": "({})".format(chgp),
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

def flex_goldcheck(text,price_now,change,chgp,notice,start,buy,stop,target):
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
                    "url": "https://a.c-dn.net/b/1OiQ5h/headline_GOLD_14.JPG",
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
                        "text": "({})".format(chgp),
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

def flex_wticheck(text,price_now,change,chgp,notice,start,buy,stop,target):
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
                    "url": "https://static.posttoday.com/media/content/2014/06/19/09FD4903F4224438B6C49E1817EBE7BF.jpg",
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
                        "text": "({})".format(chgp),
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

def flex_tfexcheck(text,price_now,change,chgp,notice,start,buy,stop,target):
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
                    "url": "https://akm-img-a-in.tosshub.com/sites/btmt/images/stories/shares_1280_20180404115810324_660x450_020120061652.jpg",
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
                        "text": "({})".format(chgp),
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

def flex_setcheck(text,price_now,change,chgp,notice,start,buy,stop,target):
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
                    "url": "https://d1sr9z1pdl3mb7.cloudfront.net/wp-content/uploads/2018/03/09172121/stock-market.jpg",
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
                        "text": "({})".format(chgp),
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

def flex_stock(text,price_now,change,chgp,notice,start,buy,stop,target,avg):
    Change_color = ['#EE0000' if '-' in str(change) else '#23D500'][0]
    trend = ['#EE0000' if '-' in str(avg) else '#3c3c3c'][0]
    switch = ['แนวรับ' if '-' in str(avg) else 'แนวต้าน'][0]
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
                    "url": "https://www.knowtechbetter.com/wp-content/uploads/2018/05/Software-for-Stock-Buying-and-selling.jpg",
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
                        "text": "({})".format(chgp),
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
                    "text": "สถานะ",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "32%",
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
                "offsetTop": "37%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "ราคาซื้อ",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "45%",
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
                "offsetTop": "50%",
                "offsetStart": "5%",
                "width": "100%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "แนวรับ",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "57%",
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
                "offsetTop": "62%",
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
                "offsetTop": "69%",
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
                "offsetTop": "74%",
                "offsetStart": "5%",
                "width": "95%"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "ตอบแทนเฉลี่ย",
                    "flex": 3,
                    "size": "sm"
                }
                ],
                "position": "absolute",
                "offsetTop": "80%",
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
                "offsetTop": "85%",
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