# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 13:15:09 2024

@author: USER
"""

import os

fd = os.open("./test.py",os.O_WRONLY | os.O_APPEND | os.O_CREAT)
str = "print('hello world')"
os.write(fd,str.encode())
os.close(fd)

os.system("python test.py")
