# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:26:48 2023

@author: USER
"""
import time
from thsrc_time_data import Thsrc_search
from thsrc_index_search import Station
from thsrc_staion_information import Station_time_data
        
# thsrc = Thsrc_search("嘉義","台北","去回程","2023.12.10","15:00","2023.12.11","15:00")
# thsrc.all_insert()

sta = Station_time_data("嘉義","台北")

sta.search_railway_north_time_data()
sta.search_railway_south_time_data()
sta.north_to_csv("台北北上")
sta.south_to_csv("台北南下")
# sta.north_to_csv()
# print(sta.north_to_df().head())
# sta.south_to_csv()
# print(sta.south_to_df().head())
# print(sta.south['go_away'])
# print(sta.north['go_away'])


# d,t = thsrc.get_data()
# print(d,t)
# thsrc.price_to_csv()
# df = thsrc.search_car_price()
# print(df)



time.sleep(10)
sta.browser.quit()