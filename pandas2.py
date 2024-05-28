#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.DataFrame({'A':[1,2],'B':[3,4]})
for index,row in df.iterrows():
    print(row['A'],row['B'])
    


# In[3]:


import pandas as pd
df=pd.DataFrame({'A':[1,2],'B':[3,4]})
for row in df.itertuples():
    print(row.A,row.B)
    


# In[4]:


import pandas as pd
df=pd.DataFrame({
    'ALI':[1,2,3],
    'Hamza':[5,6,7]
})
print(df)


# In[5]:


import pandas as pd

# Sample DataFrame with NaN values
df = pd.DataFrame({
    'Name': ['Alice', None, 'Charlie'],
    'Age': [25, 30, None]
})

# Casting columns to object type
df = df.astype('object')
# Replacing NaN values with an empty string
df.fillna('', inplace=True)
print(df)


# In[8]:


import pandas as pd

# Sample DataFrame with NaN values
df = pd.DataFrame({
    'Name': ['Alice', None, 'Charlie'],
    'Age': [25, 30, None]
})
df['Age'].fillna(0,inplace=True)
df['Age']=df['Age'].astype(int)
print(df)


# In[16]:


import pandas as pd

# Sample DataFrame with NaN values
df = pd.DataFrame({
    'Name': ['Alice', None, 'Charlie'],
    'Age': ['25', '30', '12']
})
df['Age']=df['Age'].astype(int)
print(df.dtypes)


# In[14]:


import pandas as pd
# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': ['25', '30', '35']  # 'Age' is initially a string
})

# Changing 'Age' column to integer type
df['Age'] = df['Age'].astype(int)
print(df.dtypes)


# In[17]:


import pandas as pd
# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]  # 'Age' is initially a string
})
selec=df[df['Age']>30]
print(selec)


# In[19]:


import pandas as pd
# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]  # 'Age' is initially a string
})
df=df[df['Age']<=30]
print(selec)


# In[ ]:


import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Current order of columns
print("Before changing column position:")
print(df)
cols=df.columns.tolist()

