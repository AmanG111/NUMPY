#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[10]:


data = pd.read_csv("Covid19.csv")


# In[11]:


data.head()


# In[12]:


data.describe()


# In[13]:


pd.to_datetime(data.date)
data.country.value_counts()


# In[14]:


data = data[data.country.apply(lambda x: x not in ["England", "Scotland", "Wales", "Northern Ireland"])]
data.country.value_counts()


# In[15]:


data.vaccines.value_counts()


# In[16]:


df = data[["vaccines", "country"]]
df.head()


# In[17]:


dict_ = {}
for i in df.vaccines.unique():
  dict_[i] = [df["country"][j] for j in df[df["vaccines"]==i].index]

vaccines = {}
for key, value in dict_.items():
  vaccines[key] = set(value)
for i, j in vaccines.items():
  print(f"{i}:>>{j}")


# In[23]:


import plotly.express as px
import plotly.offline as py

vaccine_map = px.choropleth(data, locations = 'iso_code', color = 'vaccines')
vaccine_map.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
vaccine_map.show()


# In[ ]:




