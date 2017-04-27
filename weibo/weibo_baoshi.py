#!/usr/bin/env python
# encoding: utf-8
import random
import sys
import datetime
import re
import os
import time
reload(sys)
sys.setdefaultencoding('utf-8')
from weibo import Client

import numpy as np

import RPi.GPIO as GPIO
import dht11

from picamera import PiCamera

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 4
t_h_detector = dht11.DHT11(pin = 4)
t_h = t_h_detector.read()

#take a photo
#camera = picamera.PiCamera()
#camera.capture('/home/pi/weibo/imgs/image.jpg')

#weibo
APP_KEY = '888061270'  # app key
APP_SECRET = '*******'  # app secret
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'  # callback url
AUTH_URL = 'https://api.weibo.com/oauth2/authorize'
USERID = '15872364200'  # userid
PASSWD = '*******'  # password

dicts={
    0:u'午夜幽灵在此报时',
    1:u'不早了，得睡觉了',
    2:u'午夜时分，幽灵活动时间，请勿打扰',
    3:u'月色不错',
    4:u'哎，又失眠了TT',
    5:u'醒了，睡不着了。',
    6:u'Good morning',
    7:u'早饭准备吃啥',
    8:u'がんばって',
    9:u'不说了，去工作',
    10:u'休息一下',
    11:u'想一想，中午吃什么呢',
    12:u'Good day',
    #13:,14:,15:,16:,17:,
    18:u'Good afternoon',
    19:u'一切正常',
    #20:,21:,
    22:u'Good night',
    23:u'起来上厕所啦'
}

client = Client(APP_KEY, APP_SECRET, CALLBACK_URL, username=USERID, password=PASSWD)

def post_new1(content, pic, location):
    print client.post('statuses/upload', status=content, pic=pic, lat=location[0], long=location[1])

def post_new0(content):
    print client.post('statuses/update', status=content)

#f = open('F:/max_id.txt','r')
#max_id=int(f.read())
#f.close()
#os.remove('F:/max_id.txt')
#

def post_comments(max_id):
    friends_timeline_ids = client.get('statuses/friends_timeline/ids', feature = 1,since_id = max_id)
    ids_list = np.array(friends_timeline_ids[u'statuses'])
    ids_int64 = ids_list.astype(np.int64)
    for i in ids_int64:
    	content = rand_content()
        client.post('comments/create',comment = content , id = i)#,attitude='simle')
        #time.sleep(1)
    last_id = ids_int64[-1]
    return last_id

def rand_content():
    contents=[u'66666666',u'可以的',u'可以哟',u'不错哟',u'可以可以',u'不错不错',u'9999999',\
    u'[微笑][微笑]',u'棒棒哒',u'么么哒']
    randn = random.randint(0,9)
    return contents[randn]


def get_today():
    """
    gen a string like '20150520'
    """
    return time.strftime('%Y%m%d', time.localtime())


def gen_location():
    # -90 - +90
    # -180 - +180
    #return random.randint(-90,90),random.randint(-180,180)
    return 30.52+random.random()/10,114.35+random.random()/10

base = '/home/pi/weibo/imgs/'
def get_img_path():
    for x in os.listdir(base):
        return base + x


def post_hour_part():
    now_time = unicode(datetime.datetime.now())[:16]
    hour = map(int, re.findall(u'\\d+', now_time))[3]
#    if dicts.has_key(hour):
#        gen_content = dicts[hour]
#        status = u'现在是' + now_time + u'，' + gen_content
#        img_path = get_img_path()
#        post_new1(status, open(img_path, 'rb'), gen_location())
#        os.remove(img_path)
#    else:
#        status = u'现在是' + now_time + u'，安心工作'
#        post_new0(status)
    
    camera = PiCamera()
    camera.annotate_text_size = 80
    camera.resolution = (2592, 1944)
    camera.framerate = 15
    camera.meter_mode = 'matrix'
    camera.start_preview()
    camera.annotate_text = now_time
    time.sleep(2)
    camera.capture('/home/pi/weibo/imgs/image.jpg')

    img_path = get_img_path()
    status=u'现在是'+now_time+u'#吊兰养成日记#温度：'+unicode(t_h.temperature)+u'℃  湿度：'+unicode(t_h.humidity)+u'%'
    post_new1(status,open(img_path,'rb'),gen_location())
    os.remove(img_path)

if __name__ == '__main__': 
    post_hour_part()
    #t = str(post_comments(max_id))
    #with open('F:/max_id.txt','w') as f:
    #    f.write(t)

#limits = client.get('account/rate_limit_status')
