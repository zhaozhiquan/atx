#!/usr/bin/env python
# coding=utf-8
import os
import unittest
import atx
from time import sleep, strftime
import public.methods as public
import configure

class YSDKSDK(unittest.TestCase,public.Methods):
	u'''YSDKC-sdk测试'''
	def setUp(self):
		if configure.device_name == '':
			self.driver = atx.connect()
		else:
			self.driver = atx.connect(configure.device_name)
		self.driver.start_app(configure.package_name,configure.activity_name)
		sleep(25)
	def tearDown(self):
		pass
		self.driver.stop_app(configure.package_name)
	def test_001(self):
		u'''QQ登录-取消'''
		self.click_images(self.driver,'game-gonggao@auto.png')
		self.click_images(self.driver,'game-qq-login@auto.png')
		sleep(5)
		#取消登录
		ele = self.element_or_none(self.driver,'text','返回')
		if ele:

			ele.click()
		else:

			self.tap(self.driver,(0.074,0.07))
		sleep(2)
		image1 = self.images_or_none(self.driver,'game-qq-login@auto.png')
		self.dy_IsNotNone(self.driver,image1,'test_001')

	def test_002(self):
		u'''QQ登录-成功'''
		self.click_images(self.driver, 'game-gonggao@auto.png')
		self.click_images(self.driver, 'game-qq-login@auto.png')
		sleep(5)
		ele = self.element_or_none(self.driver, 'text', '登录')
		if ele:

			ele.click()
		else:

			self.tap(self.driver,(0.5,0.7635))
		sleep(5)
		image1 = self.images_or_none(self.driver, 'game-server-list@auto.png')
		self.dy_IsNotNone(self.driver, image1, 'test_002')

	def test_003(self):
		u'''QQ登录-自动成功'''
		self.click_images(self.driver, 'game-gonggao@auto.png')
		self.click_images(self.driver, 'game-qq-login@auto.png')
		sleep(5)
		image1 = self.images_or_none(self.driver, 'game-server-list@auto.png')
		self.dy_IsNotNone(self.driver, image1, 'test_003')

	def test_004(self):
		u'''微信登录-取消'''
		self.click_images(self.driver, 'game-gonggao@auto.png')
		self.click_images(self.driver, 'game-weixin-login@auto.png')
		sleep(5)
		self.tap(self.driver,(0.069,0.075))  #点击X按钮
		sleep(2)
		image1 = self.images_or_none(self.driver,'game-weixin-login@auto.png')
		self.dy_IsNotNone(self.driver,image1,'test_004')

	def test_005(self):
		u'''微信登录-成功'''
		self.click_images(self.driver, 'game-gonggao@auto.png')
		self.click_images(self.driver, 'game-weixin-login@auto.png')
		sleep(5)
		self.tap(self.driver,(0.5,0.62))  #点击登录
		sleep(5)
		image1 = self.images_or_none(self.driver, 'game-server-list@auto.png')
		self.dy_IsNotNone(self.driver, image1, 'test_005')

	def test_006(self):
		u'''微信登录-自动成功'''
		self.click_images(self.driver, 'game-gonggao@auto.png')
		self.click_images(self.driver, 'game-weixin-login@auto.png')
		sleep(5)
		image1 = self.images_or_none(self.driver, 'game-server-list@auto.png')
		self.dy_IsNotNone(self.driver, image1, 'test_006')

	def test_007(self):
		u'''验证登录票据(当前微信票据),QQ登录,需授权'''
		self.click_images(self.driver, 'game-gonggao@auto.png')
		self.click_images(self.driver, 'game-qq-login@auto.png')
		sleep(5)
		ele = self.element_or_none(self.driver,'text', '登录')
		if ele:
			self.dy(self.driver,unicode(ele.text),u'登录','test_007')
		else:
			images = self.images_or_none(self.driver,'game-qq-login@auto.png')
			self.dy_IsNone(self.driver,images,'test_007')

	def test_008(self):
		u'''验证登录票据(当前QQ票据),微信登录,需授权'''
		self.click_images(self.driver, 'game-gonggao@auto.png')
		self.click_images(self.driver, 'game-weixin-login@auto.png')
		sleep(5)
		ele = self.element_or_none(self.driver, 'text', '微信登录')
		if ele:
			self.dy(self.driver, unicode(ele.text), u'微信登录','test_008')
		else:
			images = self.images_or_none(self.driver, 'game-weixin-login@auto.png')
			self.dy_IsNone(self.driver, images, 'test_008')

	def test_009(self):
		u'''退出游戏,取消'''
		self.click_images(self.driver,'game-gonggao@auto.png')
		sleep(1)
		self.driver.keyevent('KEYCODE_BACK')
		self.click_images(self.driver,'game-exit-cancel@auto.png')
		sleep(1)
		images = self.images_or_none(self.driver,'game-weixin-login@auto.png')
		self.dy_IsNotNone(self.driver,images,'test_009')

	def test_010(self):
		u'''退出游戏,确定'''
		self.click_images(self.driver, 'game-gonggao@auto.png')
		sleep(1)
		self.driver.keyevent('KEYCODE_BACK')
		self.click_images(self.driver, 'game-exit-sure@auto.png')
		sleep(1)
		images = self.images_or_none(self.driver, 'game-weixin-login@auto.png')
		self.dy_IsNone(self.driver, images, 'test_010')
	def second_start(self):
		'''第二次启动游戏'''
		self.tearDown()
		sleep(5)
		self.setUp()
		self.click_images(self.driver, 'game-gonggao@auto.png')
		self.click_images(self.driver, 'game-weixin-login@auto.png')
		sleep(5)

	def first_enter_game(self):
		'''首次进入游戏'''
		if self.enter_game_new(self.driver)  == None:#新手进入游戏--直到过完boss
			self.second_start()              #第二次启动游戏
			self.enter_game(self.driver)     #进入游戏,小镇外面
			self.enter_bar(self.driver)      #进入酒吧,命名
			sleep(10)
		else:
			self.second_start()
			self.enter_game(self.driver)  # 进入游戏,小镇外面

	def test_011(self):
		u'''进入游戏,调起支付,关闭'''
		self.test_005()    #微信登录
		self.first_enter_game()
		self.pay(self.driver)
		self.element(self.driver, 'className', 'android.widget.ImageButton').click()
		ele = self.element_or_none(self.driver,'text','确认支付方式')
		self.dy_IsNone(self.driver,ele,'test_011')

	def test_012(self):
		u'''调起QQ支付,并取消'''
		self.click_images(self.driver, 'game-gonggao@auto.png')
		self.click_images(self.driver, 'game-weixin-login@auto.png')
		sleep(5)
		self.enter_game(self.driver)
		self.pay(self.driver)
		self.element(self.driver, 'text', 'QQ钱包支付').click()
		images = self.images_or_none(self.driver,'qqpay-view@auto.png',timeout=20)
		self.dy_IsNotNone(self.driver, images, 'test_012')
		sleep(5)
		#取消
		self.driver.keyevent('KEYCODE_BACK')
		sleep(5)
		ysdk_pay = self.element(self.driver,'text','确认支付方式')
		self.dy(self.driver,unicode(ysdk_pay.text),u'确认支付方式','test_012')

	def test_013(self):
		u'''调起微信支付,并取消'''
		self.click_images(self.driver, 'game-gonggao@auto.png')
		self.click_images(self.driver, 'game-weixin-login@auto.png')
		sleep(5)
		self.enter_game(self.driver)
		self.pay(self.driver)
		self.element(self.driver,'text','微信支付').click()
		images = self.images_or_none(self.driver,'weixinpay-view@auto.png',timeout=20)
		self.dy_IsNotNone(self.driver,images,'test_013')
		sleep(5)
		self.driver.keyevent('KEYCODE_BACK')
		sleep(5)
		ysdk_pay = self.element(self.driver, 'text', '确认支付方式')
		self.dy(self.driver, unicode(ysdk_pay.text), u'确认支付方式', 'test_013')

	def test_014(self):
		u'''调起Q币支付,并取消'''
		self.click_images(self.driver, 'game-gonggao@auto.png')
		self.click_images(self.driver, 'game-weixin-login@auto.png')
		sleep(5)
		self.enter_game(self.driver)
		self.pay(self.driver)
		b = []
		a = self.element(self.driver,'className','android.widget.TextView')
		for i in range(len(a)):
			b.append(a[i].text)
		a[b.index(u'Q币')].click()
		sleep(10)
		qb_pay = self.element(self.driver, 'text', '充值Q币')
		self.dy(self.driver,unicode(qb_pay.text),u'充值Q币','test_014')
		self.element(self.driver, 'text', '返回').click()
		sleep(5)
		ysdk_pay = self.element_or_none(self.driver, 'text', '返回')
		self.dy_IsNone(self.driver,ysdk_pay,'test_014')

	def test_015(self):
		u'''调起QQ卡支付,并取消'''
		self.click_images(self.driver, 'game-gonggao@auto.png')
		self.click_images(self.driver, 'game-weixin-login@auto.png')
		sleep(5)
		self.enter_game(self.driver)
		self.pay(self.driver)
		self.element(self.driver,'text','QQ卡').click()
		sleep(2)
		qq_card = self.element_or_none(self.driver,'text','请输入QQ卡信息')
		self.dy(self.driver,unicode(qq_card.text),u'请输入QQ卡信息','test_015')
		self.element(self.driver, 'className', 'android.widget.ImageButton').click()
		sleep(2)
		ysdk_pay = self.element(self.driver, 'text', '确认支付方式')
		self.dy(self.driver, unicode(ysdk_pay.text), u'确认支付方式', 'test_015')

	def test_016(self):
		u'''调起手机充值卡支付,并取消'''
		self.click_images(self.driver, 'game-gonggao@auto.png')
		self.click_images(self.driver, 'game-weixin-login@auto.png')
		sleep(5)
		self.enter_game(self.driver)
		self.pay(self.driver)
		self.element(self.driver,'text','手机充值卡').click()
		sleep(2)
		qq_card = self.element_or_none(self.driver,'text','请输入充值卡信息')
		self.dy(self.driver,unicode(qq_card.text),u'请输入充值卡信息','test_016')
		self.element(self.driver, 'className', 'android.widget.ImageButton').click()
		sleep(2)
		ysdk_pay = self.element(self.driver, 'text', '确认支付方式')
		self.dy(self.driver, unicode(ysdk_pay.text), u'确认支付方式', 'test_016')

	def test_017(self):
		u'''游戏内切换账号'''
		self.click_images(self.driver, 'game-gonggao@auto.png')
		self.click_images(self.driver, 'game-weixin-login@auto.png')
		sleep(5)
		self.enter_game(self.driver)
		self.click_images(self.driver, 'game-more@auto.png')
		self.click_images(self.driver, 'game-set@auto.png')
		self.click_images(self.driver, 'game-imformation@auto.png')
		self.click_images(self.driver, 'game-swith@auto.png')
		images = self.images_or_none(self.driver, 'game-gonggao@auto.png',timeout=20)
		self.dy_IsNotNone(self.driver,images,'test_017')


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(YSDKSDK)
	unittest.TextTestRunner(verbosity=2).run(suite)
	'''now_time = strftime("%Y-%m-%d %H_%M_%S")
	filename = 'D:/test_result/'+now_time+"-result.html"
	fp = open(filename, 'wb')
	case_shuo_ming = u'测试情况'
	HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=case_shuo_ming).run(suite)
	fp.close()'''