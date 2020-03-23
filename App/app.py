import os
from flask import Flask, render_template


# import datetime
# import json
# import requests
# import argparse
# import logging
# from bs4 import BeautifulSoup
# # from tabulate import tabulate
# import time
# import tweepy
# from configs import *

a = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')

# FORMAT = '[%(asctime)-15s] %(message)s'
# logging.basicConfig(format=FORMAT, level=logging.DEBUG, filename='bot.log', filemode='a')

# S_HEADERS=['Total Cases ','New Cases  ','Deaths       ','New Deaths ','Recovered ','Active Cases','Critical','Cases/Million']
# FILE_NAME = 'corona_india_data.json'

# HEADERS = {'Content-type': 'application/json'}

# URL1= 'https://www.worldometers.info/coronavirus/'

# extract_contents = lambda row: [x.text.replace('\n', '') for x in row]

# def slacker(webhook_url=DEFAULT_SLACK_WEBHOOK):
#     def slackit(msg):
#         payload = { 'text': msg }
#         return requests.post(webhook_url, headers=HEADERS, data=json.dumps(payload))
#     return slackit

# def tweet(twt):
#     auth =tweepy.OAuthHandler(consumer_key, consumer_secret) 
#     auth.set_access_token(access_token, access_token_secret) 
#     api = tweepy.API(auth)
#     api.update_status(status = twt)

# def magic():
#     current_time = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

#     print(current_time)
#     response = requests.get(URL1).content
#     soup = BeautifulSoup(response, 'html.parser')
#     header=extract_contents(soup.tr.find_all('th'))
#     data1=soup.find_all("tr",{"total_row"})
#     for row in data1:
#         s = extract_contents(row.find_all('td'))

#     stats=s[1:]
#     print(stats)

#     res=''
#     for i in range(5):
#         res=res+'\n'+S_HEADERS[i]+' '+stats[i]
#     print(res)
#     twt=u'𝗖𝗼𝗿𝗼𝗻𝗮𝘃𝗶𝗿𝘂𝘀 𝘄𝗼𝗿𝗹𝗱𝘄𝗶𝗱𝗲 𝗹𝗶𝘃𝗲 𝘀𝘁𝗮𝘁𝗶𝘀𝘁𝗶𝗰𝘀 🌎'+res+'\n #coronavirus #covid19 #Hope @who\n'+current_time
#     print("works till here")
#     tweet(twt)
#     print("tweeted")

# @app.route('/dev')
# def dev():
#     while(True):
#         print("Devuu Rockss")
#         magic()
#         time.sleep(1200)
#     return render_template('index.html')

@a.route('/')
def index():
    return render_template('index.html')
