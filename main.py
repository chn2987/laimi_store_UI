#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
import time
from time import sleep
import denglu
import jia_gouwuche
import jiesuan_gouwuche
#import sy_huodong_chakan
import sy_shangping_sousuo
import sy_maiquan
import sy_lingquan
#import huadong
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
#desired_caps['deviceName'] = 'SSKJLN7H99999999'#当有多台设备时，需要声明
desired_caps["unicodeKeyboard"] = "True"#声明中文
desired_caps["resetKeyboard"] = "True"#声明中文，否则不支持中文
desired_caps['noReset'] = 'True'#执行时不初始化(保留上次登录状态、程序状态)
desired_caps['deviceName'] = '127.0.0.1：62001'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(1)
def kaishi():
    #wei=huadong.chen(driver)#已放到登录模块
    #dlu=denglu.denglu1(driver)#登录
    time.sleep(2)
    #fan=sy_lingquan.lingquan(driver)#领券中心
    mai=sy_maiquan.maiquan(driver)
    
    

    #sou_shangp=jia_gouwuche.sou_shangping(driver)#搜索商品
    #gu=jia_gouwuche.jia_gouwuche(driver)#加购物车
    #tuichu=denglu.tuichu(driver)#退出
    #jiesuan=jiesuan_gouwuche.gwc_jiesuan(driver)#结算购物车
    #ck_sy_huodong=sy_huodong_chakan.sy_manjian(driver)#查看首页活动
    #souuso_sy_shangping=sy_shangping_sousuo.sy_sousuo(driver)#首页_商品搜索
    
    


if __name__=='__main__':
    a=kaishi()
