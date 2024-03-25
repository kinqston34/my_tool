# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:25:38 2023

@author: USER
"""
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 


class TR_index():
    
    def __init__(self,start,end,query,day,start_time,end_time):
        self.start = start
        self.end = end
        self.query = query
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get("https://www.railway.gov.tw/")
            
        
    def quit(self):
        self.browser.quit()
    
    def search_mode(self):
        if self.query == "0":
            self.browser.find_element(By.ID,"startOrEndTime1").click()
        elif self.query == "1":
            self.browser.find_element(By.ID,"startOrEndTime2").click()
            
    def search_insert(self):
        #使用者輸入的是出發時間搜尋 還是 抵達時間搜尋
        self.search_mode()
        #輸入開始站        
        self.browser.find_element(By.ID,"startStation").send_keys(self.start)
        #等待下拉選單開啟
        WebDriverWait(self.browser, 10).until(        
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"ul#ui-id-1 li.ui-menu-item"))
            )
        #讀取下拉選單並確定要選擇的"完全符合"輸入站名
        d = self.browser.find_elements(By.CSS_SELECTOR,"ul#ui-id-1 li")
        for i in d:
            if i.text.split("-")[1]==self.start:
                i.click()                               
        del d
        #輸入結束站
        self.browser.find_element(By.ID,"endStation").send_keys(self.end)
        
        #等待下拉選單開啟
        WebDriverWait(self.browser, 10).until(        
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"ul#ui-id-2 li.ui-menu-item"))
            )
        #讀取下拉選單並確定要選擇的"完全符合"輸入站名，如果沒有選完全符合的選項 直接進入下一步 系統就會幫你選跑出來的第一個
        r = self.browser.find_elements(By.CSS_SELECTOR,"ul#ui-id-2 li")
        for i in r:
            if i.text.split("-")[1]==self.end:
                i.click()       
        del r
        #處理日期輸入
        self.browser.find_element(By.ID,"rideDate").click()  
        action = ActionChains(self.browser)
        action.send_keys(Keys.END).key_down(Keys.SHIFT).send_keys(Keys.HOME).key_up(Keys.SHIFT).send_keys(Keys.DELETE).send_keys(self.day).perform()
        del action

        start_t = Select(self.browser.find_element(By.ID,"startTime"))
        start_t.select_by_value(self.start_time)
        del start_t
        
        end_t = Select(self.browser.find_element(By.ID,"endTime"))
        end_t.select_by_value(self.end_time)
        del end_t
    def query_click(self):
        self.browser.find_element(By.CSS_SELECTOR,"input.btn.btn-basic.btn-lg").click()
             
        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME,"itinerary-controls"))
            )
    
       
# s = TR_index("嘉義","台北","1","20231211","08:00","23:59")
# s.search_insert()
# time.sleep(20)
# s.quit()

    