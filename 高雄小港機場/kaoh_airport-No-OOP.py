from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions
import pandas as pd
import time

airport = webdriver.Chrome()       #使用google webdriver 控制瀏覽器
airport.get('https://www.kia.gov.tw/PeriodicalScheduleC001210.aspx') #瀏覽器連結網址
japan_airport = ["成田","琉球","高松",'福岡','靜岡','關西']
flight_data = {"company":[],"air_no":[],"air_type":[],"location":[],"departure_time":[],"arrival_time":[],"week_day":[]}

def fix_next_page():     #判斷下一頁是某存在於網頁中  
        
        try:    
            airport.find_element(By.ID,"ctl00_ContentPlaceHolder1_ucPeriodicalSchedule1_ucPager1_aLinkNextPage").click()
            return True
        except:
            return False
    
def fixed_flight_data():
            
    for location in japan_airport:    
        selection = Select(airport.find_element(By.CLASS_NAME,"terminal"))   #定位下拉選單
        selection.select_by_visible_text(location)                   #選擇目的地 
    
        airport.find_element(By.CSS_SELECTOR,"input[value='搜尋']").click()   #控制瀏覽器點搜尋
        fix_one_page_data()     #單頁抓取
        
        while fix_next_page() == True:   #如果下一頁存在 就繼續按
            fix_one_page_data()    #第二頁以上循環抓取

def fix_one_page_data():   #得到定期航班資訊單頁
        
    flight = airport.find_elements(By.CLASS_NAME,"sd_tr")  #找到class="sd_tr"
    
    for i in range(len(flight)):
        if i == 0:
            continue
        a = flight[i].text.split(" ")
        b = a[0].split("\n")
        row = b+a[1:]
                    
        for key,j in zip(flight_data.keys(),row[:-7]):
            flight_data[key].append(j)
        
        row_day = row[-7:]
        
        days=""
        for index in range(len(row_day)):    #日:0,一:1 依此類推
            if row_day[index] == "Y":
                days += str(index)
        flight_data["week_day"].append(days)

def to_df(data):
        
        df = pd.DataFrame(data)
        return df

if __name__ == "__main__":  

    fixed_flight_data()
    df = to_df(flight_data)
    print(df)
    time.sleep(5)
    airport.quit()