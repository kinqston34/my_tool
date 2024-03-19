# my_tool
use python create tool

# os
使用os 套件範例

## os.py test.py
os.py write code into test.py , then run test.py

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









