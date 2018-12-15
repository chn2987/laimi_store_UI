#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年11月18日

@author:用于登录前处理滑动页的
'''
from appium import webdriver
import time
from time import sleep
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
#desired_caps['deviceName'] = 'SSKJLN7H99999999'432705
desired_caps['deviceName'] = '127.0.0.1：62001'

#接收调用信息并调用函数
def chen(driver):
    print('登录前需要-操作启动页')
    swipLeft(driver,1000)
    time.sleep(0.2)
#获得机器屏幕大小x,y
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

#左划屏幕操作
def swipLeft(dr,t):
    l=getSize(dr)
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    dr.swipe(x1,y1,x2,y1,t)
    time.sleep(0.3)
    dr.swipe(x1,y1,x2,y1,t)
    time.sleep(0.3)
    dr.swipe(x1,y1,x2,y1,t)
    time.sleep(0.3)
    dr.swipe(x1,y1,x2,y1,t)
    time.sleep(0.8)
    dr.find_element_by_id('com.zskuaixiao.store.test:id/ib_finish_guide').click()
    print('滑动正常完成')
 
    
   

