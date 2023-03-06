#!/usr/bin/env python
# coding: utf-8

# # Streamlit app for airline crash data

# First we install streamlit. Remove the # to run and put it back after to ensure the instal is not repeated

# In[2]:


# pip install streamlit


# In[3]:


import streamlit as st 
import pandas as pd
import numpy as np


# ## Import data

# In[4]:


HairEye = pd.read_csv("/Users/laurenmeenhorst/Desktop/Minor/IDS werkcolege 1/HairEyeColor(1).csv")


# In[5]:


st.title("Hair eye clours")


# In[8]:


InputHair = st.sidebar.selectbox("Select Hair colour", ("Brown", "Blond", "Black", "Red"))


# In[9]:


HairEyeSelect = HairEye[HairEye["Hair"] == InputHair]


# In[10]:


st.dataframe(HairEyeSelect)


# In[ ]:




