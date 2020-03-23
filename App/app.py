import os
from flask import Flask, render_template


import datetime
import json
import requests
import argparse
import logging
from bs4 import BeautifulSoup
# from tabulate import tabulate
import time
import tweepy
from configs import *

app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')

FORMAT = '[%(asctime)-15s] %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG, filename='bot.log', filemode='a')

S_HEADERS=['Total Cases ','New Cases  ','Deaths       ','New Deaths ','Recovered ','Active Cases','Critical','Cases/Million']
FILE_NAME = 'corona_india_data.json'

HEADERS = {'Content-type': 'application/json'}

URL1= 'https://www.worldometers.info/coronavirus/'

extract_contents = lambda row: [x.text.replace('\n', '') for x in row]

def slacker(webhook_url=DEFAULT_SLACK_WEBHOOK):
    def slackit(msg):
        #logging.info('Sending {msg} to slack'.format(msg=msg))
        payload = { 'text': msg }
        return requests.post(webhook_url, headers=HEADERS, data=json.dumps(payload))
    return slackit

def tweet(twt):
    auth =tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth)
    api.update_status(status = twt)

def magic():
    current_time = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

    print(current_time)
    # try:
    response = requests.get(URL1).content
    soup = BeautifulSoup(response, 'html.parser')
    header=extract_contents(soup.tr.find_all('th'))
    data1=soup.find_all("tr",{"total_row"})
    for row in data1:
        s = extract_contents(row.find_all('td'))

    stats=s[1:]
    print(stats)

    res=''
    for i in range(5):
        res=res+'\n'+S_HEADERS[i]+' '+stats[i]
    print(res)

    # sres='\n𝗧𝗼𝘁𝗮𝗹 𝗖𝗮𝘀𝗲𝘀:  '+stats[0]+'\n𝗡𝗲𝘄 𝗖𝗮𝘀𝗲𝘀:   '+stats[1]+'\n𝗗𝗲𝗮𝘁𝗵𝘀:        '+stats[2]+'\n𝗡𝗲𝘄 𝗗𝗲𝗮𝘁𝗵𝘀:  '+stats[3]+'\n𝗥𝗲𝗰𝗼𝘃𝗲𝗿𝗲𝗱:   '+stats[4]
    #sres='\n 𝗧𝗼𝘁𝗮𝗹 𝗖𝗮𝘀𝗲𝘀 '+stats[0]+'\n 𝗡𝗲𝘄 𝗖𝗮𝘀𝗲𝘀:'+stats[1]+'\n 𝗗𝗲𝗮𝘁𝗵𝘀:'+stats[2]+'\n 𝗡𝗲𝘄 𝗗𝗲𝗮𝘁𝗵𝘀:'+stats[3]+'\n 𝗥𝗲𝗰𝗼𝘃𝗲𝗿𝗲𝗱:'+stats[4]
    
    #slack_text=f'𝗖𝗼𝗿𝗼𝗻𝗮𝘃𝗶𝗿𝘂𝘀 𝘄𝗼𝗿𝗹𝗱𝘄𝗶𝗱𝗲 𝗹𝗶𝘃𝗲 𝘀𝘁𝗮𝘁𝗶𝘀𝘁𝗶𝗰𝘀 🌎{sres}\n #coronavirus #covid19 #Hope @who\n{current_time}'
    twt=u'𝗖𝗼𝗿𝗼𝗻𝗮𝘃𝗶𝗿𝘂𝘀 𝘄𝗼𝗿𝗹𝗱𝘄𝗶𝗱𝗲 𝗹𝗶𝘃𝗲 𝘀𝘁𝗮𝘁𝗶𝘀𝘁𝗶𝗰𝘀 🌎'+res+'\n #coronavirus #covid19 #Hope @who\n'+current_time
    #slack_text='𝗖𝗼𝗿𝗼𝗻𝗮𝘃𝗶𝗿𝘂𝘀 𝘄𝗼𝗿𝗹𝗱𝘄𝗶𝗱𝗲 𝗹𝗶𝘃𝗲 𝘀𝘁𝗮𝘁𝗶𝘀𝘁𝗶𝗰𝘀 🌎'+res+'\n #coronavirus #covid19 #Hope @who\n'+current_time
    print("works till here")
    tweet(twt)
    print("tweeted")
# def connect_db():
#     return psycopg2.connect(os.environ.get('DATABASE_URL'))


# @app.before_request
# def before_request():
#     g.db_conn = connect_db()

@app.route('/dev')
def dev():
    while(True):
        print("Devuu Rockss")
        magic()
        time.sleep(1200)
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')
