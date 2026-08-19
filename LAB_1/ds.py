#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


titanic_df = pd.read_csv("titanic.csv")
titanic_df.head()


# In[ ]:


df_from_url = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
df_from_url.head()


# In[ ]:


df_from_txt = pd.read_table("data_set.txt", sep="\t")
df_from_txt.head()


# In[ ]:


student_data = {
    "Roll_No": [10, 20, 30, 40, 50],
    "Name": ["Praneeth", "Reddy", "Karthik", "Tharun", "Shiva"],
    "Department": ["IT", "CSE", "AIML", "DS", "CS"],
    "Percentage": [90, 86, 92, 88, 95],
}

df_from_dict = pd.DataFrame(student_data)
df_from_dict.head()


# In[ ]:


df_from_json = pd.read_json("data.json")
df_from_json.head()

