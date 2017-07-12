#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    配置信息
	game_name,游戏名称简写,天命传说 = tmcs,王者远征 = wzyz
	packages_name   activity_name  可以在终端 输入 python -m atx apkparse <package_path>
	输出格式如下:
	{
    "main_activity": "com.zhankaigame.destiny.RenWanTangSplashActivity",
    "package_name": "com.zhankaigame.destiny.huawei"
	}
	device_name 设备的udid ,可以通过 adb devices 查看
	ZUK = 4c14b8b2
	三星 = 604dc279
	魅族 = 85ELBNPTMXTH
	vivo = fe4e119
	小米 = YDW8UG4TWWL7N7S8
	Coolpad = Y803-9-0x1fda0113
	金立 = FENVL7Y5GITOOVPN
	华为 = CKL6T16B29025193
	360 = a89e3b28
	努比亚 = 39ceca3f
	oppo = SCK7KBBYDICMS8WG
	乐视 = LE67A06300298090
'''

game_name = 'tmcs'
device_name = '4c14b8b2'
package_name = 'com.tencent.tmgp.shardsofdestiny'
activity_name = 'com.zhankaigame.destiny.RenWanTangMainActivity'




