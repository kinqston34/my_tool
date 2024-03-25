# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:35:59 2023

@author: USER
"""
import time
from index import index_choose
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

def find_trival_item(browser,t,h,p):
    
    titles = browser.find_elements(By.CSS_SELECTOR,"span.caption--mphmX")
    hrefs = browser.find_elements(By.CSS_SELECTOR,"a.cardsList--2cG2D")
    prices = browser.find_elements(By.CSS_SELECTOR,"span.price--Ip0QE")
    
    for title,href,price in zip(titles,hrefs,prices):
        t.append(title.text)
        h.append(href.get_attribute("href"))
        p.append(price.text)
    
def next_result_page(browser):
    
    next_result_page = browser.find_elements(By.CSS_SELECTOR,"li.Style__StyledPageStyle-sc-17tz2cz-1.kGjiOf.page.next")
    next_result_page[1].click()
    WebDriverWait(browser, 10).until(          #等待新頁面回應
        expected_conditions.presence_of_element_located((By.CLASS_NAME,'caption--mphmX'))
    )
    
def search_result():
    
    browser = index_choose() #獲取查詢後頁面控制權

    # print(browser.current_url) 
    WebDriverWait(browser, 10).until(          #等待新頁面回應
        expected_conditions.presence_of_element_located((By.CLASS_NAME,'caption--mphmX'))
    )
    
    t = []
    h = []
    p = []

    final = browser.find_elements(By.CSS_SELECTOR,"ul.Style__StyledPagination-sc-17tz2cz-0.bNVpik.Pagination.ld-pagination.pageBar--1jXsj li.Style__StyledPageStyle-sc-17tz2cz-1.kGjiOf.page")
    final_page_num = len(final)-2
    current_page = 1

    while current_page <= final_page_num:
        find_trival_item(browser,t,h,p)
        if current_page != final_page_num:
            next_result_page(browser)
        current_page += 1        
    
    data = {"旅遊行程":t,"報名網址":h,"行程金額(人/起)":p}
    
    print("搜尋結果有{}頁".format(final_page_num))
    print("總共有旅遊行程: {}".format(len(t)))
    
    df = pd.DataFrame(data)
    print(df)
    
    return browser  


# browser = index_choose() #獲取查詢後頁面控制權

# # print(browser.current_url) 
# WebDriverWait(browser, 10).until(          #等待新頁面回應
#     expected_conditions.presence_of_element_located((By.CLASS_NAME,'caption--mphmX'))
# )

# search_result()

# time.sleep(5)
# browser.quit()