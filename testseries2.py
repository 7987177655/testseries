#!/usr/bin/env python
# coding: utf-8

# In[36]:


# Q.1 What is Pandas ?
# Ans :- pandas is a open source library which is used for data manipulations . 
import pandas as pd
# (1). Series ==> 
a = pd.Series([1,22,32,77])
a


# In[2]:


# Q.2 Difference between series and dataframe ?

# Ans :- series used for one dimentional data and its output will be only value not coloum name,
#        data frame used for multidimensional data and its output will be both value and coloum name . 


# In[47]:


# Q.3 Difference between loc and iloc ? 

# Ans :- in loc syntax is [row_range , coloum_name] starting , starting & end point both include . 

df = pd.read_csv("C:\\Users\\Dell\\Documents\\data analyst task\\Salary_Data.csv")
df.head()
df.loc[:2 , "Salary" ] # starting to end point include


# In[48]:


# in iloc syntax is [ row_range , coloumn_index_number] , starting point include but last point is not include.

df = pd.read_csv("C:\\Users\\Dell\\Documents\\data analyst task\\Salary_Data.csv")
df.head()
df.iloc[:2 , 1 ] # starting point include but end point not include


# In[52]:


# Q.4 what does value_counts() ?

# Ans :- using this command we can find total of subcatogries of coloumn . 
#  syntax - dataframe['coloumn_name'].value_counts()

df = pd.read_csv("C:\\Users\\Dell\\Documents\\data analyst task\\Salary_Data.csv")
df.head()
df['Salary'].value_counts()


# In[53]:


df['YearsExperience'].value_counts()


# In[57]:


# Q.5 how do you handle missing values using pandas ?

# Ans : - df.isnull().sum( ) with the help of this we can find missing value in the coloumn and with the help of
#           df.dropna() command we can drop missing value of coloumn . 

df.isnull()
df = df.dropna()

df = pd.read_csv("C:\\Users\\Dell\\Documents\\data analyst task\\Salary_Data.csv")
df.head()
df['Salary'][1:2] = None
df


# In[1]:


# Q.6 How do you merge 2 tables using pandas ?

# Ans :- 
    
import pandas as pd

 
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['KRITI', 'RUCHI', 'POOJA']})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Age': [21, 25, 26]})

 
merged_df = pd.merge(df1, df2)

print(merged_df)


# In[9]:


# Q.8 What does group by in pandas ?

# A groupby operation involves some combination of splitting the object, applying a function, 
# and combining the results. This can be used to group large amounts of data and compute operations on these groups.

df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})
df
df.groupby(['Animal']).mean()


# In[10]:


# Q.9 difference between CrossTab vs Pivot table ?

# Ans :- 

# 1.Crosstabs are used for categorical data, while pivot tables can be used for both categorical and numerical data.
# 2.Crosstabs are used to analyze the relationship between two categorical variables, while pivot 
# tables can analyze the relationships between multiple variables, both categorical and numerical.


# In[11]:


# Q.10 In which scenerio what kind of plot you will use ? Numerical ==? , Categorical ==?

# Ans :- Numerical plots in data visualization:
# 1. Histogram
# 2. Box PLot
# 3. Line plot
# 4. Scatter Plot
# 5. pie charts


# catogorical plots in data visualization:
# 1. Box PLot
# 2. Line plot
# 3. Scatter Plot
# 4.point plot


# In[13]:


# Q.11 What does TimeDelta in Pandas ?

# Ans :- 

# time delta represents the difference between two dates and time.

import pandas as pd

delta = pd.Timedelta(days=3, hours=2, minutes=20)
delta


# In[17]:


# Q.12 How can you extract day , month , year in a date column using pandas ?

# Ans :- 

import pandas as pd

data = {'Date': ['2023-04-04', '2023-05-06', '2023-07-08']}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
df


# In[18]:


# Q.13 How can you extract hours , minutes , seconds in a datetime column ?

# Ans :- 

import pandas as pd

data = {'Datetime': ['2023-11-20 07:33:45', '2023-10-20 12:40:30', '2023-12-15 11:11:25']}

df = pd.DataFrame(data)

df['Datetime'] = pd.to_datetime(df['Datetime'])


df['Hour'] = df['Datetime'].dt.hour
df['Minute'] = df['Datetime'].dt.minute
df['Second'] = df['Datetime'].dt.second


df


# In[22]:


# Q.14 How do you read a excel file , csv file and json file in jupyter notebook using pandas ?

# Ans :- 

df = pd.read_csv("C:\\Users\\Dell\\Documents\\data analyst task\\Salary_Data.csv")

df.head()


# In[24]:


df = pd.read_json("C:\\Users\\Dell\\Documents\\data analyst task\\csvjson.json")
df.head()


# In[88]:


# Q.15 How can you create excel data from a dataframe using pandas ?

# Ans :- 

import pandas as pd

 
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['KRITI', 'RUCHI', 'POOJA']})

print(df1)

df1.to_excel("C:\\Users\\Dell\\record.xlsx") # with the help of this we can save file in excel format .


# In[ ]:




