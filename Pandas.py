#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
library={
    "name":['ali','usman','junaid','hamdan'],
    "class":[12,13,14,15],
    "sec":['cs','Ai','se','ce']
}
a=pd.DataFrame(library)
print(a)


# In[2]:


import pandas as pd
a=pd.Series([1,2,3,4,5])
print(a)


# In[3]:


import pandas as pd
em=pd.DataFrame()
print(em)


# In[4]:


import pandas as pd
data=[1,2,3,4,'hamdan']
a=pd.Series(data)
print(a)


# In[5]:


#convert numpy to pandas series
import pandas as pd
import numpy as np
numpy=np.array([1,2,3,4,5,6])
a=pd.Series(numpy)
print(a)


# In[7]:


#convert pandas to numpy
import pandas as pd
import numpy as np
pandas=pd.Series([1,2,3,4,5])
numpy=pandas.values  #variable to convert into numpy ie.values
print(numpy)


# In[9]:


import pandas as pd
data={'a':12,'b':122,'c':133,'d':155}
a=pd.Series(data)
print(a)


# In[11]:


import pandas as pd
a=pd.Series([12,13,14,15],index=['a','b','c','d'])
dict=a.to_dict()#to store series values to dict
print(dict)


# In[13]:


import pandas as pd
data=[1,2,3,4,'hamdan']
a=pd.Series(data)
b=a.tolist()
print(b)


# In[21]:


import pandas as pd
column_type={'name': str,'age':int ,'no':float}
empty_a=pd.DataFrame(columns=column_type.keys(),dtype=column_type)
print(empty_a)


# In[27]:


import pandas as pd
a= [
     ['John',30,8],
     ['allisa',40,4],
     ['hii',23,3]
]
columns_name= ['Name' , 'Age' , 'rollno']
index_no= ['person1' , 'person2' , 'person3']
df=pd.DataFrame(a, columns =columns_name ,index =index_no)
print(df)


# In[26]:


import pandas as pd

# Define the data as a list of lists
data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Define the columns and index
columns = ['Name', 'Age', 'City']
index = ['Person1', 'Person2', 'Person3']

# Create the DataFrame
df = pd.DataFrame(data, columns=columns, index=index)

print(df)


# In[32]:


import pandas as pd
columns = ['Name', 'Age', 'City']
index = ['Person1', 'Person2', 'Person3']
df = pd.DataFrame(data, columns=columns, index=index)
print(df)


# In[35]:


import pandas as pd
df=pd.DataFrame({'a':[1,2,3],'b':[4,5,6]})
a=pd.Series([7,8],name='C')
result=pd.concat([df,a],axis=1)
print(result)


# In[39]:


import pandas as pd
x=pd.DataFrame({'a':[1,2,3,4,5]})
a=x.stack()
print(a)


# In[41]:


import pandas as pd
x=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,9,10]})
data=x['a']
data2=x.iloc[:,1]
print(data)
print(data2)


# In[42]:


import pandas as pd
x=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,9,10]})
data2=x.iloc[0]
print(data2)


# In[53]:


import pandas as pd
x=pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})
x.insert(1,'C',[7,8,12])
x=x.assign(D=[9,10,11])
print(x)


# In[52]:


import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
df.insert(1, 'C', [7, 8, 9])

# Add a new column 'C' using assign()
df = df.assign(D=[7, 8, 9])

print(df)


# In[56]:


import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
df.loc[:,'C']=[7,8,9]
print(df)


# In[65]:


import pandas as pd
df=pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
},
index=['a','b','c'])
print(df.loc['a'])
print(df.loc['b','a'])
print(df.loc['a':'b'])


# In[70]:


import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Drop column 'B'
df = df.drop('B', axis=1)
print(df)


# In[75]:


import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Drop column 'B'
df = df.drop(df.columns[[1,2]], axis=1)
print(df)


# In[76]:


import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
for col in df.columns:
    if df[col].mean()>5:
        df=df.drop(col,axis=1)
print(df)


# In[77]:


import pandas as pd
df=pd.DataFrame({'A':[1,2,3,4],
                'B':[5,6,7,8],
                'c':[1,3,6,8],
                 'D':[1,5,6,8]
                })
col=df.loc[:,'B':'c'].columns
df=df.drop(col,axis=1)
print(df)


# In[78]:


import pandas as pd
df=pd.DataFrame({'A':[1,2,3,4],
                'B':[5,6,7,8],
                'c':[1,3,6,8],
                 'D':[1,5,6,8]
                })
col=df.columns[1:2]
df=df.drop(col,axis=1)
print(df)


# In[85]:


import pandas as pd
df=pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8]})
a={'A':1,'B':3}
b=df.append(a,ignore_index=True)
print(b)


# In[88]:


import pandas as pd
df=pd.DataFrame({'A':[1,2],'B':[5,6]})
df1=pd.DataFrame({'A':[3,4],'B':[7,8]})
b=df.concat([df,df1],ignore_index=True)
print(b)


# In[89]:


import pandas as pd

# Create the first DataFrame
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Create the second DataFrame
df2 = pd.DataFrame({
    'A': [7, 8, 9],
    'B': [10, 11, 12]
})

# Append rows of df2 to df1 using pd.concat
df_combined = pd.concat([df1, df2], ignore_index=True)

print(df_combined)


# In[ ]:




