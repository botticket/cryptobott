def flex_THB(text,usthbspot,Percent,word_to_reply,IQXUSTHB,comment):
  Change_color = ['#EE0000' if '-' in str(Percent) else '#23D500'][0]
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "bubble",
        "size": "giga",
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
              "backgroundColor": "#3c3c3c"
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "filler"
                }
              ],
              "flex": 2
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "image",
                  "url": "https://s.isanook.com/mn/0/rp/r/w728/ya0xa0m1w0/aHR0cHM6Ly9zLmlzYW5vb2suY29tL21uLzAvdWQvMzUvMTc4NjU4L2NvaW4uanBn.jpg",
                  "aspectMode": "cover"
                }
              ],
              "borderWidth": "3px",
              "borderColor": "#FFFFFF",
              "cornerRadius": "55px",
              "position": "absolute",
              "offsetTop": "5%",
              "offsetStart": "5px"
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
                      "align": "start",
                      "color": "{}".format(Change_color),
                      "wrap": True,
                      "size": "xl",
                      "gravity": "center"
                    }
                  ],
                  "paddingStart": "35%",
                  "paddingTop": "1%",
                  "width": "150%"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "{} {}".format(usthbspot,Percent),
                      "weight": "bold",
                      "align": "start",
                      "color": "{}".format(Change_color),
                      "wrap": True,
                      "size": "xl",
                      "gravity": "center"
                    }
                  ],
                  "paddingStart": "35%",
                  "paddingTop": "1%",
                  "width": "150%"
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
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "{}".format(word_to_reply),
                      "weight": "bold",
                      "align": "start",
                      "color": "#959595",
                      "size": "lg"
                    },
                    {
                      "type": "text",
                      "text": "{}".format(IQXUSTHB),
                      "weight": "regular",
                      "align": "start",
                      "color": "#000000",
                      "size": "lg",
                      "wrap": True
                    }
                  ],
                  "spacing": "md"
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "Target",
                      "weight": "bold",
                      "align": "start",
                      "color": "#959595",
                      "size": "lg"
                    },
                    {
                      "type": "text",
                      "text": "{}".format(comment),
                      "weight": "regular",
                      "align": "start",
                      "color": "#000000",
                      "size": "lg",
                      "wrap": True
                    }
                  ],
                  "spacing": "sm"
                }
              ],
              "flex": 3,
              "position": "absolute",
              "width": "100%",
              "paddingTop": "35%",
              "paddingStart": "5%"
            }
          ],
          "height": "270px",
          "paddingAll": "0px"
        }
      }
  }
  return bubble

def flex_WTI(text,wtispot,Percent,word_to_reply,IQXWTI,comment):
  Change_color = ['#EE0000' if '-' in str(Percent) else '#23D500'][0]
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "bubble",
        "size": "giga",
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
              "backgroundColor": "#3c3c3c"
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "filler"
                }
              ],
              "flex": 2
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
              "offsetTop": "5%",
              "offsetStart": "5px"
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
                      "align": "start",
                      "color": "{}".format(Change_color),
                      "wrap": True,
                      "size": "xl",
                      "gravity": "center"
                    }
                  ],
                  "paddingStart": "35%",
                  "paddingTop": "1%",
                  "width": "150%"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "{} {}".format(wtispot,Percent),
                      "weight": "bold",
                      "align": "start",
                      "color": "{}".format(Change_color),
                      "wrap": True,
                      "size": "xl",
                      "gravity": "center"
                    }
                  ],
                  "paddingStart": "35%",
                  "paddingTop": "1%",
                  "width": "150%"
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
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "{}".format(word_to_reply),
                      "weight": "bold",
                      "align": "start",
                      "color": "#959595",
                      "size": "lg"
                    },
                    {
                      "type": "text",
                      "text": "{}".format(IQXWTI),
                      "weight": "regular",
                      "align": "start",
                      "color": "#000000",
                      "size": "lg",
                      "wrap": True
                    }
                  ],
                  "spacing": "md"
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "Target",
                      "weight": "bold",
                      "align": "start",
                      "color": "#959595",
                      "size": "lg"
                    },
                    {
                      "type": "text",
                      "text": "{}".format(comment),
                      "weight": "regular",
                      "align": "start",
                      "color": "#000000",
                      "size": "lg",
                      "wrap": True
                    }
                  ],
                  "spacing": "sm"
                }
              ],
              "flex": 3,
              "position": "absolute",
              "width": "100%",
              "paddingTop": "35%",
              "paddingStart": "5%"
            }
          ],
          "height": "270px",
          "paddingAll": "0px"
        }
      }
  }
  return bubble

def flex_gold(text,gspot,Percent,word_to_reply,IQXGL,comment):
  Change_color = ['#EE0000' if '-' in str(Percent) else '#23D500'][0]
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "bubble",
        "size": "giga",
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
              "backgroundColor": "#3c3c3c"
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "filler"
                }
              ],
              "flex": 2
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "image",
                  "url": "https://www.thehindubusinessline.com/economy/agri-business/z0ldjz/article26390048.ece/alternates/LANDSCAPE_435/BL28COMMGOLD1",
                  "aspectMode": "cover"
                }
              ],
              "borderWidth": "3px",
              "borderColor": "#FFFFFF",
              "cornerRadius": "55px",
              "position": "absolute",
              "offsetTop": "5%",
              "offsetStart": "5px"
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
                      "align": "start",
                      "color": "{}".format(Change_color),
                      "wrap": True,
                      "size": "xl",
                      "gravity": "center"
                    }
                  ],
                  "paddingStart": "35%",
                  "paddingTop": "1%",
                  "width": "150%"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "{} {}".format(gspot,Percent),
                      "weight": "bold",
                      "align": "start",
                      "color": "{}".format(Change_color),
                      "wrap": True,
                      "size": "xl",
                      "gravity": "center"
                    }
                  ],
                  "paddingStart": "35%",
                  "paddingTop": "1%",
                  "width": "150%"
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
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "{}".format(word_to_reply),
                      "weight": "bold",
                      "align": "start",
                      "color": "#959595",
                      "size": "lg"
                    },
                    {
                      "type": "text",
                      "text": "{}".format(IQXGL),
                      "weight": "regular",
                      "align": "start",
                      "color": "#000000",
                      "size": "lg",
                      "wrap": True
                    }
                  ],
                  "spacing": "md"
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "Target",
                      "weight": "bold",
                      "align": "start",
                      "color": "#959595",
                      "size": "lg"
                    },
                    {
                      "type": "text",
                      "text": "{}".format(comment),
                      "weight": "regular",
                      "align": "start",
                      "color": "#000000",
                      "size": "lg",
                      "wrap": True
                    }
                  ],
                  "spacing": "sm"
                }
              ],
              "flex": 3,
              "position": "absolute",
              "width": "100%",
              "paddingTop": "35%",
              "paddingStart": "5%"
            }
          ],
          "height": "270px",
          "paddingAll": "0px"
        }
      }
  }
  return bubble

def flex_tfex(text,tfex_now,Percent,word_to_reply,tfexx,comment):
  Change_color = ['#EE0000' if '-' in str(Percent) else '#23D500'][0]
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "bubble",
        "size": "giga",
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
              "backgroundColor": "#3c3c3c"
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "filler"
                }
              ],
              "flex": 2
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
              "offsetTop": "5%",
              "offsetStart": "5px"
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
                      "align": "start",
                      "color": "{}".format(Change_color),
                      "wrap": True,
                      "size": "xl",
                      "gravity": "center"
                    }
                  ],
                  "paddingStart": "35%",
                  "paddingTop": "1%",
                  "width": "150%"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "{} {}".format(tfex_now,Percent),
                      "weight": "bold",
                      "align": "start",
                      "color": "{}".format(Change_color),
                      "wrap": True,
                      "size": "xl",
                      "gravity": "center"
                    }
                  ],
                  "paddingStart": "35%",
                  "paddingTop": "1%",
                  "width": "150%"
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
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "{}".format(word_to_reply),
                      "weight": "bold",
                      "align": "start",
                      "color": "#959595",
                      "size": "lg"
                    },
                    {
                      "type": "text",
                      "text": "{}".format(tfexx),
                      "weight": "regular",
                      "align": "start",
                      "color": "#000000",
                      "size": "lg",
                      "wrap": True
                    }
                  ],
                  "spacing": "md"
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "Target",
                      "weight": "bold",
                      "align": "start",
                      "color": "#959595",
                      "size": "lg"
                    },
                    {
                      "type": "text",
                      "text": "{}".format(comment),
                      "weight": "regular",
                      "align": "start",
                      "color": "#000000",
                      "size": "lg",
                      "wrap": True
                    }
                  ],
                  "spacing": "sm"
                }
              ],
              "flex": 3,
              "position": "absolute",
              "width": "100%",
              "paddingTop": "35%",
              "paddingStart": "5%"
            }
          ],
          "height": "270px",
          "paddingAll": "0px"
        }
      }
  }
  return bubble

def flex_set(text,set_now,Percent,word_to_reply,sett,comment):
  Change_color = ['#EE0000' if '-' in str(Percent) else '#23D500'][0]
  bubble = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "bubble",
        "size": "giga",
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
              "backgroundColor": "#3c3c3c"
            },
            {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "filler"
                }
              ],
              "flex": 2
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
              "offsetTop": "5%",
              "offsetStart": "5px"
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
                      "align": "start",
                      "color": "{}".format(Change_color),
                      "wrap": True,
                      "size": "xl",
                      "gravity": "center"
                    }
                  ],
                  "paddingStart": "35%",
                  "paddingTop": "1%",
                  "width": "150%"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "{} {}".format(set_now,Percent),
                      "weight": "bold",
                      "align": "start",
                      "color": "{}".format(Change_color),
                      "wrap": True,
                      "size": "xl",
                      "gravity": "center"
                    }
                  ],
                  "paddingStart": "35%",
                  "paddingTop": "1%",
                  "width": "150%"
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
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "{}".format(word_to_reply),
                      "weight": "bold",
                      "align": "start",
                      "color": "#959595",
                      "size": "lg"
                    },
                    {
                      "type": "text",
                      "text": "{}".format(sett),
                      "weight": "regular",
                      "align": "start",
                      "color": "#000000",
                      "size": "lg",
                      "wrap": True
                    }
                  ],
                  "spacing": "md"
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": "Target",
                      "weight": "bold",
                      "align": "start",
                      "color": "#959595",
                      "size": "lg"
                    },
                    {
                      "type": "text",
                      "text": "{}".format(comment),
                      "weight": "regular",
                      "align": "start",
                      "color": "#000000",
                      "size": "lg",
                      "wrap": True
                    }
                  ],
                  "spacing": "sm"
                }
              ],
              "flex": 3,
              "position": "absolute",
              "width": "100%",
              "paddingTop": "35%",
              "paddingStart": "5%"
            }
          ],
          "height": "270px",
          "paddingAll": "0px"
        }
      }
  }
  return bubble

def flex_stock(text,price_now,notice,change,open,buy,stop,avg,target):
  Change_color = ['#EE0000' if '-' in str(change) else '#23D500'][0]
  trend = ['#EE0000' if '-' in str(avg) else '#23D500'][0]
  bubble ={
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
      "type": "bubble",
      "size": "giga",
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
            "backgroundColor": "#3c3c3c"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "filler"
              }
            ],
            "flex": 2
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://media.brstatic.com/2017/03/20172321/stock-market-ticker-charts_573x300.jpg",
                "aspectMode": "cover",
                "size": "sm"
              }
            ],
            "borderWidth": "2px",
            "borderColor": "#FFFFFF",
            "cornerRadius": "55px",
            "position": "absolute",
            "offsetTop": "5%",
            "offsetStart": "5px"
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
                    "align": "start",
                    "color": "{}".format(Change_color),
                    "wrap": True,
                    "size": "xl",
                    "gravity": "center"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(price_now),
                    "align": "end",
                    "color": "{}".format(Change_color),
                    "gravity": "center",
                    "size": "md",
                    "offsetEnd": "10%"
                  }
                ],
                "paddingStart": "100px",
                "paddingTop": "1%"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(notice),
                    "weight": "regular",
                    "align": "start",
                    "color": "#F8F9F9",
                    "wrap": True,
                    "size": "md",
                    "gravity": "center"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(change),
                    "align": "end",
                    "color": "{}".format(Change_color),
                    "gravity": "center",
                    "size": "md",
                    "offsetEnd": "10%"
                  }
                ],
                "paddingStart": "100px",
                "paddingTop": "5px",
                "width": "100%"
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
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Buy",
                    "weight": "bold",
                    "align": "start",
                    "color": "#959595",
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "{} | {}".format(open,buy),
                    "weight": "regular",
                    "align": "start",
                    "color": "#000000",
                    "size": "lg",
                    "wrap": True
                  }
                ],
                "spacing": "xs"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Stop",
                    "weight": "bold",
                    "align": "start",
                    "color": "#959595",
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "{}".format(stop),
                    "weight": "regular",
                    "align": "start",
                    "color": "#000000",
                    "size": "lg",
                    "wrap": True,
                    "offsetBottom": "5%"
                  }
                ],
                "spacing": "md"
              }
            ],
            "flex": 3,
            "position": "absolute",
            "width": "50%",
            "paddingTop": "65%",
            "paddingStart": "8%"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Avg",
                    "weight": "bold",
                    "align": "start",
                    "color": "{}".format(trend),
                    "size": "sm"
                  },
                  {
                    "type": "text",
                    "text": "{}%".format(avg),
                    "weight": "regular",
                    "align": "start",
                    "color": "{}".format(trend),
                    "size": "lg",
                    "wrap": True
                  }
                ],
                "spacing": "xs"
              }
            ],
            "flex": 3,
            "position": "absolute",
            "width": "50%",
            "paddingTop": "65%",
            "paddingStart": "15%",
            "offsetEnd": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Target",
                "size": "sm",
                "color": "#959595",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": "{}".format(target),
                "size": "lg",
                "color": "#000000",
                "wrap": True
              }
            ],
            "offsetStart": "4%",
            "offsetBottom": "5%"
          }
        ],
        "height": "270px",
        "paddingAll": "0px"
      }
    }
  }
  return bubble