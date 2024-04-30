# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:48:02 2024

@author: USER
"""

from timeit import timeit

lst = (i for i in range(100))

def good(num):
    return num >= 60

def fun():
    ans = []
    for num in lst:
        if good(num):
            ans.append(num)
    return ans
            
def fun2():
    return filter(good, lst)

print(f"with: {timeit(fun,number=10000)}")
print(f"with: {timeit(fun2,number=10000)}")