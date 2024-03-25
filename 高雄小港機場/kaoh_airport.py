# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:46:34 2024

@author: USER
"""

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions
import pandas as pd
import time

class Kaohslung_airport():
    
    def __init__(self):
        self.airport = webdriver.Chrome()       #使用google webdriver 控制瀏覽器
        self.airport.get('https://www.kia.gov.tw/PeriodicalScheduleC001210.aspx') #瀏覽器連結網址
        self.japan_airport = ["成田","琉球","高松",'福岡','靜岡','關西']    #高雄國際機場提供的日本機場選項
        
    def quit(self):
        return self.airport.quit()     #定義關閉瀏覽器
        
    def fix_one_page_data(self):   #得到定期航班資訊單頁
        
        flight = self.airport.find_elements(By.CLASS_NAME,"sd_tr")
        
        for i in range(len(flight)):
            if i == 0:
                continue
            self.a = flight[i].text.split(" ")
            self.b = self.a[0].split("\n")
            self.row = self.b+self.a[1:]
                        
            for key,j in zip(self.flight_data.keys(),self.row[:-7]):
                self.flight_data[key].append(j)
            
            self.row_day = self.row[-7:]
            
            self.days=""
            for index in range(len(self.row_day)):    #日:0,一:1 依此類推
                if self.row_day[index] == "Y":
                    self.days += str(index)
            self.flight_data["week_day"].append(self.days)
                    
        # print(self.flight_data)
    
        
    def fix_next_page(self):  
        
        try:    
            self.airport.find_element(By.ID,"ctl00_ContentPlaceHolder1_ucPeriodicalSchedule1_ucPager1_aLinkNextPage").click()
            return True
        except:
            return False
                    
    def to_df(self,data):
        
        self.df = pd.DataFrame(data)
        return self.df
        
    
    def fixed_flight_data(self):
        
        self.flight_data = {"company":[],"air_no":[],"air_type":[],"location":[],"departure_time":[],"arrival_time":[],"week_day":[]}
        
        # print(self.flight_data)
        for location in self.japan_airport:    
            selection = Select(self.airport.find_element(By.CLASS_NAME,"terminal"))   #定位下拉選單
            selection.select_by_visible_text(location)                   #選擇目的地 
        
            self.airport.find_element(By.CSS_SELECTOR,"input[value='搜尋']").click()   #控制瀏覽器點搜尋
            self.fix_one_page_data()
            
            while self.fix_next_page() == True:
                self.fix_one_page_data()

    def fixed_flight_data_updatetime(self):
        update = self.airport.find_element(By.CSS_SELECTOR,"div.schdeule_date_info.clearfix p span")
        return(update.text)
    
# 單檔案測試用 沒有要用請註解以下
if __name__ == "__main__":  
    air = Kaohslung_airport()
    air.fixed_flight_data()
    update = air.fixed_flight_data_updatetime()
    print("資料更新時間:",update)

    df = air.to_df(air.flight_data)
    print(df)

    time.sleep(5)
    air.quit()
    
    

    