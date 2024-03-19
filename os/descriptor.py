
class Name():
    def __get__(self,obj,objtype):
        return "kingston"
    
class A:
    name = Name()    #要觸發descriptor 必須要是 type attribute or member

class B:
    def __init__(self):
        self.name = Name()    #type 產生的 object 無法觸發 descriptor

o = A()
o2 = B()
print(o.name)   # o是一個a的實例類
print(A.name)   # 呼叫A裡的name屬性 裡面實際是一個Name 實例
print(o.__dict__)
print(o)
print("=======================")
print(o2.name)  # 變成了一個Name的class
print("=======================")
print(o.name)    
o.name = "aaa"   #調用STORE_ATTR , 將name 設定為 aaa => __dict__ : {"name":"aaa"}
print(o.__dict__)
print(o.name)
Name.__set__ = lambda x,y,z: None  #增加一個__set__ 函數
print(o.name)   #結果變成 kingston  #調用LOAD_ATTR

# 當如果 descriptor 內 沒有 __get__ , __set__ 同時存在 => 則查看 __dict__ 又沒有  => 看看單獨 __get__ 有沒有值




