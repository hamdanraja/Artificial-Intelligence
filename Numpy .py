#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
a= np.array([1,2,3,4,5,6])
print(a)
print(np.__version__)


# In[6]:


import numpy as np
a=np.array([1,2,3,5,4])
print(a)
print(type(a))


# In[7]:


import numpy as np
#passing tuple
a= np.array((1,2,3,4,5,6))
print(a)


# In[8]:


#dimensional arrays
import numpy as np
a=np.array([45])
print(a)


# In[9]:


import numpy as np
a=np.array([2,44,55,66,77,88])
print(a)


# In[22]:


import numpy as np
a=np.array([[45,2,3,4,55,6],[2,3,4,5,567,6]])
print(a)
print(a.ndim)


# In[21]:


import numpy as np
a=np.array([[[45,2,3,4,55,6],[2,3,4,5,567,6]],[[45,2,3,4,55,6],[2,3,4,5,567,6]]])
print(a)
print(a.ndim)# to check dimensions


# In[26]:


import numpy as np
a=np.array([2,44,55,66,77,88],ndmin =5)
print(a)
print("number of dimensions", a.ndim)


# In[29]:


#array indexing
import numpy as np
a=np.array([1,2,3,4,5,6])
print(a[5]+a[2])


# In[36]:


import numpy as np
a=np.array([[45,2,3,4,55,6],[2,3,4,5,567,6]])
print(a[1,3])


# In[33]:


import numpy as np
a=np.array([[[45,2,3,4,55,6],[2,3,4,5,567,6]],[[45,2,3,4,55,6],[2,3,4,5,567,6]]])
print(a[1,0,4])


# In[34]:


#negative indexing
import numpy as np
a=np.array([[45,2,3,4,55,6],[2,3,4,5,567,6]])
print(a[0,-1])


# In[35]:


import numpy as np
a=np.array([[[45,2,3,4,55,6],[2,3,4,5,567,6]],[[45,2,3,4,55,6],[2,3,4,5,567,6]]])
print(a[0,1,-6])


# In[39]:


import numpy as np
a= np.array([1,2,3,4,5,6])
print(a[0:4])


# In[40]:


import numpy as np
a= np.array([1,2,3,4,5,6])
print(a[0:])


# In[41]:


import numpy as np
a= np.array([1,2,3,4,5,6])
print(a[:4])


# In[42]:


import numpy as np
a= np.array([1,2,3,4,5,6])
print(a[-5:-3])


# In[43]:


import numpy as np
a= np.array([1,2,3,4,5,6,7,8])
print(a[1:6:2])


# In[65]:


import numpy as np
a= np.array([1,2,3,4,5,6,7,8])
print(a[::6])


# In[66]:


import numpy as np
a=np.array([[45,2,3,4,55,6],[2,3,4,5,567,6]])
print(a[1,0:5])


# In[67]:


import numpy as np
a=np.array([[45,2,3,4,55,6],[2,3,4,5,567,6]])
print(a[0,0:5:2])


# In[74]:


import numpy as np
a=np.array([[45,2,3,4,55,6],[2,3,4,5,567,6]])
print(a[0:2,1])


# In[75]:


import numpy as np
arr = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr[::2])


# In[80]:


import numpy as np
arr=np.array([1,2,3,4,5],dtype='S')
print(arr)
print(arr.dtype)


# In[82]:


import numpy as np
arr=np.array([1.1,2.1,3.1,4.1,5.1])
newarr=arr.astype('i')
print(newarr)
print(newarr.dtype)


# In[84]:


import numpy as np
arr=np.array([1,3,5])
newarr=arr.astype('bool')
print(newarr)
print(newarr.dtype)


# In[86]:


import numpy as np
a=np.array([1,2,3,4,5,6,7])
x=a.copy()
arr[0]=45
print(x)
print(a)


# In[90]:


import numpy as np
arr=np.array([1,2,3,4,5,6,7])
x=a.view()
arr[0]=45
print(x)
print(arr)


# In[89]:


import numpy as np
a=np.array([1,2,3,4,5,6,7])
x=a.view()
x[0]=45
print(x)
print(a)


