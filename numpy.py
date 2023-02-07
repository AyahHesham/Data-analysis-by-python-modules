#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# ### creating 1D array from python list 

# In[2]:


x=[1,2,3]
arr=np.array(x)
x


# In[3]:


arr


# ### x is list

# In[4]:


x*2


# In[5]:


np.__version__ 


# ### y is array

# In[6]:


arr*2


# ###  creating 2D array from python list of lists 

# In[53]:


y=[[1,2,3],[1,2,3],[1,6,9],[5,8,0],[7,8,5],[7,5,4]]
arr2=np.array(y)


# In[8]:


arr2


# In[9]:


np.zeros((3,4))


# In[10]:


np.ones((5,6))


# In[11]:


np.arange(1,10,2)


# In[12]:


np.full((4,5),10)


# In[13]:


np.linspace(0,10,5)


# In[11]:


h=[[1,2,3],[1,2,3],[1,6,9],[5,8,0],[7,8,5],[7,5,4]]
arrm=np.array(h)


# In[70]:


arrm.shape


# In[71]:


arrm


# In[14]:


np.eye(6)


# In[61]:


arrm.size


# ### create 5 numbers frm 0 to 10

# In[17]:


L_ARR=np.linspace(0,10,5)
L_ARR


# In[18]:


arr=np.random.rand(5)
arr


# In[19]:


arr=np.random.rand(5,5)
arr


# ### will return 5 random integers

# In[62]:


arr=np.random.randint(1,10,5)


# In[21]:


arr4=np.arange(25)


# ### return the index of max value 

# In[22]:


arr4.argmax()


# In[23]:


arr4.reshape(5,5)


# In[24]:


arr4.min()


# In[25]:


arr4.argmin()


# In[26]:


arr4.max()


# In[27]:


arr5=np.array([1,2,3,4],dtype=np.float32)


# In[28]:


arr5


# In[29]:


arr8 = np.array(['introduciton','to','numpy']).dtype


# ### type conversion

# In[30]:


arr = np.array([True,False],dtype=np.bool_)


# In[31]:


arr.astype(np.int32)  


# ### Type Coercion

# In[32]:


np.array([True , 50,3.5])


# In[33]:


arr = np.array([1,2,3.8]).dtype


# In[34]:


arr


# In[35]:


arr = np.array([True,False,1]).dtype
arr


# ### indexing 1D array

# In[36]:


arr = np.array([10,20,30,40]) 
arr[0]


# ###  indexing 2D array
# #### when indexing 2D array give numpy row and col number

# #####  the second row and first column because we start from 0 

# In[72]:


arrm[1,0]


# #### second row and second column 

# In[73]:


arrm[1][1]


# ### In 2D array
# ####  will return the first full row 

# In[74]:


arrm[0] 


# #### indexing all rows for the 2 colm

# In[75]:


arr2[:,1] 


# ### Slicing Arrays
# #### slice 1D , 4 is not included
# 

# In[76]:


arr = np.array([10,20,30,40,50,60])
arr[2:4]


# ####  slice 2D
# ##### 2:4 from the row. , 3:5 from the cols

# In[77]:


arrm[2:4,3:5] 


# ### slice 2D with a step 
# #### 2:4:2 from the row step = 2 , 3:5:2 from the cols with step = 2

# In[78]:


arrm[2:4:2,3:5:2]


# In[79]:


arrm


# ### Broadcast

# In[45]:


arr = np.arange(25)


# In[46]:


arr[0:5] = 100 


# In[47]:


arr


# In[48]:


arr = np.arange(25) 


# In[49]:


slice_arr = arr[0:5] 


#  ### boradcast all values 

# In[50]:


slice_arr[:] = 100  


# In[51]:


print(slice_arr)        
print(arr)  # the original array will be modified too  


# ### to change this behavior use copy method 

# In[52]:


slice_arr = arr.copy() 
slice_arr[:] = 100 
print(slice_arr)
print(arr)  #will not change  


# ### Sort array
# #### sort along the cols , cols is the defaul

# In[80]:


np.sort(arrm)


# #### axis=0 means sort along the row

# In[81]:


np.sort(arrm,axis=0)


# ### Filtering array

# In[3]:


arr = np.arange(1,6)


# In[5]:


mask = arr % 2 == 0 ##creating a mask
mask


# In[7]:


# conditional selection
bool_arr = arr > 5
arr[bool_arr] # will get the numbers that are > 5 in the array
arr


# In[8]:


arr = np.arange(1,6)
mask = arr % 2 == 0 # creating the mask
arr[mask] # index the array with a mask = fancy indexing


# In[13]:


mymask = arrm[:,1] % 2 == 0 # create mask for rows , 1 = columns
mymask


# In[14]:


arrm[mymask]


# ### np.where :
# #### return array of tuples of indices
# #### we use it when we need the indices to redirect numpy to apply code on them
# #### we can use it for filtering and creating new data based on condition

# In[20]:


np.where(arrm[:,1] % 2 == 0)


# In[22]:


np.where(arr==0 ,"",arr) # this will return all place that is not zero


# ### Array Operations

# In[32]:


arr = np.arange(0,6)


# In[26]:


arr - arr


# In[27]:


arr + arr


# In[28]:


arr * arr


# In[29]:


arr/arr


# In[30]:


arr * 100


# In[33]:


arr ** 2


# ### Array Universal Functions

# In[35]:


np.sqrt(arr)


# In[36]:


np.exp(arr)


# In[37]:


np.sin(arr)


# In[38]:


np.log(arr)


# ### Add elements

# In[39]:


m=[[7,8,9,6],[5,7,8,5],[8,9,7,8],[4,5,3,3]]
y=[[5,7,6,4],[4,2,3,4],[7,9,5,3],[8,6,3,9]]
arr1=np.array(m)
arr2=np.array(y)

np.concatenate((arr1,arr2)) # default with row


# In[40]:


np.concatenate((arr1,arr2),axis=1) # with column


# ### reshape

# In[42]:


arr_1d = np.array([1,2,3])
arr_2d = arr_1d.reshape((3,1))


# ### Deleting in nump

# In[43]:


# to delete the 2 row from an array
np.delete(arr,1,axis=0)


# In[46]:


# to delete the second column use axis=1
np.delete(arrm,1,axis=1)


# In[47]:


# no axis
np.delete(arr,1) # return flatten array


# ### Summarize array data

# In[48]:


arr.sum() # the sum of all values


# In[50]:


arr.sum(axis=0) # sum values of all rows in each column --> create column totals


# In[53]:


arrm.sum(axis=1) # sum values of all columns in each row --> create row totals


# In[54]:


arr.min() # the minimum in the entire array , we can set axis like sum


# In[55]:


arr.max() # the maximum in the entire array , we can set axis like sum


# In[56]:


arr.mean() # the average on the entire array


# In[58]:


arrm.mean(axis=1) # the average in each row


# In[ ]:




