# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 13:58:08 2023

@author: USER
"""
import time
from TR_index import TR_index
from selenium.webdriver.common.by import By
import pandas as pd


class TR_search(TR_index):
    
    def __init__(self,start, end,query,day,start_time,end_time,transfer_condition = False):
        super().__init__(start,end,query,day,start_time,end_time)
        super().search_insert()
        super().query_click()
        
        self.transfer_c = transfer_condition
        self.data ={
                "train":[],             #車種車次 (始發站 → 終點站)
                "departure_time":[],    #出發時間
                "arrival_time":[],      #抵達時間
                "trip_time":[],         #行駛時間
                "via":[],               #經由
                "normal_ticket":[],     #全票
                "child_ticket":[],      #孩童票
                "old_ticket":[],        #敬老票
                "remark":[],
            }
        
    def quit(self):
        self.browser.quit()
    
    def search_result(self):
        
        data_num = len(self.browser.find_elements(By.CSS_SELECTOR,"tr.trip-column"))

        td = self.browser.find_elements(By.CSS_SELECTOR,"tr.trip-column td")
        for i in range(data_num):
            self.data["train"].append(td[10*i].text)
            self.data["departure_time"].append(td[10*i+1].text)
            self.data["arrival_time"].append(td[10*i+2].text)
            self.data["trip_time"].append(td[10*i+3].text)
            self.data["via"].append(td[10*i+4].text)
            self.data["normal_ticket"].append(td[10*i+6].text)
            self.data["child_ticket"].append(td[10*i+7].text)
            self.data["old_ticket"].append(td[10*i+8].text)
        
        self.browser.find_element(By.ID,"toggleAllTableBtn").click()  #處理備註
        remark = self.browser.find_elements(By.CSS_SELECTOR,"td.symbol")
        for i in remark:
             img = i.find_elements(By.CSS_SELECTOR,"img")
             span = i.find_element(By.CSS_SELECTOR,"span")
             s = ""
             for j in img:
                 s += j.get_attribute("title")+","
             s += span.text
             self.data["remark"].append(s)
             
        del td,img,span,s
        
    def to_df(self):
        self.df = pd.DataFrame(self.data)
        # print(self.df.head())
        return self.df
    
    def to_csv(self):
        
        th = self.browser.find_elements(By.TAG_NAME,"Th")
        title = []
        for i in th[:9]:
            title.append(i.text)
        
        self.to_df().columns = title
        self.to_df().to_csv("TR_search_result.csv",encoding="utf-8-sig")
        
        del th,title
       
    def search_insert(self):     #新增條件查詢 
        
        if self.transfer_c == "1":      #接受轉乘
            self.browser.find_element(By.CSS_SELECTOR,"label[for=option2]").click()
        elif self.transfer_c == "2":    #指定轉乘
            self.browser.find_element(By.CSS_SELECTOR,"label[for=option3]").click()
    

tr = TR_search("臺中","新竹","0","20231211","08:00","23:59","1")
tr.search_insert()
# tr.search_result()
# tr.to_csv()
time.sleep(10)
tr.quit()

        
        
    
        