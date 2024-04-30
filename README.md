# my_tool
use python create tool

# os
使用os 套件範例

## os.py test.py
os.py write code into test.py , then run test.py
## sys_argv.py
test input use sys_argv

# decorator 
## decorator.py 
decorator test case

# unittest
unittest 套件範例
## subTest.py
使用subTest 測試loop 錯誤範例

# google_search_img.py
google圖片 搜尋並下載圖片
* use chromedriver

#### record 
2024/3/19 修改timeoutexception 重新啟動

## 程式開始:
input : key(搜尋關鍵字)、 crab_num(指定抓取的數量)
output : 在電腦路徑底下，建立img資料夾並且儲存圖片

## class & function
GoogleSearchImg (class)

### function 
* __init__ : 開啟google Chrome，連上google 圖片
* search : 輸入搜尋關鍵字 & 搜尋  
判斷 1 : 是否搜尋結果 no_search_result  
判斷 2 : 是否有找到該img元素  
如果找不到有異常 : 關閉原本瀏覽器 並且再開啟檔案 (需要再輸入關鍵字 & 搜尋)  

* more_result:  
判斷 3 : 搜尋最底部，搜尋結果到底，沒有其他搜尋結果了，如果找不到，表示還有其餘搜尋結果未被打開，是一個按鈕元素   
判斷 4 : 判斷指定數量，是否已經達到需求，沒有就控制瀏覽器滾條，直到符合數量   
  
* crab : 確認爬取數量已經滿足需求，開始爬取url 並且 download 
* download : 從url中，下載圖片
* no_search_result : 是否有搜尋結果，True or False
* safe_search: 關閉安全模式

# 中央氣象
## central_weather_index.py 

* 進入主頁輸入，縣市和鄉鎮

## central_weather_data.py

* 抓取表格資料

# 台鐵

## TR_index.py 

* 進到台鐵主頁，搜尋欄中自動填入所需資訊並搜尋

## TR_data.py

* 抓取台鐵資料， 時間表相關資料

# 桃園機場

## Taoy_airport.py

* 抓取桃園機場資訊往國外固定航班資訊

# 高雄小港機場

* 抓取高雄機場資訊往國外固定航班資訊

# 高鐵

## thsrc_index_search.py

* 進到高鐵主頁 選擇搜尋相關資訊 並搜尋

## thsrc_time_data.py

* 搜尋後，高鐵時刻表相關資訊擷取 (設定 可以生成 時間表 或 票價表)

## thsrc_object.py 

* 呼叫物件抓取資料

## thsrc_staion_information.py

* 高鐵提供的各站與台鐵連接的時間表服務擷取

## multi_thsrc.py

* 測試利用multithread 在分配高鐵搜尋上的成效

# 雄獅旅行社

課堂期中挑戰
## index.py 
進到首頁

## search.py
搜尋後頁面抓取

## start.py
程式進入點


# learning 
放練習檔案
* asynic_example.py 模組練習
* timeit.py 模組練習

# fb.py 
製作中 臉書發文 (未完成)














