# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:53:06 2023

@author: USER
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def index_choose():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://www.liontravel.com/category/zh-tw/index")
    
    
    WebDriverWait(browser, 10).until(          #等待主頁回應，搜尋框未出來前，會無法執行以下動作
        expected_conditions.presence_of_element_located((By.ID,'searchPanel-195356'))
    )
    
    time.sleep(5)
    
    # root = browser.find_element(By.CSS_SELECTOR,"div#searchPanel-195356")
    jscode = "return document.querySelector('#searchPanel-195356').shadowRoot"
    shadowroot = browser.execute_script(jscode)
    content = shadowroot.find_elements(By.CSS_SELECTOR,"div.tabs_container--3vm6i ul li")       
    content[1].click()   #點目的地搜尋
    
    content_2 = shadowroot.find_elements(By.CSS_SELECTOR,"div.row--1f0Zy") #div.dropdown-wrap div.dropdownBoxPc div.selectBox div.contentWrap span
    content_2[0].click()  #選擇出發地外框
    content_3 = shadowroot.find_elements(By.CSS_SELECTOR,"div.dropdownBoxContent.open div.selectContentWrap div.option span")
    content_3[0].click()  #選擇台北  (台北 松山/桃園機場  台中  台南  高雄  不限  北北基  桃竹苗  中彰投  雲嘉南  高屏  宜花東 )
    
    content_4 = shadowroot.find_elements(By.CSS_SELECTOR,"div.row--1f0Zy")
    content_4[1].click()  #選擇目的地外框
    content_5 = shadowroot.find_elements(By.CSS_SELECTOR,"div.ntb_rcln.one_floor ul.tabs li span") #div.row--1f0Zy div div div.inputSkin_Parent div.ListStyle.allDeviceMenuListDtmRajn div.dtm_rcfr-wrap.open
    content_5[1].click()  #選擇東北亞
    
    content_6 = shadowroot.find_elements(By.CSS_SELECTOR,"div.panel.active div.sec div.sec_content span.item") #div.sec div.sec_content
    content_6[45].click()  #選擇北海道
    # for i in content_6:
    #     print(i.get_attribute("innerHTML"),end=" ")
    
    content_7 = shadowroot.find_elements(By.CSS_SELECTOR,"div.row--1f0Zy")
    content_7[4].click()
    
    browser.switch_to.window(browser.window_handles[1])  #browser.window_handles[1] 取得新分頁的標籤名稱，並將控制權轉換給新分頁
    
    return browser
    

