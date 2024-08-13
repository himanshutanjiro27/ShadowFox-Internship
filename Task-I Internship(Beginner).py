#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


data1=pd.read_csv("Downloads/HousingData.csv")
data1.head()


# In[6]:


# Exploring the Dataset in depth
data1.describe()


# In[6]:


data1.info()


# In[7]:


# Data Cleaning 
data1.isnull()


# In[8]:



data1.isnull().sum()


# In[9]:


data1.tail()


# In[ ]:





# In[15]:




