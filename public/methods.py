#!/usr/bin/env python
#coding=utf-8

from time import sleep, strftime
import os
import configure
class Methods(object):
	def size(self):
		if configure.device_name == '':
			size = 'adb shell wm size'
		else:
			size = 'adb -s %s shell wm size' % configure.device_name
		a =  os.popen(size)
		for i in a:
			pass
		size =i.split(': ')
		size = size[1].split('x')
		size= [int(size[0]),int(size[1])] #size[0] 为width size[1] 为high
		return size

	def screencap(self,driver,**kwargs):
		dict1 = kwargs
		self.name = dict1['name']
		day = strftime('%Y-%m-%d')
		path = 'result/' + day + '/screencap/'
		self.driver.screenshot(os.getcwd()+os.sep+path + self.name + '.png')

	def dy(self,driver,value1,value2,screen_name):
		self.driver = driver
		try:
			self.assertEqual(value1, value2)
		except:
			self.screencap(self.driver,name=screen_name)
			self.assertEqual(value1, value2)
	def dy_IsNone(self,driver,obj,screen_name):
		self.driver = driver
		try:
			self.assertIsNone(obj)
		except:
			self.screencap(self.driver,name=screen_name)
			self.assertIsNone(obj)
	def dy_IsNotNone(self,driver,obj,screen_name):
		self.driver = driver
		try:
			self.assertIsNotNone(obj)
		except:
			self.screencap(self.driver,name=screen_name)
			self.assertIsNotNone(obj)

	def tap(self,driver,value,dealy=None):
		#value 是一个元组
		self.driver = driver
		zuobiao = self.public(driver)
		value = (int(value[0]*zuobiao[0]),int(value[1]*zuobiao[1]))
		return self.driver.tap([value],dealy)

	def element(self, driver, methods, value):
		'''
		:param driver:驱动
		:param methods: 方式
		:param value: 值
		:return: 返回对象
		'''
		self.driver = driver
		if methods == 'text':
			return self.driver(text=value)
		elif methods == 'xpath':
			return self.driver(xpath=value)
		elif methods == 'resourceId':
			return self.driver(resourceId=value)
		elif methods == 'className':
			return self.driver(className = value)

	def element_or_none(self, driver, methods, value):
		'''
		:param driver:驱动
		:param methods:方式
		:param value:知
		:return:元素存在返回元素,不存在,返回None
		'''
		self.driver = driver
		try:
			element = self.element(self.driver, methods, value)
			if len(element) == 0:
				self.assertEqual(True, False)
		except:
			element = None
		return element

	def enter_game_new(self,driver):
		self.driver = driver

		self.click_images(self.driver, 'game-server-list@auto.png')
		print '进入游戏'
		sleep(30)
		try:
			self.wait_images(self.driver,'game-accelerated@auto.png')
			self.click_images(self.driver,'game-accelerated@auto.png')
		except:
			self.tap(self.driver, (0.912, 0.052))
		sleep(5)
		game_enter_bar = self.images_or_none(self.driver,'game-enter-bar@auto.png')
		if game_enter_bar == None:
			sleep(90)
			for i in xrange(10):
				self.tap(self.driver, (0.5, 0.7458))
				sleep(1)
			print '解锁新功能'
			sleep(3)
			for i in xrange(2):
				self.tap(self.driver, (0.5, 0.9307291666))
				sleep(1)
			print '天神'
			sleep(3)
			for i in xrange(2):
				self.tap(self.driver, (0.5, 0.4036))  # 解锁
				sleep(1)
			print '解锁'
			sleep(5)
			for i in xrange(2):
				self.tap(self.driver, (0.5, 0.5))  # 随便点
				sleep(1)
			print '随便点'
			for i in xrange(2):
				self.tap(self.driver, (0.1851, 0.7291))  # 天命
				sleep(1)
			print '天命'
			sleep(3)
			self.tap(self.driver, (0.5, 0.5))  # 随便点
			print '随便点'
			sleep(3)
			for i in xrange(2):
				self.tap(self.driver, (0.1851, 0.8291))  # 空白处
				sleep(1)
			print '空白处'
			sleep(3)
			for i in xrange(2):
				self.tap(self.driver, (0.1851, 0.9375))  # 返回
				sleep(1)
			print '返回'
			sleep(40)
			return None
		else:
			a = ''
			return a

	def enter_game(self,driver):
		self.driver = driver

		self.click_images(self.driver, 'game-server-list@auto.png')
		print '进入游戏'
		sleep(30)
		try:
			self.wait_images(self.driver,'game-accelerated@auto.png')
			self.click_images(self.driver,'game-accelerated@auto.png')
		except:
			self.tap(self.driver, (0.912, 0.052))

	def enter_bar(self,driver):
		self.driver = driver
		size = self.size()
		self.click_images(self.driver, 'game-enter-bar@auto.png')
		print '进入酒吧'
		sleep(5)
		self.driver.long_click(size[0]/2,size[1]*1/10)
		sleep(5)
		self.click_images(self.driver, 'game-bar-boss@auto.png')
		print '点击酒吧老板'
		sleep(15)
		for i in xrange(2):
			self.tap(self.driver, (0.8129, 0.9348958333))
			sleep(1)
		print '点击协会'
		sleep(2)
		for i in xrange(2):
			self.tap(self.driver, (0.4611, 0.4156))
			sleep(1)
		print '点击箱子1'
		sleep(2)
		for i in xrange(2):
			self.tap(self.driver, (0.7657, 0.5421))
			sleep(1)
		print '点击箱子2'
		sleep(5)
		self.driver.click(100, 100)
		sleep(2)
		for i in xrange(2):
			self.tap(self.driver, (0.7194, 0.9348958333))
			sleep(2)
		print '点击确定'
		sleep(10)
		self.click_images(self.driver, 'game-random-name@auto.png')

		print '随机名字'
		sleep(2)
		self.click_images(self.driver, 'game-submit@auto.png')

		print '提交'
		sleep(2)
	def pay(self,driver):
		self.driver = driver
		self.click_images(self.driver, 'game-zhuanshi@auto.png')

		print '点击砖石+'
		sleep(2)
		self.click_images(self.driver, 'game-6-zhuanshi@auto.png')

		print '点击6元砖石'
		sleep(15)
	def images_or_none(self,driver,images_name,timeout = 10):
		self.driver = driver
		game_name = configure.game_name
		try:
			self.wait_images(self.driver, images_name,timeout)
		except:
			pass
		images =  self.driver.exists('./'+game_name+'_images/'+images_name)
		return images


	def click_images(self, driver,  images_name):
		self.driver = driver
		game_name = configure.game_name
		images = self.driver.click_image('./' + game_name +'_images/'+ images_name)
		return images

	def wait_images(self,driver,images,timeout = 10):
		self.driver = driver
		game_name = configure.game_name
		images= self.driver.wait('./' + game_name + '_images/' + images,timeout)
		return images

	def tap(self,driver,value):
		self.driver = driver
		size = self.size()
		return self.driver.click(size[0] * value[0], size[1] * value[1])