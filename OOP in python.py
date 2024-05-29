#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Student:
    def __init__(self):
        print("address of object is :",self)
s1=Student()
print("address of s1 is:",s1)


# In[2]:


class Student:
    def __init__(self):
        self.name="ABC"
        self.age=20
    def display(self):
        print("hello my name is",self.name,"age is:",self.age)
s1=Student()
print("details are ")
s1.display()


# In[4]:


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name",self.name,"age:",self.age)
s1=Student("Hamdan",20)
print("details are:")
s1.display()


# In[7]:


class dog:
    species="canis"
    def __init__(self,name,age):
        self.name=name
        self.age=age
d1=dog("tommy",3)
d2=dog("luna",4)
print("name of dogs are:",d1.name,"age of dog is:",d1.age,"species of dog is :",d1.species)
print("name of dogs are:",d2.name,"age of dog is:",d2.age,"species of dog is :",dog.species)
dog.__dict__


# In[8]:


class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def work(self):
        print(self.name,"is working at age",self.age)
s1=Employee("hamdan",20)
s1.work()
    


# In[9]:


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("Hamdan",20)
print(s1.name)
print(s1.age)
print("after modifications of data")
s1.name="usman"
s1.age=30
print(s1.name)
print(s1.age)


# In[12]:


class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def __display(self):
        print("name: ",self.name,"Balance :",self.__balance)
s1=bankaccount("hamdan",765324579754)
s1.display()


# In[17]:


class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def __display(self):
        print("name: ",self.name,"Balance :",self.__balance)
    def access_private(self):
        self.__display()
s1=bankaccount("hamdan",765324579754)
s1.access_private()


# In[19]:


class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
s1=bankaccount("hamdan",765324579754)
print("name: ",s1.name)
print("Balance: ",s1._bankaccount__balance)


# In[21]:


class person:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def _display(self):
        print("name:","hamdan","age:",20)
class Friend(person):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self._rollno=rollno
    def display(self):
        self._display()
        print("my rollno is:",self._rollno)
s=Friend("Usman",30,129)
s.display()


# In[23]:


class person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age
s1=person("hamdan",20)
print("name:",s1.name,"age:",s1.get_age())
s1.set_age(16)
print("name:",s1.name,"age:",s1.get_age())


# In[24]:


class vehicle:
    def vehicle(self):
        print("vehicle name")
class Car(vehicle):
    def car_info(self):
        print("inside the car")
car=Car()
car.car_info()
car.vehicle()


# In[27]:


class person:
    def person_info(self,name,age):
        print("name:",name,"age:",age)
class Company:
    def company_info(self,com_name,loc):
        print("name:",com_name,"loc:",loc)
class Child(person,Company):
    def emp(self,salary,skill):
        print("salary:",salary,"skill:",skill)
s1=Child()
s1.person_info('hamdan',23)
s1.company_info('Google','US')
s1.emp(122222,'AI')
        
    
        


# In[28]:


class person:
    def person_info(self,name,age):
        print("name:",name,"age:",age)
class Company(person):
    def company_info(self,com_name,loc):
        print("name:",com_name,"loc:",loc)
class Child(Company):
    def emp(self,salary,skill):
        print("salary:",salary,"skill:",skill)
s1=Child()
s1.person_info('hamdan',23)
s1.company_info('Google','US')
s1.emp(122222,'AI')


# In[31]:


class shopping:
    def __init__(self,basket,buyer):
        self.basket=basket
        self.buyer=buyer
    def __len__(self):
        print("redefine")
        count=len(self.basket)
        return count*2
shop=shopping(['Shoes','dress'],'Jessa')
print(len(shop))


# In[ ]:




