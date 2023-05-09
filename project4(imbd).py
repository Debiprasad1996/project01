#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. plot a graph to show the distribution of genre in the top 250 movies 
# 2. find out which movie has the maximum number of votes and which genre it belongs to and its duration.
# 3. find out which movie has the minimum number of votes and which genre it belongs to and its duration.
# 4. find out movies of each genre which has maximum number of votes. *


# In[14]:


import pandas as pd
import seaborn as sns
import numpy as np


# In[15]:


data=pd.read_csv("movies.csv")
df=pd.DataFrame(data)
print(df).head(10)


# In[16]:


df.info()


# In[18]:


df.describe()


# # To convert (imbd_votes) object to int

# In[23]:


df["imbd_votes"] = df["imbd_votes"].replace("[,,]", "", regex=True).astype(int)


# In[20]:


df.info()


# In[21]:


df.describe()


# # 2. find out which movie has the maximum number of votes and which genre it belongs to and its duration.

# In[24]:


df["imbd_votes"].max()


# In[31]:


df1=df.loc[df["imbd_votes"]==2711075]
df1[["title","imbd_votes","genre","duration"]]


# # 3. find out which movie has the minimum number of votes and which genre it belongs to and its duration.

# In[32]:


df["imbd_votes"].min()


# In[33]:


df1=df.loc[df["imbd_votes"]==31167]
df1[["title","imbd_votes","genre","duration"]]


# # 4. find out movies of each genre which has maximum number of votes

# In[40]:


gp=df.groupby("genre").agg({"imbd_votes":max})
gp


# # plot a graph to show the distribution of genre in the top 250 movies

# In[42]:


df[["genre","imbd_votes"]]


# In[46]:


sns.lineplot(data=df,x="genre",y="imbd_votes",color="purple")
plt.show()


# In[ ]:




