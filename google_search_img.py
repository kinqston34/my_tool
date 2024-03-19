# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:46:01 2024

@author: Kingston
"""

import os
import sys
import requests
import re
import base64
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

class GoogleSearchImg():

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://www.google.com/imghp?hl=zh-TW&ogbl")
        self.browser.maximize_window()

    def quit(self):
        self.browser.quit() 

    def search(self,key,crab_num):

        self.browser.find_element(By.CLASS_NAME,"gLFyf").send_keys(key)
        self.browser.find_element(By.CLASS_NAME,"Tg7LZd").click()

        if self.no_search_result():  # False: 查詢有結果 , True: 查詢無果
            print("沒有相符的搜尋結果")
            return

        try:           #是否有找到該img元素
            WebDriverWait(self.browser, 10).until(                      
                    expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"img.Q4LuWd"))
                )
            
        except TimeoutException:
            self.quit()
            os.system("python google_search_img.py {} {}".format(key,crab_num))
            sys.exit()

        next = True
        while next:
            next = self.more_result(crab_num)

    def more_result(self,crab_num): #更多結果
        
        try:      #尋找有無其餘搜尋結果
            other_result_none = self.browser.find_element(By.CLASS_NAME,"w9dUj")   
            # print(other_result_none.text) #確定元素存在
        
        except NoSuchElementException:   #還有其他搜尋結果存在沒有被展開
            
            other_result = self.browser.find_element(By.CSS_SELECTOR,"input.LZ4I")
            # print(other_result.get_attribute("value")) #確定元素存在

            while not other_result.is_displayed():
                count = 0
                imgs = self.browser.find_elements(By.CSS_SELECTOR,"img.Q4LuWd")
                # print("imgs:", len(imgs))
                for img in imgs:
                    if img.get_attribute("src") != None :
                        count += 1
                    else:
                        break
                if count > crab_num:  # 當指定抓取數量已經足夠時，不用執行向下
                    print("count:",count)
                    print("crab_num",crab_num)
                    break    
                self.browser.execute_script("window.scrollBy(0,1000)")
                time.sleep(1.5)   

                WebDriverWait(self.browser, 10).until(
                    expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"img.Q4LuWd"))
                ) 

            if other_result.is_displayed() and count < crab_num:   #如果 "顯示更多結果" 可見，設定接下來動作
                other_result.click()
                return True
                # ActionChains(self.browser).scroll_to_element(other_result).perform()
        self.crab()
        return False
             
    def crab(self):   #爬取
        imgs = self.browser.find_elements(By.CSS_SELECTOR,"img.Q4LuWd")
        print("查詢結果: {}張".format(len(imgs)))
        i = 1
        for img in imgs:
            url = img.get_attribute("src")
            # print("{} src : {}".format(i,url))   #列印url
            # print()
            self.download(url,i)            #下載圖片到img資料中 (原路徑底下)
            if i == crab_num :
                break 
            i+=1

    def download(self,url,index):  #下載 
        dirs = "img"
        if os.path.exists(dirs) == False:
            os.makedirs("./img/")
        
        if url == None:  
            # url == None
            return    
        elif re.match(r"^data:image",url):
            # url= data:image:
            url_base64_str = url.split(",")[1]      # 擷取 base64 編碼部分
            img = base64.b64decode(url_base64_str)
            with open("./img/{}.jpg".format(index),"wb") as f:
                f.write(img)
        else:
        # url= http://
            res = requests.get(url)  #處理http 網址
            if res.status_code == 200:
                with open("./img/{}.jpg".format(index),"wb") as f:
                    f.write(res.content)

    def no_search_result(self):  #判斷查詢有無結果
        try:
            no_result = self.browser.find_element(By.CLASS_NAME,"Zd9MXe")
        except:
            return False
        else:
            if no_result.text == "沒有相符的搜尋結果":
                return True
            
if __name__ == "__main__":
    if len(sys.argv) == 3:
        key = sys.argv[1]
        crab_num = int(sys.argv[2])
    else:
        key = input("請輸入想要搜尋的關鍵字: ")
        crab_num = int(input("請輸入想要下載幾張照片: "))
    
    start = time.time()
    google_img = GoogleSearchImg()
    google_img.search(key,crab_num)
    end = time.time()
    print("程式完成，執行時間差:",end - start)
    time.sleep(30)
    google_img.quit()


    