def dec(f):
    return 1

@dec
def double(x):
    return x *2

# 完全等價
double = dec(double)  #輸出和輸入都是函數
print(double) # 1  類似常數函數


def fun1(i):

    def inner(f):

        def inner_main(*args,**kwargs):  #任意長度函數
            ans = f(2)*i
            return ans
        
        return inner_main
    
    return inner

@fun1(1000)
def double(x):
    return x * 2

print(double(2))
#等價
#inner = fun1(1000)
#double = inner(double)



