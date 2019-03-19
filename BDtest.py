#!/usr/bin/env python
# coding: utf-8

# In[13]:


import sqlite3


# In[14]:


conn = sqlite3.connect('nam.db')


# In[15]:


c = conn.cursor()


# In[16]:


c.execute ('''CREATE TABLE masters (firstname text, lastname text, age int, score real)''')


# In[27]:


firstname = "Vladimir"
lastname = "Kuznetsov"
age = 29
score = 25


# In[28]:


conn.commit()


# In[29]:


c.execute ("INSERT INTO masters (firstname, lastname, age, score) VALUES (?,?,?,?)", (firstname, lastname, age, score))


# In[30]:


conn.commit()


# In[31]:


conn.close()


# In[ ]:




