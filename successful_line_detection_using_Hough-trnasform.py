#!/usr/bin/env python
# coding: utf-8

# ### Description : This python notebook includes the comparative study of line detection technique by using hough-transform method.We have taken 3 sample input images for the purpose,We can have a closer look at the given inputs and outputs.

# ### Author : Riya Chougule

# ### Date : 26/8/2020

# In[1]:


import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# #### 1.Invoice original sample

# In[2]:


img4 = cv2.imread("inv10.jpg")
grayscale4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
edges4 = cv2.Canny(grayscale4, 30, 100)
lines4 = cv2.HoughLinesP(edges4, 1, np.pi/180, 60, 50, 5)
for line in lines4:
    for x1, y1, x2, y2 in line:
        res4=cv2.line(img4, (x1, y1), (x2, y2), (20, 220, 20), 3)
result4 = Image.fromarray(res4)
img4 = Image.open("inv10.jpg",'r')
img4


# #### 1.Line-detected image

# In[3]:


result4


# #### 2.Invoice original sample

# In[4]:


img5 = cv2.imread("inv20.jpg")
grayscale5 = cv2.cvtColor(img5, cv2.COLOR_BGR2GRAY)
edges5 = cv2.Canny(grayscale5, 30, 100)
lines5 = cv2.HoughLinesP(edges5, 1, np.pi/180, 60, 50, 5)
for line in lines5:
    for x1, y1, x2, y2 in line:
        res5=cv2.line(img5, (x1, y1), (x2, y2), (20, 220, 20), 3)
result5 = Image.fromarray(res5)
img5 = Image.open("inv20.jpg",'r')
img5


# #### 2.Line-detected image

# In[5]:


result5


# #### 3.Invoice original sample

# In[6]:


img6 = cv2.imread("inv8.jpg")
grayscale6 = cv2.cvtColor(img6, cv2.COLOR_BGR2GRAY)
edges6 = cv2.Canny(grayscale6, 30, 100)
lines6 = cv2.HoughLinesP(edges6, 1, np.pi/180, 60, 50, 5)
for line in lines6:
    for x1, y1, x2, y2 in line:
        res6=cv2.line(img6, (x1, y1), (x2, y2), (20, 220, 20), 3)
result6 = Image.fromarray(res5)
img6 = Image.open("inv8.jpg",'r')
img6


# #### 3.Line-detected image

# In[7]:


result6


# ### Conclusion : We can observe that lines detected are highlitghted by green colour and we can have the detected lines by comparative study of original image and edge-detected image
