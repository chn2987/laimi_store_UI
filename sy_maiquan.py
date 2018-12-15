#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年9月18日

@author: 从快捷入口买券操作(没有支付)
'''
from appium import webdriver
import time
from time import sleep

def maiquan(driver):
    time.sleep(2)
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().text("买券")').click()
        time.sleep(1)
        driver.find_element_by_id('com.zskuaixiao.store.test:id/imageView2').click()
        time.sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("加入购物车")').click()
        time.sleep(1)
    except:
        print('执行错误')
        
    
    '''
    time.sleep(5)
    def getSize():
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return (x, y) 
    
    #屏幕向上滑动
    def swipeUp(t):
        l = getSize()
        x1 = int(l[0] * 0.5)    #x坐标
        y1 = int(l[1] * 0.75)   #起始y坐标
        y2 = int(l[1] * 0.25)   #终点y坐标
        driver.swipe(x1, y1, x1, y2,t)   
    swipeUp(1000)
    '''
    
    
    
    
    