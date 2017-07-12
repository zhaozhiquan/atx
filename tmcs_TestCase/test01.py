#!/usr/bin/env python
# coding=utf-8
import os
import unittest
import atx
from time import sleep, strftime
import HTMLTestRunner
import public.methods as public
import configure

class UCSDK(unittest.TestCase,public.Methods):
	u'''UC-sdk测试'''
	def setUp(self):
		pass
		# if configure.device_name == '':
		# 	self.driver = atx.connect()
		# elif configure.device_name != '':
		# 	self.driver = atx.connect(configure.device_name)
	def tearDown(self):
		#self.driver.adb_shell(['am force-stop com.zhankaigame.destiny.uc'])
		pass

	def test_100(self):
		u'''检查icon'''
		self.driver.keyevent('KEYCODE_HOME')
		size = self.size()
		for i in range(5):
			icon = self.images_or_none(self.driver,'game-ysdk-icon@auto.png')
			if icon == None:
				self.driver.swipe(size[0]*0.8,size[1]/2,size[0]*0.2,size[1]/2,steps = 10)
				sleep(2)
			else:
				break
		self.dy_IsNotNone(self.driver,icon,'test_100')
	'''def test_101(self):
		#检查闪屏
		self.driver.start_app(configure.package_name, configure.activity_name)
		self.driver.wait('./'+configure.game_name+'_images/'+'game-uc-splash@auto.png')
		splash_screen = self.images_or_none(self.driver,'game-uc-splash@auto.png')
		self.dy_IsNotNone(self.driver, splash_screen, 'test_101')'''
	def test111(self):

		with open("/Users/zhaozhiquan/Downloads/online.txt",'rb') as f:
			f_read = f.read()
			f_read_decode = f_read.decode('UTF-16')
			print f_read_decode