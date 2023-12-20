#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q.7 How do you connect jupyter notebook to mysql ?

get_ipython().system('pip install mysql.connector')


# In[2]:


import mysql.connector


# In[3]:


conn = mysql.connector.connect(host = 'localhost' , 
                             user = 'root',
                             password = '', 
                             database = 'praveendata')


# In[4]:


import pandas as pd


# In[5]:


pd.read_sql_query("SELECT * FROM bank_accounts" , conn)


# In[ ]:




