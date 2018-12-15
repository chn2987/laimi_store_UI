#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年9月14日
@author:在全部商品中搜索__并加入购物车
'''
from appium import webdriver
import time
from time import sleep
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '127.0.0.1：62001'
#主要实现在 全部商品列表搜索商品
def sou_shangping(driver):
    time.sleep(3)
    #点击全部商品
    driver.find_element_by_id('com.zskuaixiao.store.test:id/rb_category').click()
    time.sleep(1)
    #点击搜索 
    driver.find_element_by_id('com.zskuaixiao.store.test:id/et_search').click()
    source = open("G:\\eclipse_1\\android_appium\\android_shangdian\\shangping.txt", "r")
    #读取source的所有行
    un = source.readlines()
    #通过页面元素index定位
    #driver.find_element_by_android_uiautomator('new UiSelector().index(0)').send_keys("八宝粥")
    driver.find_element_by_android_uiautomator('new UiSelector().index(0)').send_keys(un)
    time.sleep(0.5)
    #点击回车(进行搜索)
    driver.keyevent(66)
    #driver.find_element_by_xpath("//android.widget.EditText[@resource-id=\'com.zskuaixiao.store.test:id/et_search\']").send_keys(u'八宝粥')
    time.sleep(1)
    #获取元素的文本   
    chen=driver.find_element_by_id('com.zskuaixiao.store.test:id/tv_title').text
    #转换数据
    zhuan="".join(un)
    #查看数据类型
    #print (type(zhuan),type(chen))
    time.sleep(1)
    #判断zhuan变量是否在chen变量中(返回true或false)
    jieguo= zhuan in chen  
    #判断搜索列表是否有该商品 (根据文件动态判断) 
    if jieguo==True:
        print ('搜索商品_返回成功')
    else:
        print ('搜索商品_失败！')
'''
#判断搜索列表是否有该商品 (非动态判断)
    try:
      #通过xpath判断
      driver.find_element_by_android_uiautomator('new UiSelector().textMatches("^八宝粥.*")')
      print ('搜索商品_返回成功')
    except:
      print ('搜索商品_失败！')
      pass
'''
#加购物车操作_并验证是否成功(必须先查到结果，否则失败)    
def jia_gouwuche(driver):
    time.sleep(2)
    #通过xpath点击搜索列表的商品
    driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id=\"com.zskuaixiao.store.test:id/recycler_view\"]/android.widget.RelativeLayout[1]").click()
    # 点击加入购物车按钮
    driver.find_element_by_id('com.zskuaixiao.store.test:id/tv_add_to_cart').click()
    time.sleep(0.5)
    #进入购物车
    driver.find_element_by_id('com.zskuaixiao.store.test:id/iv_cart').click()
    time.sleep(2)
    bb=driver.find_element_by_android_uiautomator('new UiSelector().text("泰奇八宝粥绿色优惠装1 370g*24(整箱)")').text
    print('bb=',bb)
    source = open("G:\\eclipse_1\\android_appium\\android_shangdian\\shangping.txt", "r")
    un = source.readlines()
    zhuan="".join(un)#list转str
    print('un',un)
    chen= zhuan in bb
    time.sleep(1)
    if chen==True:
        print ('验证加入购物车_商品成功')
        #返回首页
        #driver.find_element_by_id('com.zskuaixiao.store.test:id/rb_home').click()
        driver.keyevent(4)
        time.sleep(1)
        driver.keyevent(4)
        time.sleep(1)
        driver.keyevent(4)
        time.sleep(1)   
    else:
        print ('购物车内没有该商品_加入失败')
        #返回首页
        driver.find_element_by_id('com.zskuaixiao.store.test:id/rb_home').click()
    time.sleep(5)
    #driver.quit()
    
      































  
    
    
