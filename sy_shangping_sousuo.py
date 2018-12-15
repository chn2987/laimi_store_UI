#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年9月18日

@author: 实现首页商品名称、条码搜索
'''
from appium import webdriver
import time
from time import sleep

def sy_sousuo(driver):
    time.sleep(2)
    #点击首页_商品搜索框
    driver.find_element_by_id('com.zskuaixiao.store.test:id/et_search').click()
    time.sleep(2)
    #输入内容
    driver.find_element_by_android_uiautomator('new UiSelector().index(0)').send_keys('八宝粥')
    time.sleep(0.5)
    #点击回车
    driver.keyevent(66)
    
    
    