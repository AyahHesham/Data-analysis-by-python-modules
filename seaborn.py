#!/usr/bin/env python
# coding: utf-8

# ![seaborn](https://th.bing.com/th/id/R.65da3af9ceaaa23cf5e9d0984ba4d29a?rik=WO8hdcGKvgGsDQ&pid=ImgRaw&r=0)

# * ****Seaborn is a library mostly used for statistical plotting in Python.
# *** It is built on top of Matplotlib and provides beautiful default styles and color palettes to make statistical plots more attractive**

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
sns.__version__


# In[2]:


sns.get_dataset_names()


# In[3]:


df=sns.load_dataset('flights')
df.head()


# In[4]:


x=[5,10,15]
y=[16,18,30]
sns.set(style="darkgrid") #integrate seaborn with plt
plt.plot (x,y)


# # Countplot

# In[5]:


sns.countplot(x='passengers',data=df)


# In[6]:


sns.countplot(x='passengers',data=df,hue='month',palette='viridis')


# # Barplot
# * used for statical functions

# In[7]:


sns.barplot(x='passengers',y='month',data=df)


# In[8]:


sns.barplot(x='passengers',y='month',data=df,ci=None,estimator=sum)
#ci for remove line


# # ViolinPlot

# In[9]:


sns.violinplot(y='passengers',data=df)


# In[10]:


sns.violinplot(y='passengers',data=df,hue='month')


# # Swarmplot

# In[11]:


sns.swarmplot(x='passengers',data=df)


# # Strip Plot

# In[12]:


sns.stripplot(x='passengers',data=df) #like swarmplot but every oint drawn lonly

