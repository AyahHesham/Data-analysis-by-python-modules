#!/usr/bin/env python
# coding: utf-8

# In[95]:


import pandas as pd


# In[6]:


pd.__version__ 


# #### -In pandas 1d named Series  and 2d or more named dataframe
# #### -Case sentisive
# #### -we can return darta by the index and we cane change the type of index

# In[9]:


list=[1,2,3,4]
s=pd.Series(data=list)
s


# In[10]:


s[3]


# In[15]:


s2=pd.Series(data=list,index=['a','b','c','d'])
s2


# In[14]:


s2['a']


# In[16]:


s2[0]


# #### we can make Series  from dic not only list

# In[18]:


d={'a':4,'b':6,'c':8,'d':10}
s3=pd.Series(data=d)
s3


# ### Dataframe in pandas like matrix in numpy -->2d 
# #### dataframe is a main tool in pandas
# #### structured from columns and rows like excel 
# #### every column is a Series and can has their own datatype 
# ##### the row can has more than datatype but column not

# In[98]:


data={'student':['Aya','Ahmed','Alaa'],'age':[25,20,17],'degree':[80,94,97]}
df=pd.DataFrame(data)
df


# In[99]:


df2=pd.DataFrame(data,index=['a','b','c'])
df2


# #### To return data from df
# ##### dataframe name ['column name'] or dataframe name.column name will return data from sereis

# In[25]:


df2['student']


# In[26]:


df.age


# #### For take subset from df , df name[[]]

# In[28]:


df[['degree','age']]


# ### we can conctinate two columns and add it in the main df

# In[31]:


df['stu_age']=df['student']+df['age']
df['stu_age']


# #### To drop column or rows but not from the main df with column
# ##### axsis=1 -->column , axsis=0 -->row and this is the default

# In[40]:


df.drop('degree',axis=1)


# In[41]:


df


# In[42]:


df.drop(2)


# #### for drop column or row from the main df we will use inplace attribute

# In[49]:


df.drop('degree',axis=1,inplace=True)
df


# In[50]:


df.shape


# ### Locate elements
# #### iloc for integre , loc for others

# In[73]:


df.iloc[1]


# In[75]:


df2.loc['b','age']


# In[72]:


df2.iloc[ : ,2]


# In[80]:


df.loc[df.age>20]


# In[81]:


df.loc[df.age==20]


# In[82]:


df.loc[df.age!=20]


# ### get columns based on selected data

# In[94]:


df.loc[df['student'].isin(['aya','Aya','Alaa']),:]


# In[101]:


df.loc[(df.age>22)&(df.degree>70)]


# ### we can use lambda on df column withe use 'applay and lambda name'
# #### if we wanna make all alpapit of word capital 

# In[107]:


df['student'].apply(lambda x:x.upper())


# In[108]:


df


# #### Mask in pandas

# In[109]:


df[df.age>22]


# In[110]:


df[df['age']>22]


# ## How to read data

# In[113]:


df=pd.read_csv('diabetes.csv') ##csv or any type


# In[118]:


df.head() #for 5 rows from the table head


# In[117]:


df.head(10)


# In[120]:


df.sample() #sample from anywhere in dataset


# In[121]:


df.sample(7)


# In[125]:


df.shape


# In[123]:


df.info()


# In[126]:


df.columns


# In[129]:


df.describe() #for static functions on dataset


# In[130]:


df.memory_usage()


# In[132]:


df['Outcome'].value_counts()


# ### For know if there are null or duplicated data

# In[133]:


df.isna()


# In[134]:


df.isna().sum()


# In[ ]:


df.dropna(inplace=true) # to drop null data from the dataset


# In[ ]:


df.fillna('value',inplace=true) #to replace null with values


# In[ ]:


df['column name'].fillna('value',inplace=true) #to replace null with values in selected clumn


# ##### duplicated data

# In[135]:


df.duplicated()


# In[141]:


df[df.duplicated()] #for dublicated value


# In[ ]:


df.drop_duplicates()


# In[ ]:


df.drop_duplicates(inpace=true) #to drop dublicates data from dataset and save it

