#!/usr/bin/env python
# coding: utf-8

# In[23]:


A=[3,4,4,6,1,4,4] 
c=0
N=5
l= [0]*N
for j in A:
    if j<=N: 
        c=1
        i=j-1
        #print(i)
        l[i]+=c
        c=0
        #print(l)
    if j>N:
        c=max(l)
        l=[c]*N
print(l)
   
            
            
    
        
    


# In[ ]:


(0, 0, 1, 0, 0)
(0, 0, 1, 1, 0)
(0, 0, 1, 2, 0)
(2, 2, 2, 2, 2)
(3, 2, 2, 2, 2)
(3, 2, 2, 3, 2)
(3, 2, 2, 4, 2)

