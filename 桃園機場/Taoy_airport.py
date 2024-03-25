# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 17:44:00 2024

@author: USER
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
import pandas as pd

import time

class TaoyuanAirport():

    def __init__(self):
        
        
        options = Options()
        options.add_argument("--headless")
        self.airport = webdriver.Chrome()
        self.airport.get("https://www.taoyuan-airport.com/flight_timetable")
        
    def quit(self):
        self.airport.quit()
    
      
    def fix_data_input(self,searchkey):
        
        self.searchkey = searchkey
        # 等待網頁表格資料載入
        
        self.data = {"apply_time":[],"terminal":[],"flight_informations":[],"location":[],"departure_time":[],"arrival_time":[],"weekdays":[]}    
        WebDriverWait(self.airport,5).until(    
            expected_conditions.presence_of_element_located((By.ID,'print'))    
        )
        
        search = self.airport.find_element(By.ID,"choose_time")
        search.send_keys(self.searchkey)
        
        #輸入search key 後等待自動資料自動載入
        WebDriverWait(self.airport,5).until(    
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'ul#print li div ul'))    
        )
        
    def fix_one_page_data(self):   
        apply_time = self.airport.find_elements(By.CLASS_NAME,"note")
        
        terminals = self.airport.find_elements(By.CSS_SELECTOR,"div.color.sm_f p")
        for i in terminals:
            #加入航班時間    
            self.data["apply_time"].append(apply_time[0].text)
            self.data["terminal"].append(i.text)
            
        flight_informations = self.airport.find_elements(By.CSS_SELECTOR,"ul#print li div ul")
        
        for i in flight_informations:
            
            info = i.find_elements(By.TAG_NAME,"li")  #尋找裡面的li
            contents = []
            for j in info:
                contents.append(j.text)
            
            self.data["flight_informations"].append(contents)
            
        contains = self.airport.find_elements(By.CSS_SELECTOR,"p.sm_f")
        
        temp = 0
        for i in contains:
            if temp % 3 == 0:
                self.data["location"].append(i.text)
            elif temp % 3 == 1:
                self.data["departure_time"].append(i.text)
            else:
                self.data["arrival_time"].append(i.text)
            temp += 1   
        
        weekdays = self.airport.find_elements(By.CSS_SELECTOR,"div.date")
        
        week = ""
        temp2 = 1
        
        for i in weekdays:
            
            try:
                item = i.find_element(By.CSS_SELECTOR,"p")
                
                if item.get_attribute("class") == "yes":
                    week += str(temp2)
            except:
                item = None
                            
            if temp2 % 7 == 0:
                self.data["weekdays"].append(week)
                temp2 = 1
                week = ""
                continue;
                
            temp2 += 1
            
        
        for k,value in self.data.items():
            print(len(value))
            
        
        # self.fix_data_change()  #資料第一正規化
        # print(self.normalized_data)
        # print(len(self.normalized_data))
        
    def fix_data_change(self):
            
        self.normalized_data = []    
        for ap,t,fs,l,d,a,w in zip(self.data["apply_time"],self.data["terminal"],self.data["flight_informations"],self.data["location"],self.data["departure_time"],self.data["arrival_time"],self.data["weekdays"]):
            
            for f in fs:
                f = f.split(" ")
                row = {
                    "apply_time":ap,
                    "terminal":t,
                    "airline":f[0],
                    "air_NO":f[1],
                    "location":l,
                    "departure_time":d,
                    "arrival_time":a,
                    "weekdays":w,
                }
                
                self.normalized_data.append(row)
        
        df = pd.DataFrame(self.normalized_data)
        print(df)
        
    def fix_next_page(self):
        
        try:
            pages = self.airport.find_elements(By.CSS_SELECTOR,"p.container.page a")
        except:
            print("no next_page")
        
        
        for i in range(1,len(pages)-2): 
            pages[i].click()
            
            WebDriverWait(self.airport,5).until(    
                expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'ul#print li div ul'))    
            )
            
            self.fix_one_page_data()
            
        self.fix_data_change()
        
    def fix_next_week(self):
        
       next_week = self.airport.find_elements(By.CSS_SELECTOR,"p.right_now a")
       next_week[1].click()
       
       WebDriverWait(self.airport,5).until(    
           expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'ul#print li div ul'))    
       )
       
       
       
       
       
air = TaoyuanAirport()
air.fix_data_input("日本")
air.fix_one_page_data()
air.fix_next_page()
air.fix_next_week()
time.sleep(5)
air.quit()
     
        