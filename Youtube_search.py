#!/usr/bin/env python
# coding: utf-8

# In[1]:


import webbrowser
import pyautogui as py
import time
#test_str=str(input("ENTER EMAIL ID OF THE PROFILE TO BE SEARCHED:"))
#res=test_str.split("@")[0]
#l=[]
#for i in res:
    #l.append(i)
#ls_alpha = [i for i in l if not i.isdigit()]
#s=""
#s=s.join(ls_alpha)
x=str(input("ENTER YOUR SRN:"))

from getpass import getpass
y=getpass('ENTER PASSWORD:')

webbrowser.open("https://www.pesuacademy.com/Academy/")

time.sleep(5)
#py.typewrite(x)
#py.keyDown("tab")
#py.keyDown("tab")
py.typewrite(x)
py.keyDown("tab")
py.typewrite(y)

py.keyDown('return')


time.sleep(1)

time.sleep(3)
py.keyDown('tab')

#py.typewrite(s)
time.sleep(5)


py.keyDown("return")
time.sleep(3)
py.keyDown("return")


# In[2]:



pip install pyautogui


# In[ ]:




