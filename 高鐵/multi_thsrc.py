# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:09:51 2023

@author: USER
"""
import time
from concurrent.futures import ThreadPoolExecutor
from thsrc_time_data import Thsrc_search 

def job(d,l):
    thsrc = Thsrc_search(d,l,"去回程","2023.12.10","15:00","2023.12.11","15:00")
    df = thsrc.search_car_price()
    print(df)
    thsrc.quit()
    return "job is finish"
    
def main():
    executor = ThreadPoolExecutor(5)
    x = ["左營","台南","嘉義","雲林","彰化","台中","苗栗","新竹","南港","桃園","板橋","台北","南港"]
    
    f1 = executor.submit(job,x[0],x[2])
    f2 = executor.submit(job,x[4],x[12])
    f3 = executor.submit(job,x[3],x[11])
    f4 = executor.submit(job,x[10],x[1])
    f5 = executor.submit(job,x[6],x[8])
    
    t = 0
    for i in range(3):
        print("the time is {}s".format(t+i*15))
        time.sleep(15)
        
        if f1.done():
            print(f1.result())
            print("f1 finish")
        
        if f2.done():
            print(f2.result())
            print("f2 finish")
    
        if f3.done():
            print(f3.result())
            print("f3 finish")
            
        if f4.done():
            print(f4.result())
            print("f4 finish")
            
        if f5.done():
            print(f5.result())
            print("f5 finish")
main()
        