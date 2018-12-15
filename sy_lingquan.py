#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年11月20日

@author:优惠券___逐渐领取操作(领券后android没有自动过滤，自动化容易出错，，所以在执行前需要先配置好优惠券)
'''
from appium import webdriver
import time
from time import sleep

def lingquan(driver):
    driver.find_element_by_android_uiautomator('new UiSelector().text("领券")').click()
    time.sleep(2)
    #driver.find_element_by_xpath("//*android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]").click()
    #driver.find_element_by_name("我的优惠券").click()
    for i in range(1,9):
        time.sleep(2)
        if i>=7:
            for a in range(1,8):
                c=1/i
                x = driver.get_window_size()['width']
                #获取屏幕高
                y = driver.get_window_size()['height']
                time.sleep(3)
                #向上滑屏幕     
                driver.swipe(1/2*x, 19/20*y, 1/2*x, c*y, 200)
                time.sleep(5)
                try:
                    aa=driver.find_element_by_android_uiautomator('new UiSelector().index('+str(a)+')').find_element_by_id('com.zskuaixiao.store.test:id/rl_control').click()
                    driver.find_element_by_android_uiautomator('new UiSelector().index('+str(a)+')').find_element_by_id('com.zskuaixiao.store.test:id/rl_control')
                    print('1滑动后领取成功%d' %(a))
                     
                except:
                    try:
                        #领取不成功，在商品列表
                        time.sleep(2)
                        driver.keyevent(4)
                        a+=1
                        time.sleep(2)
                        driver.find_element_by_android_uiautomator('new UiSelector().text("领券")').click()
                        x = driver.get_window_size()['width']
                        #获取屏幕高
                        y = driver.get_window_size()['height']
                        time.sleep(3)
                        #向上滑屏幕     
                        driver.swipe(1/2*x, 1/2*y, 1/2*x, c*y, 200)
                        time.sleep(3)
                        #______________二次滑动________________________________________
#                         time.sleep(2)
#                         x = driver.get_window_size()['width']
#                          #获取屏幕高
#                         y = driver.get_window_size()['height']
#                         time.sleep(3)
#                         #向上滑屏幕     
#                         pp=i+a
#                         driver.swipe(1/2*x, 1/2*y, 1/2*x, 1/pp*y, 200)
#                         time.sleep(5)
#                          
                        #点击领券按钮
                        aa=driver.find_element_by_android_uiautomator('new UiSelector().index('+str(i)+')').find_element_by_id('com.zskuaixiao.store.test:id/rl_control').click()
                        time.sleep(1)
                        driver.find_element_by_android_uiautomator('new UiSelector().index('+str(i)+')').find_element_by_id('com.zskuaixiao.store.test:id/rl_control')
                        print('2滑动后领取成功%d' %(a))
                    except:
                        time.sleep(2)
                        driver.keyevent(4)
                        time.sleep(2)
                        driver.find_element_by_android_uiautomator('new UiSelector().text("领券")').click()
                        print("滑动后领取失败%d" %(a))
                                             
        #这里是i小于7执行的语句(小于一屏)                 
        try:
          aa=driver.find_element_by_android_uiautomator('new UiSelector().index('+str(i)+')').find_element_by_id('com.zskuaixiao.store.test:id/rl_control').click()
          driver.find_element_by_android_uiautomator('new UiSelector().index('+str(i)+')').find_element_by_id('com.zskuaixiao.store.test:id/rl_control')
          print('1小于一屏幕领取成功%d' %(i))
             
        except:
            try:
                #领取不成功，在商品列表
                time.sleep(2)
                driver.keyevent(4)
                i+=1
                time.sleep(2)
                driver.find_element_by_android_uiautomator('new UiSelector().text("领券")').click()
                time.sleep(2)
                #点击领券按钮
                aa=driver.find_element_by_android_uiautomator('new UiSelector().index('+str(i)+')').find_element_by_id('com.zskuaixiao.store.test:id/rl_control').click()
                time.sleep(1)
                driver.find_element_by_android_uiautomator('new UiSelector().index('+str(i)+')').find_element_by_id('com.zskuaixiao.store.test:id/rl_control')
                print('2小于一屏幕领取成功%d' %(i))
                 
            except:
                time.sleep(2)
                driver.keyevent(4)
                time.sleep(1)
                driver.find_element_by_android_uiautomator('new UiSelector().text("领券")').click()
                print("小于一屏幕第%d次失败" %(i))
    
    #执行完毕返回首页
    driver.keyevent(4)                 

#     for p in range(2,20):
#         time.sleep(2)
#         w=1/p
#         x = driver.get_window_size()['width']
#          #获取屏幕高
#         y = driver.get_window_size()['height']
#         time.sleep(3)
#         #向上滑屏幕     
#         driver.swipe(1/2*x, 19/20*y, 1/2*x, w*y, 200)
#         time.sleep(4)
#         driver.keyevent(4)
#         time.sleep(2)
#         driver.find_element_by_android_uiautomator('new UiSelector().text("领券")').click()
#         print('滑动第%d' %(p))
        
#     driver.tap([(590,199)],10)#根据坐标定位
#     time.sleep(3)
#     #____获取当前界面所有元素 并写入文件
#     wei=driver.page_source
#     rr=open('E:\123.txt','w',encoding='utf-8')
#     rr.write(wei)#把wei写入123.txt

  
    
