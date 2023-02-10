#!/usr/bin/env python
# coding: utf-8

# In[7]:


import sys  
get_ipython().system('{sys.executable} -m pip install --user matplotlib')


# In[52]:


import matplotlib.pyplot as plt


# In[53]:


import numpy as np


# In[54]:


import pandas as pd


# ## plot

# In[75]:


x=np.array([1,3,5,7])
y=np.array([2,4,6,8])
plt.plot(x,y)


# In[22]:


plt.plot(x,y,'o',color='yellow')  #WE CAN USE ANY SEMBOLE


# ### we can draw by one axis

# In[17]:


plt.plot(x)


# In[21]:


plt.plot(x,marker='o',color='Crimson')


# In[39]:


plt.plot(x,marker='*',color='Crimson',ms='20',linestyle='dashed',mfc='yellow',linewidth='5',mec='blue')


# In[41]:


z=np.array([1,3,5,7])
y=np.array([20,30,40])


# In[42]:


plt.plot(x)
plt.plot(y)


# In[48]:


plt.plot(x,color='Crimson')
plt.plot(y,color='DarkCyan')
plt.xlabel('products',loc='left')
plt.ylabel('sales',loc='bottom')
plt.title('jumia')


# In[51]:


font1={'family':'impact','color':'green','size':15}
plt.plot(x,color='Crimson')
plt.xlabel('products',loc='left',fontdict=font1)
plt.title('jumia')
plt.grid()


# In[57]:


font1={'family':'impact','color':'green','size':15}
plt.plot(x,color='Crimson')
plt.xlabel('products',loc='left',fontdict=font1)
plt.title('jumia')
plt.grid(axis='x')


# In[60]:


font1={'family':'impact','color':'LightBlue','size':15}
plt.plot(x,color='Crimson',linewidth='5')
plt.xlabel('products',loc='left',fontdict=font1)
plt.title('jumia')
plt.grid(axis='y',color='y',linestyle='--',linewidth='4')


# In[69]:


font1={'family':'impact','color':'green','size':15}
plt.plot(x,color='Crimson')
plt.xlabel('products',loc='left',fontdict=font1)
plt.title('jumia')
plt.grid()
plt.figure(figsize=(10,12)) #for figuer size
plt.savefig('mysirst figure')


# In[73]:


plt.gcf().canvas.get_supported_filetypes_grouped()


# In[74]:


plt.gcf().canvas.get_supported_filetypes().keys()


# # Scatter plot

# In[80]:


z=np.array([1,90,5,7,89,60,40,80,77,88])
y=np.array([10,96,35,27,40,99,42,96,7,21])
a=np.array([12,94,55,73,29,54,43,82,17,48])
b=np.array([11,9,59,36,23,69,20,63,8,22])
al=([.6,.4,.8,1,1.5,.9,.4,.3,.2,.3])
plt.scatter(z,y,color='r')
plt.scatter(a,b,color='b')


# In[81]:


z=np.array([1,90,5,7,89])
y=np.array([10,96,35,27,40])
colors=np.array(['Crimson','yellow','blue','pink','black'])
plt.scatter(z,y,color=colors)


# In[84]:


z=np.array([1,90,5,7,89,60,40,80,77,88])
y=np.array([10,96,35,27,40,99,42,96,7,21])
a=np.array([12,94,55,73,29,54,43,82,17,48])
b=np.array([11,9,59,36,23,69,20,63,8,22])
al=([.6,.4,.8,1,.5,.9,.4,.3,.2,.3])
plt.scatter(z,y,color='r',alpha=al)
plt.scatter(a,b,color='b')


# # Bars

# In[89]:


plt.bar(a,b)


# In[91]:


plt.barh(a,b,color='g')


# # Histogram

# In[92]:


plt.hist(x)


# # Pie chart

# In[98]:


z=np.array([1,90,5,7,89])


# In[99]:


t=['data','scince','math','en','static']
plt.pie(z,labels=t)


# In[106]:


t=['data','scince','math','en','static'] #labels array
xp=[.2,.1,.4,.2,.2] #explode array
plt.pie(z,labels=t,explode=xp)


# In[115]:


t=['data','scince','math','en','static'] #labels array
xp=[.2,.1,.4,.2,.2] #explode array
plt.pie(z,labels=t,explode=xp,shadow=True,colors=colors)
plt.legend()


# In[117]:


t=['data','scince','math','en','static'] #labels array
xp=[.2,.1,.4,.2,.2] #explode array
plt.pie(z,labels=t,explode=xp,shadow=True,colors=colors)
plt.legend(title='subject') #legend for define data


# # Box plot
# ### used for outlayer

# In[123]:


plt.boxplot(z)


# In[126]:


z=np.array([1,90,5,7,89,60,40,80,77,88])
y=np.array([10,96,35,27,40,99,42,96,7,21])
plt.fill_between(y,a)


# In[ ]:





# In[ ]:




