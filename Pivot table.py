#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv("D:\Pivot_pandas\Dataset.csv")


# In[3]:


df.head()


# In[4]:


df_pivot = pd.pivot_table(df,values="lead_name",index='feedback',aggfunc="count",
                          margins=True,margins_name="Total",dropna=False)


# In[5]:


df_pivot


# In[6]:


df_pivot.reset_index(level=0, inplace=True)


# In[7]:


df_pivot


# In[18]:


df_pivot.to_csv('report.csv')


# In[9]:


# df_pivot = df_pivot.set_index(['lead_name'])


# In[10]:


# df_pivot.reset_index(level=0, inplace=True)


# In[ ]:





# In[11]:


val = df_pivot["lead_name"].iloc[-1]


# In[12]:


val


# In[13]:


val2 = df_pivot["lead_name"].iloc[0:-1].sum()


# In[14]:


Na_value = int(val-val2)


# In[15]:


Na_value


# In[16]:


new_col = pd.DataFrame([{'feedback':'Feedback Not Available',
            'lead_name' : Na_value}])
new_col.head()


# In[19]:


Last_pivot = df_pivot.append(new_col)


# In[20]:


Last_pivot


# In[ ]:


# Last_pivot


# In[27]:


Last_pivot.iloc[1:] = Last_pivot.iloc[1:].shift(-1)
Last_pivot

