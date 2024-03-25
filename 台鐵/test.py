# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:42:21 2023

@author: USER
"""
import time
from selenium.webdriver.common.by import By
from TR_index import TR_index
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class test(TR_index):
    def __init__(self, start,end):
        super().__init__(start,end,query=None,day=None,start_time=None,end_time=None)
        
    def search_insert(self):
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
        
        
        
        self.browser.find_element(By.ID,"endStation").send_keys(self.end)
        
        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"ul#ui-id-2 li.ui-menu-item"))
            )
        
        r = self.browser.find_elements(By.CSS_SELECTOR,"ul#ui-id-2 li")
        for i in r:
            if i.text.split("-")[1]==self.end:
                i.click()
                
        
        
t = test("新竹","臺中")
t.search_insert()
time.sleep(10)
t.quit()
