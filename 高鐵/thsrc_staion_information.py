# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:05:52 2023

@author: USER
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from thsrc_index_search import Station
import time
import pandas as pd
class Station_time_data(Station):
    
    def __init__(self, departure, location):
        super().__init__(departure, location)
        
        
    def search_railway_north_time_data(self):
        
        self.north={
                 "car_type":[],
                 "station":[],
                 "arrival":[],
                 "go_away":[],
            }
        
        if self.find_railway_station(): 
            
            head = self.browser.find_element(By.CSS_SELECTOR,"thead.border-bottom tr")
            self.title = head.text.split()
            
            body = self.browser.find_elements(By.CSS_SELECTOR,"tbody#northBound tr")
            for i in body:
                info = i.text.split(" ")     #存取北上台鐵資訊
                if len(info) == 6:
                    self.north['car_type'].append(info[0])
                    self.north['station'].append(info[1]+info[2]+info[3])
                    self.north['arrival'].append(info[4])
                    self.north['go_away'].append(info[5])
                
                elif len(info)==7:
                    self.north['car_type'].append(info[0]+info[1])
                    self.north['station'].append(info[2]+info[3]+info[4])
                    self.north['arrival'].append(info[5])
                    self.north['go_away'].append(info[6])
    
    def search_railway_south_time_data(self):
        
        self.south={
                "car_type":[],
                "station":[],
                "arrival":[],
                "go_away":[],
            }
        
        if self.find_railway_station(): 
            
            self.browser.find_element(By.CSS_SELECTOR,"a[title='南下']").click()
            
            head = self.browser.find_element(By.CSS_SELECTOR,"thead.border-bottom tr")
            self.title = head.text.split()
            
            time.sleep(0.2)   #webdriverwait 失效強制等待(資料顯示來源來自非js,來自台鐵)
            
            body = self.browser.find_elements(By.CSS_SELECTOR,"tbody#southBound tr")
            
            for i in body:
                info = i.text.split(" ")     #存取北上台鐵資訊
                if len(info) == 6:
                    self.south['car_type'].append(info[0])
                    self.south['station'].append(info[1]+info[2]+info[3])
                    self.south['arrival'].append(info[4])
                    self.south['go_away'].append(info[5])
                
                elif len(info)==7:
                    self.south['car_type'].append(info[0]+info[1])
                    self.south['station'].append(info[2]+info[3]+info[4])
                    self.south['arrival'].append(info[5])
                    self.south['go_away'].append(info[6])
    
    def north_to_csv(self,filename):
        
            self.north_to_df().to_csv("{}.csv".format(filename),encoding="utf-8-sig")
                       
    def south_to_csv(self,filename):
            
            self.south_to_df().to_csv("{}.csv".format(filename),encoding="utf-8-sig")
        
    def north_to_df(self):
        
        if self.north["car_type"]:
            
            self.df_north = pd.DataFrame(self.north)
            self.df_north.columns = self.title
            return self.df_north
            
    def south_to_df(self):
         
         if self.south["car_type"]:            
            self.df_south = pd.DataFrame(self.south)
            self.df_south.columns = self.title
            return self.df_south
        
    def data_renew_time(self):
        
        renew = self.browser.find_element(By.ID,"trainUpdateTime")
        renewtime = renew.text
        renewtime = renewtime.split("\n")[1]
        return renewtime
        
            