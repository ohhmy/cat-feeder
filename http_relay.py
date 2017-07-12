#!/usr/bin/env python2

import relay
import requests
import time
import RPi.GPIO as GPIO
import dht11
import infrared

class HTTP_RELAY():
	def __init__(self):
		self.dht = dht11.DHT11()
		self.get_paras = 'http://ec2-54-222-242-143.cn-north-1.compute.amazonaws.com.cn:10000/statusData?paras=DEV1%2CDEV2%2CDEV3%2CMODE'
		self.post_dst = 'http://ec2-54-222-242-143.cn-north-1.compute.amazonaws.com.cn:10000/statusData/%s/%s/%d'
		self.para_list = [0,0,0,0,0]
		self.dev_sst = [0,0,0,0]
		self.dev_dst = [0,0,0,0]
		self.para_name = ['DEV1','DEV2','DEV3','DEV4']
		rdst = requests.get(self.get_paras)
		for i,j in zip(self.para_name[:3],[0,1,2]):
			self.dev_dst[j]=rdst.json()['data'][i]['deviceStatus']

	def get_paras(self):
		rget = requests.get(self.get_paras)
		for i,j in zip(self.para_name,[0,1,2,4]):
			self.dev_dst = rget.json()['data'][i]['deviceStatus']
			self.para_list[j] = rget.json()['data'][i]['switchStatus']

	def mannual_mode(self):
		self.get_paras()
		for i,j in zip(self.para_name[:3],[0,1,2]):
			if(self.para_list[j]!=self.dev_sst[j]):
				self.dev_sst[j] = self.para_list[j]
				relay.control(self.dev_sst)
				self.dev_dst[j] = 1-self.dev_dst[j]
				requests.post(self.post_dst%i%'D'%dev_dst[j])

	def auto_mode(self):
		if(infrared.light = 1):
			requests.post(self.post_dst%'DEV3'%'D'%1)
			requests.post(self.post_dst%'DEV3'%'S'%1)
		else:
			requests.post(self.post_dst%'DEV3'%'D'%0)
			requests.post(self.post_dst%'DEV3'%'S'%0)

	def http_relay():
		while(True):
			self.get_paras()
			if(self.para_list[4]==1):
				self.auto_mode()
			else:
				self.mannual_mode()

			time.sleep(1)