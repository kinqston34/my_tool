# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 15:14:24 2023

@author: USER   
"""
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from thsrc_index_search import Thsrc_index_search
import pandas as pd

class Thsrc_search(Thsrc_index_search):
    
    def __init__(self,departure,location,mode,departure_day,departure_time,location_day,location_time,discount=False): 
        
        super().__init__(departure,location,mode,departure_day,departure_time,location_day,location_time,discount)
        super().index_insert_key()
        
        self.data = {                        #回程
                "departure_time":[],    #出發時間
                "travel_time":[],       #行車時間
                "arrival_time":[],      #抵達時間
                "train_number":[],      #車次
                "free_seat_car":[],     #自由座車廂
                }
        
        self.data2 = {                       #去程
                "return_time":[],       #出發時間 
                "travel_time":[],       #行車時間
                "arrival_time":[],      #抵達時間
                "train_number":[],      #車次
                "free_seat_car":[],     #自由座車廂
                }
        
        if discount == False:                      #如果都沒有點選優惠 設定預設值為1
            self.temp = 1
        else:
            self.temp = len(self.discount)
            
        for i in range(self.temp):
            self.data["favor{}".format(i)]=[]
            self.data2["favor{}".format(i)]=[]      #生成優惠欄位
    
    def get_data(self):
        return self.data,self.data2
    
    def quit(self):                  #browser.quit
        self.browser.quit()
    
    def data_to_csv(self):
        self.all_insert()
        title = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-01 div.tr-table div.tr-thead div.tr-td")
        cols = []
        for i in title[:-1]:
            cols.append(i.text)
        
        dp = pd.DataFrame(self.data)
        dp.columns = cols
        dp.to_csv("thsrc_departure_result.csv",encoding="utf-8-sig")
        rp = pd.DataFrame(self.data2)
        rp.columns = cols
        rp.to_csv("thsrc_return_result.csv",encoding="utf-8-sig")
    
    def price_to_csv(self):
        df = self.search_car_price()
        df.to_csv("thsrc_search_price.csv",encoding="utf-8-sig")
        
    def departure_next_result(self):
    
        try:
            self.browser.find_element(By.CSS_SELECTOR,"a#ttab-01_nextPage i.kyicon-arrow_forward").click()
        
            WebDriverWait(self.browser, 10).until(          #等待主頁回應，搜尋框未出來前，會無法執行以下動作
                expected_conditions.presence_of_element_located((By.CLASS_NAME,'tr-row'))
            )
            
            return True
        
        except:
            return False
        
        
    def departure_first_result_insert(self):       #第一頁查詢
        
        dt_at = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-01 div.tr-table div#timeTableTrain_S a.tr-row div.tr-td span.font-16r.darkgray")
        tt = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-01 div.tr-table div#timeTableTrain_S a.tr-row div.tr-td div.traffic-time p")
        tn = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-01 div.tr-table div#timeTableTrain_S a.tr-row div.tr-td.train")
        fsc = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-01 div.tr-table div#timeTableTrain_S a.tr-row div.tr-td.car") 
        
        # eb = browser.find_elements(By.CSS_SELECTOR,"p.toffer-text span")     #優惠欄位 (查詢時如果有點選優惠才會新增)
        # r = browser.find_elements(By.CSS_SELECTOR,"div.tr-td.hidden-s")      #備註欄位
        
        for i in range(len(dt_at)):     #insert data
            if i % 2 == 0:
                self.data["departure_time"].append(dt_at[i].text)
            else:
                self.data["arrival_time"].append(dt_at[i].text)
            
    
        for a,b,c in zip(tt,tn,fsc):
            self.data["travel_time"].append(a.text)
            self.data["train_number"].append(b.text)
            self.data["free_seat_car"].append(c.text)
    
    def departur_forward_result_insert(self):        #往後查詢
        
        dt_at = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-01 div.tr-table div#timeTableTrain_ a.tr-row div.tr-td span.font-16r.darkgray")
        tt = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-01 div.tr-table div#timeTableTrain_ a.tr-row div.tr-td div.traffic-time p")
        tn = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-01 div.tr-table div#timeTableTrain_ a.tr-row div.tr-td.train")
        fsc = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-01 div.tr-table div#timeTableTrain_ a.tr-row div.tr-td.car") 
    
        # eb = browser.find_elements(By.CSS_SELECTOR,"p.toffer-text span")     #優惠欄位 (查詢時如果有點選優惠才會新增)
        # r = browser.find_elements(By.CSS_SELECTOR,"div.tr-td.hidden-s")      #備註欄位
        
        for i in range(2,len(dt_at)):     #第一筆重複拿掉
            if i % 2 == 0:
                self.data["departure_time"].append(dt_at[i].text)
            else:
                self.data["arrival_time"].append(dt_at[i].text)
            
    
        for a,b,c in zip(tt[1:],tn[1:],fsc[1:]):
            self.data["travel_time"].append(a.text)
            self.data["train_number"].append(b.text)
            self.data["free_seat_car"].append(c.text)
    
    def departure_first_discount_insert(self):
        
        favor = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-01 div.tr-table div#timeTableTrain_S a.tr-row div.tr-td.hidden-s p.toffer-text span")
        
        for j in range(self.temp):
            for i in range(len(favor)):
                if i % self.temp == j:
                    self.data["favor{}".format(j)].append(favor[i].text)
        
    
    def departure_forward_discount_insert(self):
        
        favor = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-01 div.tr-table div#timeTableTrain_ a.tr-row div.tr-td.hidden-s p.toffer-text span")
    
        for j in range(self.temp):
            for i in range(len(favor)):
                if i == 0:
                    continue
                if i % self.temp == j:
                    self.data["favor{}".format(j)].append(favor[i].text)
        
    def departure_insert_all(self):                       #將搜尋結果全部insert data
        self.departure_first_result_insert()
        self.departure_first_discount_insert()
        while self.departure_next_result() == True:
            self.departur_forward_result_insert()
            self.departure_forward_discount_insert()
        
        # else:
        #     print("最後一頁不能再按了")
    #------------------------------------------------------------#
    
    def return_next_result(self):
    
        try:
            self.browser.find_element(By.CSS_SELECTOR,"a#ttab-02_nextPage i.kyicon-arrow_forward").click()
        
            WebDriverWait(self.browser, 10).until(          #等待主頁回應，搜尋框未出來前，會無法執行以下動作
                expected_conditions.presence_of_element_located((By.CLASS_NAME,'tr-row'))
            )
            
            return True
        
        except:
            return False
        
        
    def return_first_result_insert(self):       #第一頁查詢
        
        dt_at = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-02 div.tr-table div#timeTableTrain_R a.tr-row div.tr-td span.font-16r.darkgray")
        tt = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-02 div.tr-table div#timeTableTrain_R a.tr-row div.tr-td div.traffic-time p")
        tn = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-02 div.tr-table div#timeTableTrain_R a.tr-row div.tr-td.train")
        fsc = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-02 div.tr-table div#timeTableTrain_R a.tr-row div.tr-td.car") 
        
        # eb = browser.find_elements(By.CSS_SELECTOR,"p.toffer-text span")     #優惠欄位 (查詢時如果有點選優惠才會新增)
        # r = browser.find_elements(By.CSS_SELECTOR,"div.tr-td.hidden-s")      #備註欄位
        
        for i in range(len(dt_at)):     #insert data
            if i % 2 == 0:
                self.data2["return_time"].append(dt_at[i].text)
            else:
                self.data2["arrival_time"].append(dt_at[i].text)
            
    
        for a,b,c in zip(tt,tn,fsc):
            self.data2["travel_time"].append(a.text)
            self.data2["train_number"].append(b.text)
            self.data2["free_seat_car"].append(c.text)
    
    def return_forward_result_insert(self):        #往後查詢
        
        dt_at = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-02 div.tr-table div#timeTableTrain_ a.tr-row div.tr-td span.font-16r.darkgray")
        tt = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-02 div.tr-table div#timeTableTrain_ a.tr-row div.tr-td div.traffic-time p")
        tn = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-02 div.tr-table div#timeTableTrain_ a.tr-row div.tr-td.train")
        fsc = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-02 div.tr-table div#timeTableTrain_ a.tr-row div.tr-td.car") 
    
        # eb = browser.find_elements(By.CSS_SELECTOR,"p.toffer-text span")     #優惠欄位 (查詢時如果有點選優惠才會新增)
        # r = browser.find_elements(By.CSS_SELECTOR,"div.tr-td.hidden-s")      #備註欄位
        
        for i in range(2,len(dt_at)):     #第一筆重複拿掉
            if i % 2 == 0:
                self.data2["return_time"].append(dt_at[i].text)
            else:
                self.data2["arrival_time"].append(dt_at[i].text)
            
    
        for a,b,c in zip(tt[1:],tn[1:],fsc[1:]):
            self.data2["travel_time"].append(a.text)
            self.data2["train_number"].append(b.text)
            self.data2["free_seat_car"].append(c.text)
        
    def return_first_discount_insert(self): 
        
        favor = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-02 div.tr-table div#timeTableTrain_R a.tr-row div.tr-td.hidden-s p.toffer-text span")
        
        for j in range(self.temp):
            for i in range(len(favor)):
                if i % self.temp == j:
                    self.data2["favor{}".format(j)].append(favor[i].text)
            

    def return_forward_discount_insert(self):
        
        favor = self.browser.find_elements(By.CSS_SELECTOR,"div#ttab-02 div.tr-table div#timeTableTrain_ a.tr-row div.tr-td.hidden-s p.toffer-text span")
        
        for j in range(self.temp):
            for i in range(len(favor)):
                if i == 0:
                    continue
                if i % self.temp == j:
                    self.data2["favor{}".format(j)].append(favor[i].text)
        
        
    def return_insert_all(self):                       #將搜尋結果全部insert data
        self.return_first_result_insert()
        self.return_first_discount_insert()
        while self.return_next_result() == True:
            self.return_forward_result_insert()
            self.return_forward_discount_insert()
        # else:
        #     print("最後一頁不能再按了")
#----------------------------------------------------------#    
    def train_overnight_insert(self):       #過夜車
        try :
            #去程過夜車
            self.browser.find_element(By.CSS_SELECTOR,"div#timeTableTrain_S a.tr-row.overnight") 
        except NoSuchElementException :
            print("no overnight train in departure way")
            d_overnight = False
        else:
            d_overnight = {
                        "departure_time":[],    #出發時間
                        "travel_time":[],       #行車時間
                        "arrival_time":[],      #抵達時間
                        "train_number":[],      #車次
                        "free_seat_car":[],     #自由座車廂
                        }
            
            dt = self.browser.find_elements(By.CSS_SELECTOR,"div#timeTableTrain_S a.tr-row.overnight div.tr-td.tr-overnight span.font-16r.darkgray")
            at = self.browser.find_elements(By.CSS_SELECTOR,"div#timeTableTrain_S a.tr-row.overnight div.tr-td span.font-16r.darkgray")
            tt = self.browser.find_elements(By.CSS_SELECTOR,"div#timeTableTrain_S a.tr-row.overnight div.tr-td div.traffic-time p")
            tn = self.browser.find_elements(By.CSS_SELECTOR,"div#timeTableTrain_S a.tr-row.overnight div.tr-td.train")
            fsc = self.browser.find_elements(By.CSS_SELECTOR,"div#timeTableTrain_S a.tr-row.overnight div.tr-td.car")
            
            for i,j in zip(dt,at):
                d_overnight["departure_time"].append(i.text)
                d_overnight["arrival_time"].append(j.text)
            
            for a,b,c in zip(tt,tn,fsc):
                d_overnight["travel_time"].append(a.text)
                d_overnight["train_number"].append(b.text)
                d_overnight["free_seat_car"].append(c.text)
                
        try :
            #回程過夜車
            self.browser.find_element(By.CSS_SELECTOR,"div#timeTableTrain_R a.tr-row.overnight")  
        except NoSuchElementException :
            print("no overnight train in return way")
            r_overnight = False
        else:
            r_overnight = {
                        "return_time":[],    #出發時間
                        "travel_time":[],       #行車時間
                        "arrival_time":[],      #抵達時間
                        "train_number":[],      #車次
                        "free_seat_car":[],     #自由座車廂
                        }
            
            dt = self.browser.find_elements(By.CSS_SELECTOR,"div#timeTableTrain_R a.tr-row.overnight div.tr-td.tr-overnight span.font-16r.darkgray")
            at = self.browser.find_elements(By.CSS_SELECTOR,"div#timeTableTrain_R a.tr-row.overnight div.tr-td span.font-16r.darkgray")
            tt = self.browser.find_elements(By.CSS_SELECTOR,"div#timeTableTrain_R a.tr-row.overnight div.tr-td div.traffic-time p")
            tn = self.browser.find_elements(By.CSS_SELECTOR,"div#timeTableTrain_R a.tr-row.overnight div.tr-td.train")
            fsc = self.browser.find_elements(By.CSS_SELECTOR,"div#timeTableTrain_R a.tr-row.overnight div.tr-td.car")
            
            for i,j in zip(dt,at):
                r_overnight["return_time"].append(i.text)
                r_overnight["arrival_time"].append(j.text)
                
            for a,b,c in zip(tt,tn,fsc):
                r_overnight["travel_time"].append(a.text)
                r_overnight["train_number"].append(b.text)
                r_overnight["free_seat_car"].append(c.text)
            
        return d_overnight,r_overnight
                        
    #------------------------------------------------------------#
        
    def search_car_price(self):                 #找票價
        
        prices = self.browser.find_elements(By.TAG_NAME,"tr")
        ticket_type = prices[0].text.split(" ")
        
        car_type = []
        price = []
        for i in prices[1:]:
            car_type.append(i.text.split(" ")[0])
            price.append(i.text.split(" ")[1:])
                
        df = pd.DataFrame(price,index=car_type,columns=ticket_type)
        print("{} <---> {}".format(self.departure,self.location))
        return df
    
    #------------------------------------------------------------#
    def all_insert(self):           #呼叫方法insert 所選的mode
        
        if self.mode == "單程":    
            self.departure_insert_all()
        elif self.mode == "去回程":
            self.departure_insert_all()
            self.return_insert_all()
    
    