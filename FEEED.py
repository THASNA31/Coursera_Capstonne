#!/usr/bin/env python
# coding: utf-8

# ## Assuming the branches also receive their equitable protion

# ### Imprt necessary libraries

# In[2]:


import numpy as np
from scipy.optimize import minimize


# ### Data

# In[56]:


# Demand at the agencies
dem = np.array([10,20,25,15])

# Holding costs
h0 = 5    # at hub
h1 = 5    # at branch 1
h2 = 5    # at branch 2

# Begining inventory
I0 = 5    # at hub
I1 = 5    # at branch 1
I2 = 5    # at branch 2

# Food donations
S0 = 5    # to hub
S1 = 30   # to branch 1
S2 = 5    # to branch 2

# Distance matrix
D = np.array([100,30,20,25,30,15,10,10])


# ### List of indexes served by each branch

# In[57]:


# Agencies served by the branches
b = np.array([[0,1],[2,3]])


# ### Generte the functions for equity, effectiveness and efficiency

# #### Equity

# In[62]:


def equity(x,y):
    eq = 0
    for i in range(1, len(x)+1):
        eq = eq + abs(x[i-1] - (sum(dem[b[i-1]])/sum(dem))*sum(x))
        
    for j in range(1, len(y)+1):
        eq = eq + abs(y[j-1] - (dem[j-1]/sum(dem))*sum(y))
        
    return eq