# In[91]:


import numpy as np
a=np.array([1,2,3,4,5,6,7])
x=a.view()
y=a.copy()
print(x.base)
print(y.base)


# In[93]:


import numpy as np
a=np.array([[45,2,3,4,55,6],[2,3,4,5,567,6]])
print(a.shape)


# In[96]:


import numpy as np
a=np.array([45,2,3,4,55,6],ndmin=5)
print(a)
print(a.shape)


# In[97]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)


# In[98]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)


# In[99]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)


# In[100]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)


# In[101]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
for x in arr:
    print(x)


# In[102]:


import numpy as np

arr = np.array([[1, 2, 3, 4],[ 5, 6, 7, 8]])
for x in arr:
    print(x)


# In[104]:


import numpy as np

arr = np.array([[1, 2, 3, 4],[ 5, 6, 7, 8]])
for x in arr:
    for y in x:
        print(y)


# In[105]:


import numpy as np

arr = np.array([[[1, 2, 3, 4],[ 5, 6, 7, 8]],[[ 5, 6, 7, 8],[9,10,11,12]]])
for x in arr:
    print(x)


# In[106]:


import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)


# In[109]:


import numpy as np

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)


# In[113]:


import numpy as np

arr = np.array([[1, 2, 3, 4],[ 5, 6, 7, 8]])
for x in np.nditer(arr[:,::2]):
    print(x)


# In[120]:


import numpy as np

arr = np.array([[1, 2, 3, 4],[ 5, 6, 7, 8]])
for x in np.nditer(arr[:,::2]):
    print(x)


# In[121]:


import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
    print(idx, x)


# In[122]:


import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)


# In[124]:


import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
arr=np.concatenate((arr1,arr2))
print(arr)


# In[131]:


import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
arr=np.concatenate((arr1,arr2),axis=1)
print(arr)


# In[135]:


import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=0)
print(arr)


# In[136]:


import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)


# In[137]:


import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)


# In[138]:


import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)


# In[7]:


import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,4)
print(newarr)


# In[11]:


import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print(newarr[0])
print(newarr[1])
print(newarr[2])


# In[19]:


import numpy as np
arr=np.array([[1,2],[3,4],[5,6],[7,8]])
newarr=np.hsplit(arr,2)
print(newarr)


# In[26]:


import numpy as np
arr=np.array([1,2,3,4,5,6,7])
x=np.where(arr % 2 == 0)
print(x)


# In[27]:


import numpy as np
arr=np.array([1,2,3,4,5,6,7])
x=np.where(arr % 2 == 1)
print(x)


# In[35]:


import numpy as np
arr=np.array([1,2,3,4,5,6,7])
x=np.where(arr%2== 0)
print(x)


# In[37]:


import numpy as np
arr=np.array([1,2,3,4,5,6,7])
x=np.searchsorted(arr,7)
print(x)


# In[39]:


import numpy as np
arr=np.array([7,1,2,3,4,5,6,7])
x=np.searchsorted(arr,7,side='left')
print(x)


# In[40]:


import numpy as np
arr=np.array([1,2,3,4,5,6,7])
x=np.searchsorted(arr,[1,3,6,7])
print(x)


# In[41]:


import numpy as np

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))


# In[43]:


import numpy as np

arr = np.array([True, False, True])

print(np.sort(arr))


# In[44]:


import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))


# In[45]:


import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)


# In[47]:


import numpy as np
a=np.array([1,22,33,24,43,57,87])
filtersort=[]
for element in a:
    if element<43:
        filtersort.append(True)
    else:
        filtersort.append(False)
newarr=a[filtersort]
print(newarr)


# In[48]:


import numpy as np
a=np.array([1,22,33,24,43,57,87])
filtersort=[]
for element in a:
    if element%2==0:
        filtersort.append(True)
    else:
        filtersort.append(False)
newarr=a[filtersort]
print(newarr)


# In[49]:


import numpy as np
a=np.array([1,22,33,24,43,57,87])
filtersort=a%2==0
newarr=a[filtersort]
print(newarr)


# In[ ]:




