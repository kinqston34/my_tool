# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class Central_Weather_Index():
    
    def __init__(self,city=None,country=None):
        self.browser = webdriver.Chrome()
        self.browser.get("https://www.cwa.gov.tw/V8/C/W/OBS_Map.html")
        self.city = city
        self.country = country
        
    def quit(self):
        self.browser.quit()
        
    def weather_city_mode(self):
        self.browser.find_element(By.CSS_SELECTOR,"li[tabindex='23']").click()
        self.select = self.browser.find_element(By.NAME,"CID")
        self.select.click()
        self.city_op = Select(self.select)
        # example = "嘉義市" or "嘉義縣"
        for op in self.city_op.options:
            if self.city == op.text: 
                self.city_op.select_by_visible_text(self.city)
                self.browser.find_element(By.CSS_SELECTOR,u"button[data-gtmtitle='選單_天氣_縣市預報_確定按鈕']").click()
                break
        else:
            print(self.city+"不在選項中")
            
    def weather_country_mode(self):
        self.browser.find_element(By.CSS_SELECTOR,"li[tabindex='23']").click()
        self.select = self.browser.find_elements(By.TAG_NAME,"select")[1]
        self.select.click()
        self.city_op = Select(self.select)
        # example = "嘉義市" or "嘉義縣"
        for op in self.city_op.options:
            if self.city == op.text:
                self.city_op.select_by_visible_text(self.city)
                break
        else:
            print(self.city+"不在選項中")
        # example = "新港鄉" or "北港鎮"
        self.select = self.browser.find_element(By.NAME,"TID")
        self.select.click()
        self.country_op = Select(self.select)
        
        for op in self.country_op.options:
            if self.country == op.text:
                self.country_op.select_by_visible_text(self.country)
                self.browser.find_element(By.CSS_SELECTOR,u"button[data-gtmtitle='選單_天氣_鄉鎮預報_確定按鈕']").click()
                break
        else:
            print(self.country+"不在選項中")
    
        

# w = Central_Weather_station("嘉義縣","新港鄉")
# w.weather_city_country_mode() 
# time.sleep(10)
# w.quit()       
        
        