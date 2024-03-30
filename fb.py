# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 17:07:37 2023

@author: USER
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

import time
class Facebook():
    def __init__(self,email,password):
        #關閉瀏覽器權限選項 
        options = webdriver.ChromeOptions()
        
        prefs = {
                'profile.default_content_setting_values':{
                    'notifications': 2    
                }
            }
        options.add_experimental_option('prefs',prefs)
        self.browser = webdriver.Chrome(options=options)
        self.browser.get("https://www.facebook.com/")
        self.browser.find_element(By.ID,"email").send_keys(email)
        self.browser.find_element(By.ID,"pass").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR,"button[name='login']").click()
        
        self.browser.find_element(By.CSS_SELECTOR,"div.xi81zsa.x1lkfr7t.xkjl1po.x1mzt3pk.xh8yej3.x13faqbe").click()
        
        WebDriverWait(self.browser,10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"p.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8"))
            )
    
    def postmessage(self):

        # 發文權限
        self.browser.find_element(By.CSS_SELECTOR,"span.xw3qccf.xeaf4i8").click() #按下發文中的權限設定
        # time.sleep(2)
        # body = self.browser.find_element(By.CSS_SELECTOR,"div[role='radiogroup']")
        # print("現在的body:",body.get_attribute("innerHTML"))

        time.sleep(10)
        ele = self.browser.find_element(By.CSS_SELECTOR,"div.xu06os2.x1ok221b")  #只限本人 div
        self.browser.execute_script("arguments[0].scrollIntoView(true);",ele)   #滾本人選項可見
        
        # ele.click()
        

        print("到此ok")

        # WebDriverWait(self.browser,10).until(
        #     expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft"))
        # )
        # self.browser.find_element(By.CSS_SELECTOR,"span.x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft").click() #按下完成
        # print("到此ok")
        # self.browser.find_element(By.CSS_SELECTOR,"p.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8 br").send_keys("您好<br>hello")
        
    def quit(self):
        self.browser.quit()
            
        
        
f = Facebook("aa37741867@gmail.com","kingston0000")
f.postmessage()
time.sleep(30)
f.quit()        
    