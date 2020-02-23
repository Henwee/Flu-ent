#!/usr/bin/env python
# coding: utf-8

# In[2]:


import folium
import pandas as pd


# In[3]:


flu_data = pd.read_csv(r"C:\Users\Kevin Pradjinata\Desktop\hackathon\hacks.csv")


# In[4]:


flu_data.head()


# In[5]:


flu_total = list(flu_data["INF_TOTAL"])


# In[6]:


flu_country = list(flu_data["COUNTRY"])


# In[7]:


flu_dict = {}
i = 0
for k in flu_country:
    flu_dict[k] = flu_total[i]
    i += 1


# In[8]:


flu_dict


# In[9]:


country_data = pd.read_csv(r"C:\Users\Kevin Pradjinata\Desktop\hackathon\centers.csv")


# In[10]:


country_data.head()


# In[11]:


country_long = list(country_data["Longitude"])
country_lat = list(country_data["Latitude"])


# In[12]:


country_list = list(country_data["Country"])


# In[13]:


country_list.index("United States")


# In[14]:


for k in flu_dict.keys():
    if k in country_list:
        ind = country_list.index(k)
        print(k, country_lat[ind], country_long[ind], flu_dict[k])
    else:
        print(k)


# In[15]:


map = folium.Map(location=[0, 0], zoom_start=1.5)


# In[16]:


folium.Circle(
        radius= 100,
        location=[33, 65],
        color='crimson',
        fill=True,
        ).add_to(map)


# In[17]:


for k in flu_dict.keys():
    if k in country_list:
        ind = country_list.index(k)
        folium.Circle(
        radius= flu_dict[k] * 50,
        location=[country_lat[ind], country_long[ind]],
        color='crimson',
        fill=True,
        ).add_to(map)


# In[18]:


map


# In[ ]:




