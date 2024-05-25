#!/usr/bin/env python
# coding: utf-8

# In[3]:


from numpy import random
x= random.randint(5)
print(x)


# In[6]:


from numpy import random
x=random.rand()
print(x)


# In[8]:


from numpy import random
x= random.randint(100,size= 5)
print(x)


# In[10]:


from numpy import random
x= random.randint(100,size=(2,5))
print(x)


# In[11]:


from numpy import random
x=random.rand(5)
print(x)


# In[12]:


from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)


# In[13]:


from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)


# In[14]:


from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)


# In[15]:


from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))


# In[17]:


x=[1,2,3,4,5]
y=[6,7,8,9,10]
z=[]
for i,j in zip(x,y):
    z.append(i+j)
    print(z)
    


# In[19]:


import numpy as np
x=[1,2,3,4,5]
y=[6,7,8,9,10]
z=np.add(x,y)
print(z)


# In[20]:


import numpy as np
x=[1,2,3,4,5]
y=[6,7,8,9,10]
z=np.subtract(x,y)
print(z)


# In[26]:


import numpy as np
def myadd(x,y):
    return x+y
myadd = np.frompyfunc(myadd,2,1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))


# In[27]:


import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
z=np.add(x,y)
print(z)


# In[28]:


import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
z=np.subtract(x,y)
print(z)


# In[30]:


import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
z=np.multiply(x,y)
print(z)


# In[31]:


import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
z=np.divide(x,y)
print(z)


# In[32]:


import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
z=np.power(x,y)
print(z)


# In[33]:


import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
z=np.mod(x,y)
print(z)


# In[34]:


import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
z=np.divmod(x,y)
print(z)


# In[35]:


import numpy as np

arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)

print(newarr)


# In[36]:


import numpy as np

arr = np.trunc([-3.1666, 3.6667])

print(arr)


# In[37]:


import numpy as np

arr = np.fix([-3.1666, 3.6667])

print(arr)


# In[40]:


import numpy as np

arr = np.around(3.1666)

print(arr)


# In[41]:


import numpy as np

arr = np.floor([-3.1666, 3.6667])

print(arr)


# In[42]:


import numpy as np

arr = np.ceil([-3.1666, 3.6667])

print(arr)


# In[43]:


import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))


# In[44]:


import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr)


# In[45]:


import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)


# In[48]:


import numpy as np

arr = np.array([1, 2, 3])
arr1=np.array([4,5,6])

newarr = np.cumsum((arr,arr1))

print(newarr)


# In[49]:


import numpy as np

arr = np.array([5, 6, 7, 8])

newarr = np.cumprod(arr)

print(newarr)


# In[50]:


import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr, n=2)

print(newarr)


# In[51]:


import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.unique(arr)

print(newarr)


# In[ ]:




