#!/usr/bin/env python
# coding: utf-8

#  <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <h1 align=center>Data 1202: Data Analytics Tools</h1>
#     <h1 align=center>Lab 2</h1>
# </div>

# <h1>Introduction</h1>
# <h3>Welcome!</h3>
# 
# <p>
# In this Lab, you will learn how to use Python (pandas) for preprocessing your data when Imported from a SQL databease and from csv loacal file. By the end of this lab, you will be familiar with the connection methods and how you can run SQL Queries using Python.
# </p>

# <h2>Table of Contents</h2>
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# In this Lab you will learn:
# <ol>
#     <li><a href="#p1">How to import a csv file from your device</a></li>
#     <li><a href="#p2">Run Simple Queries and read them into a DataFrame</a></li>
#     <li><a href="#p3">Run Complex Queries and read them into a DataFrame</a></li>
#     <li><a href="#p4">WHERE in Python</a></li>
#     <li><a href="#p5">Practice Questions</a></li>
# </ol>
# 
# Estimated Time Needed: <strong>60 min</strong>
# </div>
# 

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <h1 align=center><a name=p1>Part 1 :How to import a csv file from your device  </a></h1>
# </div>

# In[1]:


# How many games on this list were launched between 2000-2005? 

# Import pandas
import pandas as pd


# In[23]:


# Set file path to a variable
input_salaries = "Salaries.csv"


# In[24]:


# Read Data into a DataFrame
df_salaries = pd.read_csv(input_salaries)
df_salaries.head()


# In[19]:


# This is the practice importing csv files from diffrence location
#change backward slash / to forward slash \ 
#df_test = pd.read_csv('D:\DC Study\Data-1202/vgsales.csv')
df_test = pd.read_csv(r'D:\DC Study\Data-1202\vgsales.csv')
df_test.head()


# In[20]:


# Filter DataFrame for proper years
between_00_05 = df_test[(df_test["Year"] >= 2000) & (df_test["Year"] <= 2005)]

print(between_00_05)


# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <h1 align=center><a name=p2>Part 2 : Run Simple Queries and read them into a DataFrame </a></h1>
# </div>

# In[1]:


import pandas as pd
import pymysql
from sqlalchemy import create_engine


# In[2]:


engine = create_engine('mysql+pymysql://user10:PW@localhost/ap')


# In[3]:


conn = engine.connect()


# In[4]:


# read a simple query into DataFrame
df=pd.read_sql_query("SELECT * FROM data1202.vgsales", conn)


# In[5]:


# print DataFrame and shaw the first 10 raws
df.head()


# In[6]:


#Find how many records this data frame has
df.shape


# In[7]:


#How many elements are there?
df.size


# In[8]:


#What are the column names?
df.columns


# In[9]:


#What types of columns we have in this data frame?
df.dtypes


# In[10]:


df.info()


# In[ ]:


dir(df)


# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <h1 align=center><a name=p3>Part 3 : Run Complex Queries and read them into a DataFrame </a></h1>
# </div>

# In[ ]:


# read a complex query into DataFrame
complex_df = pd.read_sql_query('''SELECT
    Round(SUM(NA_Sales)) as 'NA_Sales',
    ROUND(SUM(EU_Sales)) as 'EU_Sales',
    ROUND(SUM(JP_Sales)) as 'JP_Sales',
    ROUND(SUM(Global_Sales)) AS 'Global_Sales',
    ROUND((SUM(NA_Sales)/SUM(Global_Sales)) * 100) as 'NA_GlobalShare'

FROM
    data1202.vgsales
WHERE
    Genre = 'Action'
        AND Year>= 2005''', conn)


# In[ ]:


complex_df.head()


# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <h1 align=center><a name=p4>Part 4 : WHERE in Python </a></h1>
# </div>

# In[ ]:


# WHERE in python
nintendo_games = df[df['Publisher'] == 'Nintendo]


# In[ ]:


nintendo_games.head()


# In[ ]:


print("The number of Nintendo games is: " + str(len(nintendo_games)))


# In[ ]:


# Read Data into a DataFrame
df = pd.read_csv(input_file_path)


# In[ ]:


# TWO condition WHERE clause
action_05 = df[(df['Genre']=='Action') & (df['Year'] >= 2005)]
action_05.head()


# In[ ]:


print("The max sales of action games in EU after 2005 is: " + str(action_05.EU_Sales.max()))


# In[ ]:


# Filter DataFrame for proper years
between_00_05 = df[(df["Year"] >= 2000) & (df["Year"] <= 2005)]

print(between_00_05)


# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <h1 align=center><a name=p5>Part 5 : Practice Questions </a></h1>
# </div>

# <div class="alert alert-danger alertdanger" style="margin-top: 20px">
# <h1>Question #1:</h1>
# <b>Shaw all databases</b>
# </div>

# In[ ]:


# <your code goes here>


# <div class="alert alert-danger alertdanger" style="margin-top: 20px">
# <h1>Question #2:</h1>
# <b>From Vg_sales, retrive all sales between 2000 and 2005 and assign them to All_sales dataframe</b>
# </div>

# In[ ]:


# <your code goes here>


# 
# <div class="alert alert-danger alertdanger" style="margin-top: 20px">
# <h1>Question #3:</h1>
# <b>Identify the data type for all columns in All_sales dataframe you created in Question 2.</b>
# </div>
# 

# In[ ]:


# <your code goes here>


# 
# 
# <div class="alert alert-danger alertdanger" style="margin-top: 20px">
# <h1>Question #4:</h1>
# <b>List the column names of the dataframe you created in Question 2</b>
# </div>
# 

# In[ ]:


# <your code goes here>

