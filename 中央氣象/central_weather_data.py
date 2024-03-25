# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:16:32 2023

@author: USER
"""
from central_weather_index import Central_Weather_Index
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
import re
import time

class Central_Weather_Data(Central_Weather_Index):
    
    def __init__(self,city,country=None):
        super().__init__(city,country)
        
    def city_today(self):
        weather = []
        super().weather_city_mode()
        self.title = self.browser.find_elements(By.CSS_SELECTOR,"li span.title")
        self.temperature = self.browser.find_elements(By.CSS_SELECTOR,"li span.tem span.tem-C.is-active")
        self.rain = self.browser.find_elements(By.CSS_SELECTOR,"li span.rain")
       
        for i,j,k in zip(self.title[:3],self.temperature[:3],self.rain[:3]):
            weather.append((i.text,j.text+"°C",k.text.split("\n")[1]))
        
        return weather
    
    def country_today(self):
        weather=[]
        super().weather_country_mode()
        self.browser.find_element(By.ID,"Tab_weeksTable").click()
        WebDriverWait(self.browser,5).until(
                expected_conditions.presence_of_element_located((By.ID,"TableIdweeks"))
            )
        pattern = re.compile("PC7_Wx PC7_D1 PC7_D1\w")
        #wx:天氣狀況 , maxT: 最高溫 , minT: 最低溫, rain: 降雨機率 , maxAT: 體感最高溫 , minAT: 體感最低溫, rh: 相對溼度
        # self.wx = self.browser.find_element(By.CSS_SELECTOR,"td[headers='PC7_Wx'] img")   
        # self.maxT = self.browser.find_elements(By.CSS_SELECTOR,"td[headers='PC7_MaxT'] span.tem-C")   
        # self.minT = self.browser.find_elements(By.CSS_SELECTOR,"td[headers='PC7_MinT'] span.tem-C")
        # self.rain = self.browser.find_elements(By.CSS_SELECTOR,"td[headers='PC7_Po']")
        # self.maxAT = self.browser.find_elements(By.CSS_SELECTOR,"td[headers='PC7_MaxAT'] span.tem-C")
        # self.minAT = self.browser.find_elements(By.CSS_SELECTOR,"td[headers='PC7_MinAT'] span.tem-C")
        # self.rh = self.browser.find_element(By.CSS_SELECTOR,"td[headers='PC7_RH']")
        
        td = self.browser.find_elements(By.CSS_SELECTOR,"td[headers='{}']".format(pattern))
        for i in td:
            print(i.get_attribute("innerHTML"))

w = Central_Weather_Data("嘉義縣","新港鄉")
w.country_today()

time.sleep(5)
w.quit()

