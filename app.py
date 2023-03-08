import streamlit as st
import pandas as pd
import numpy as np

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




