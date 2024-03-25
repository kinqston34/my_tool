# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:17:41 2023

@author: USER
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

class Thsrc_index_search():
    
    def __init__(self,departure,location,mode,departure_day,departure_time,location_day,location_time,discount=False):
        
        self.departure = departure        #user insert
        self.location = location
        self.mode = mode
        self.d_day = departure_day
        self.l_day = location_day
        self.d_time = departure_time
        self.l_time = location_time
        self.discount = discount
        
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get("https://www.thsrc.com.tw/")
    
        WebDriverWait(self.browser, 10).until(          #等待主頁回應，搜尋框未出來前，會無法執行以下動作
            expected_conditions.presence_of_element_located((By.CLASS_NAME,'footer-bottom'))
        )
            
        self.browser.find_element(By.CLASS_NAME,"swal2-confirm.swal2-styled").click() #cookie 同意
    
    def index_insert_key(self):
        Departure = Select(self.browser.find_element(By.ID,"select_location01"))
        Departure.select_by_visible_text(self.departure)  #選擇出發地
        
        Location = Select(self.browser.find_element(By.ID,"select_location02"))
        Location.select_by_visible_text(self.location)   #選擇目的地
        
        Mode = Select(self.browser.find_element(By.ID,"typesofticket"))
        Mode.select_by_visible_text(self.mode)   #選擇單程票還是去回程票\
        
        if self.mode == "單程":
            self.one_way()
        elif self.mode == "去回程":
            self.one_way()
            self.two_way()
        
        self.browser.find_element(By.CSS_SELECTOR,"div.filter-option").click()   #點選優惠，打開優惠選項
        #最多只能選擇四種優惠(高鐵定的)
        #key_click = "0"         #從使用者選擇而定
        self.discount_choose(self.discount)   #key_click
    
        self.browser.find_element(By.ID,"start-search").click()
    
    #========換到搜尋後頁面==============
    
        WebDriverWait(self.browser,10).until(          #等待主頁回應，搜尋框未出來前，會無法執行以下動作
            expected_conditions.presence_of_element_located((By.CLASS_NAME,'tr-row'))
        )

    
    def one_way(self):   #設定去程時間
        
        self.browser.find_element(By.ID,"Departdate01").send_keys(Keys.DELETE)    #先刪除預設值 用delete，在執行語法模擬，最後輸入值
        self.browser.execute_script("document.querySelector(\"#Departdate01\").onkeydown='return AllowTab(event)'")  
        self.browser.find_element(By.ID,"Departdate01").send_keys(self.d_day) 
        
        self.browser.find_element(By.ID,"outWardTime").send_keys(Keys.DELETE)    #先刪除預設值 用delete，在執行語法模擬，最後輸入值
        self.browser.execute_script("document.querySelector(\"#outWardTime\").onkeydown='return AllowTab(event)'")  
        self.browser.find_element(By.ID,"outWardTime").send_keys(self.d_time) 
        
        
    def two_way(self):    #設定回程時間
         
        self.browser.find_element(By.ID,"Returndate01").send_keys(Keys.DELETE)    #先刪除預設值 用delete，在執行語法模擬，最後輸入值
        self.browser.execute_script("document.querySelector(\"#Returndate01\").onkeydown='return AllowTab(event)'")  
        self.browser.find_element(By.ID,"Returndate01").send_keys(self.l_day) 
        
        self.browser.find_element(By.ID,"returnTime").send_keys(Keys.DELETE)    #先刪除預設值 用delete，在執行語法模擬，最後輸入值
        self.browser.execute_script("document.querySelector(\"#returnTime\").onkeydown='return AllowTab(event)'")  
        self.browser.find_element(By.ID,"returnTime").send_keys(self.l_time)
        self.browser.find_element(By.ID,"returnTime").send_keys(Keys.ENTER) #避免畫面衝突
    
    def discount_choose(self,key_click = False):
        
        if key_click == False:
            return
        else:
            dis = self.browser.find_elements(By.CSS_SELECTOR,"ul.dropdown-menu.inner.show li a span.text") 
            for i in key_click:
                dis[eval(i)].click()
    
                # discount[0].click()   #點選早鳥
                # discount[1].click()   #點選校外教學
                # discount[2].click()   #點選大學生
                # discount[3].click()   #點選指定車次團體
                # discount[4].click()   #點選20人團體
                # discount[5].click()   #點選企業會員

class Station(Thsrc_index_search):         #主頁點選車站資訊
    
    def __init__(self, departure, location):
        
        super().__init__(departure,location,mode=None,departure_day=None,departure_time=None,location_day=None,location_time=None,discount=False)
        self.browser.find_element(By.CSS_SELECTOR,"a[title='車站資訊']").click()
        
        WebDriverWait(self.browser, 10).until(          #等待主頁回應，搜尋框未出來前，會無法執行以下動作
            expected_conditions.presence_of_element_located((By.ID,'northBound'))
        )
        
    def find_railway_station(self):
        
        self.browser.find_element(By.CSS_SELECTOR,"a[title={}]".format(self.location)).click()
        
        WebDriverWait(self.browser, 10).until(          #等待主頁回應，搜尋框未出來前，會無法執行以下動作
            expected_conditions.presence_of_element_located((By.ID,"northBound"))
        )
        
        try:
            self.browser.find_element(By.CSS_SELECTOR,"a[title='臺灣鐵路']")
        except NoSuchElementException:
            return False
        else:
            return True
            
    
    
    
# browser = web_index_search()
# time.sleep(10)
# browser.quit()

