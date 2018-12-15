#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年9月15日
@author: chen
'''
from appium import webdriver
import re
import time
from time import sleep
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '127.0.0.1：62001'
def gwc_jiesuan(driver):
    time.sleep(5)
    #点击购物车
    driver.find_element_by_id('com.zskuaixiao.store.test:id/rb_cart').click()
    #判断购物车是否为空
    try:
        de=driver.find_element_by_id('com.zskuaixiao.store.test:id/tv_total').text
        #正则过滤掉不需要的字段
        #print('de',de)
        gege=re.findall(r" ¥(.+?).00",de)
        #把序列转换成str类型
        ee="".join(gege)
        #数据类型转换
        uu=int(ee)
        #判断是否达到配送条件  
        if uu>=10:
            print("购买商品金额_满足起送条件")
            try:
             #判断当前页面是否有sdv_goods，如果有就成功，否则走异常流程
              driver.find_element_by_id('com.zskuaixiao.store.test:id/sdv_goods')     
              print ('购物车中_有商品')
            except:
              print ('购物车中没有商品_或页面错误')
              exit()
          
            #点击去结算按钮
            driver.find_element_by_id('com.zskuaixiao.store.test:id/tv_balance').click()
            time.sleep(1)
            try:  
               driver.find_element_by_xpath("//android.widget.Button[@text=\'提交\']").click()
               time.sleep(1)
               #点击我的快消
               driver.find_element_by_id('com.zskuaixiao.store.test:id/rb_account').click()
               time.sleep(1)
               driver.find_element_by_android_uiautomator('new UiSelector().text("我的订单")').click()
               #判断订单是否成功
               try:
                  driver.find_element_by_android_uiautomator('new UiSelector().text("2017-11-20")').click() 
                  print ("结算购物车成功_生成订单")     
                  driver.keyevent(4)
                  driver.keyevent(4)
                  #返回首页
                  driver.find_element_by_id('com.zskuaixiao.store.test:id/rb_home').click()
                  print('返回首页成功')
                                    
               except:      
                    
                    print ("结算购物失败_没有生成订单")
            except:
                print('订单未提交-可能商品库存不足')
                try:
                    aa=driver.find_element_by_android_uiautomator('new UiSelector().text("自动修改")').text
                    print(aa)
                    if aa=='自动修改':
                        print('商品数量不足_需要修改数量')
                        time.sleep(2)
                        #点击自动修改
                        driver.find_element_by_android_uiautomator('new UiSelector().text("自动修改")').click()
                        time.sleep(2)
                        heji=driver.find_element_by_id('com.zskuaixiao.store.test:id/tv_total').text
                        chen=re.findall(r" ¥(.+?).00",heji)
                        kk="".join(chen)
                        shu=int(kk)
                        print(type(shu),shu)
                        if shu==0:
                            print("购物车内没有商品_或没有选中商品")
                            #返回首页
                            driver.find_element_by_id('com.zskuaixiao.store.test:id/rb_home').click()
                          
                        elif shu>0:
                            time.sleep(1)
                            #在点击去结算按钮
                            driver.find_element_by_id('com.zskuaixiao.store.test:id/tv_balance').click()
                            time.sleep(1)
                            #点击去结算按钮
                            driver.find_element_by_xpath("//android.widget.Button[@text=\'提交\']").click()
                            time.sleep(3)
                               #点击我的快消
                            driver.find_element_by_id('com.zskuaixiao.store.test:id/rb_account').click()
                            time.sleep(1)
                            driver.find_element_by_android_uiautomator('new UiSelector().text("我的订单")').click()
                            #判断订单是否成功
                            try:
                                driver.find_element_by_android_uiautomator('new UiSelector().text("2017-09-19")').click() 
                                print ("结算购物车成功_生成订单")     
                                driver.keyevent(4)
                                driver.keyevent(4)
                                #返回首页
                                driver.find_element_by_id('com.zskuaixiao.store.test:id/rb_home').click()
                                                    
                            except:           
                                print ("结算购物失败_没有生成订单")
                        else:
                            print("出现异常情况_中断购物车")
                            #返回首页
                            driver.find_element_by_id('com.zskuaixiao.store.test:id/rb_home').click()                             
                    else:
                        print ('存在第三种弹框,或页面元素改变')
                except:
                    cc=driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').text
                    
        else:
            pp=driver.find_element_by_id('com.zskuaixiao.store.test:id/tv_total').text           
            print("未达到起送条件_请继续购买",pp)
            
        '''        
        else:
            print("获取不到自动修改按钮_可能界面异常")
            driver.quit()
            exit()
            '''
    except:
        print('购物车没有任何内容')
        #返回首页
        driver.find_element_by_id('com.zskuaixiao.store.test:id/rb_home').click()              
       