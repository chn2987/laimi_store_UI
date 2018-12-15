#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年9月14日

@author:现实登陆操作_退出操作
'''
from appium import webdriver
import time
from time import sleep
import huadong
from symbol import except_clause

#定义运行脚本时不用每次提示安装
#capabilities.setCapability("noReset", true)
'''
#重装app或app路径不在电脑端时使用
desired_caps['appPackage'] = 'com.zskuaixiao.store.test'
desired_caps['appActivity'] = 'com.zskuaixiao.store.module.homepage.view.SplashActivity'
'''
#登陆app及判断是否成功
def denglu1(driver):
    time.sleep(2)
    try:
        #如果當前界面存在android.widget.ImageView元素(启动页元素)，就调用滑动方法(huadong.chen)
        driver.find_element_by_xpath("//android.widget.ImageView").text
        wei=huadong.chen(driver)
        #time.sleep(0.5)
        driver.find_element_by_id('com.zskuaixiao.store.test:id/et_login_name').clear()
        driver.find_element_by_id('com.zskuaixiao.store.test:id/et_login_name').send_keys('18520103625')
        #模拟点击回车
        driver.keyevent(66)
        time.sleep(0.2)
        #driver.find_element_by_id('com.zskuaixiao.store.test:id/et_password').clear()
        driver.find_element_by_id('com.zskuaixiao.store.test:id/et_password').send_keys('123456')
        #time.sleep(0.2)
        #提交登陆
        driver.find_element_by_id('com.zskuaixiao.store.test:id/btn_login').click()
        time.sleep(3)
        #正常流程去找首页，找不到就走异常
        try:
          #通过id判断
          #chen=driver.find_element_by_id('com.zskuaixiao.store.test:id/btn_login')
          #通过xpath判断
          driver.find_element_by_xpath("//*[contains(@text,'首页')]")
          print ('登录断言成功')
        except:
          print ('找不到元素')
          pass

    except:
        try:
            #如果當前界面存在“登录”按鈕，就直接登录操作
            driver.find_element_by_id('com.zskuaixiao.store.test:id/btn_login')
            driver.find_element_by_id('com.zskuaixiao.store.test:id/et_login_name').clear()
            driver.find_element_by_id('com.zskuaixiao.store.test:id/et_login_name').send_keys('18520103625')
            #模拟点击回车
            driver.keyevent(66)
            time.sleep(0.1)
            #driver.find_element_by_id('com.zskuaixiao.store.test:id/et_password').clear()
            driver.find_element_by_id('com.zskuaixiao.store.test:id/et_password').send_keys('123456')
            time.sleep(0.5)
            #提交登陆
            driver.find_element_by_id('com.zskuaixiao.store.test:id/btn_login').click()
            time.sleep(4)
            #正常流程去找首页，找不到就走异常
            try:
              #通过id判断
              #chen=driver.find_element_by_id('com.zskuaixiao.store.test:id/btn_login')
              #通过xpath判断
              driver.find_element_by_xpath("//*[contains(@text,'首页')]")#如果首页元素不存在就会跳到"except"
              print ('登录断言成功')
            except:
              print ('找不到元素')
              pass
        except:
            print("执行过程出现意外")
                
            
                
#实现退出 及判断是否到了登录页面
def tuichu(driver): 
    time.sleep(0.5)
    driver.find_element_by_id('com.zskuaixiao.store.test:id/rb_account').click()
    time.sleep(1)
    driver.find_element_by_id('com.zskuaixiao.store.test:id/iv_head').click()
    time.sleep(1)
    driver.find_element_by_id('com.zskuaixiao.store.test:id/btn_login').click()
    time.sleep(1)
    driver.find_element_by_id('android:id/button1').click()
    time.sleep(2)
    try:
      #通过id判断
      #chen=driver.find_element_by_id('com.zskuaixiao.store.test:id/btn_login')
      #通过xpath判断
      driver.find_element_by_xpath("//*[contains(@text,'登录')]")
      print ('测试通过_退出系统成功')
    except:
      print ('测试失败了_退出系统失败')
      pass
    time.sleep(2)
    
    '''
    driver.find_element_by_name("1").click()
    driver.find_element_by_name("5").click()
    '''