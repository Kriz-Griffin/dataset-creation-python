#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries
import pandas as pd
import numpy as np
import random


# ### creating array for student id

# In[2]:


sid = np.arange(1000,2000) #1000 is start and 2000 is end


# In[3]:


sid[1:10] #first 10 values


# In[4]:


sid.size


# ## creating random datas for categorical values like gender

# In[5]:


gen = ['male','female'] 
gender = [] #empty list to store n number of data

for i in range(1000):
    x = random.choice(gen)
    gender.append(x)


# In[8]:


gender[1:10] #first 10 values


# In[9]:


len(gender)


# ## Class

# In[10]:


courses = ['BCA','BSc.CS','B.Tech','MCA','M.Tech','MSc.CS']
cls = []


# In[11]:


for i in range(1000):
    x = random.choice(courses)
    cls.append(x)


# In[13]:


cls[1:10] #first 10 values


# In[14]:


len(cls)


# ## Pass or fail

# In[15]:


porf = ['Pass','Pass','Pass','Pass','Pass','Pass','Pass','Fail'] 
#chance of fail is low and pass is high (1/8 chance of fail and 7/8 chance pass)
status = []


# you can use the same method to add Transgender in generating gender

# In[16]:


for i in range(1000):
    x = random.choice(porf)
    status.append(x)


# In[17]:


status[1:10]#first 10 values


# In[18]:


len(status)


# ## creating datas according to the categorical data

# We have created the dataset of passed or failed, now we should create marks according to that. for example if a person is failed, their mark should be less than or equal to 30, if they are passed it should be above 30

# In[19]:


#create an empty list for marks
marks = []


# In[20]:


#iterate through status list and using if condition assign them a value
for i in status:
    if (i == "Fail"):
        tempmark = np.random.randint(0,30)
        marks.append(tempmark)
    else:
        tempmark = np.random.randint(30,100)
        marks.append(tempmark)


# In[21]:


len(marks)


# # Converting these into datasets

# In[22]:


#sid,gender,class,status,marks are the attributes


# In[23]:


df = pd.DataFrame({'Student ID':sid,'Gender':gender,'Class':cls,'Pass/Fail':status,'Marks':marks})


# In[24]:


df.head(10)


# # Saving dataframe to csv file

# In[31]:


df.to_csv("Downloads/File.csv",index=False)


# ## importing this dataset

# In[32]:


dataframe = pd.read_csv("Downloads/File.csv")


# In[33]:


dataframe.head(10)

