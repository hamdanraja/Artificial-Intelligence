#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print("name is:",self.name,"age is:",self.age,"gender is:",self.gender)
class Student(Person):
    def __init__(self,name,age,gender,Class,rollno):
        super().__init__(name,age,gender)
        self.Class=Class
        self.rollno=rollno
    def display_student(self):
        self.display()
        print("class is:",self.Class,"rollno is",self.rollno)
class teacher(Person):
    def __init__(self,name,age,gender,subject,experience):
        super().__init__(name,age,gender)
        self.subject=subject
        self.experience=experience
    def display_teacher(self):
        self.display()
        print("class is:",self.subject,"rollno is",self.experience) 
class admin(Student,teacher):
    def __init__(self, name, age, gender, rollno, Class, subject, experience, salary, position):
        student.__init__(self, name, age, gender, rollno, Class)
        teacher.__init__(self, name, age, gender, subject, experience)
        self.salary = salary
        self.position = position

    def display_admin_info(self):
        self.display()
        self.display_student()
        self.display_teacher()
        print(f"Salary: {self.salary}")
        print(f"Position: {self.position}")
print("Enter student info:")
Student_Name=input("enter your name")
Student_Age=int(input("enter your age"))
Student_Gender=input("enter your Gender")
Student_Class=int(input("enter your class"))
Student_Rollno=int(input("enter your rollno"))

print("Enter Teachers info")
Teacher_Name=input("enter your name")
Teacher_Age=int(input("enter your age"))
Teacher_Gender=input("enter your Gender")
Teacher_Subject=input("enter your subject")
Teacher_experience=int(input("enter your experience"))

print("Enter Admins info")
admin_Name=input("enter your name")
admin_Age=int(input("enter your age"))
admin_Gender=input("enter your Gender")
admin_Subject=input("enter your subject")
admin_experience=int(input("enter your experience"))
admin_salary=int(input("enter your experience"))
admin_position=input("enter your experience")


s1 = student(student_Name, student_Age, student_Gender, student_Rollno, student_Class)
s2 = teacher(Teacher_Name, Teacher_Age, Teacher_Gender, Teacher_Subject, Teacher_experience)
s3 = admin(admin_Name, admin_Age, admin_Gender, admin_Subject, admin_experience, admin_salary, admin_position)

print("\nStudent Information:")
student.display_student()

print("\nTeacher Information:")
teacher.display_teacher()

print("\nAdmin Information:")
admin.display_admin()


# In[14]:


class Account:
    def __init(self,acc_no,balance,holder_name):
        self.acc_no=acc_no
        self.balance=balance
        self.holder_name=holder_name
    def deposit(amount):
        self.balance+=amount
        print(f"Deposited {amount} into account {self.acc_no}. New balance: {self.balance}")
    def withdraw(amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.acc_no}. New balance: {self.balance}")
        else:
            print(f"Insufficient funds in account {self.acc_no}. Current balance: {self.balance}")
            
class SavingsAccount(Account):
    def __init__(self,acc_no,balance,holder_name, interest_rate):
        super().__init__(acc_no, balance,holder_name)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest of {interest} added to account {self.account_number}. New balance: {self.balance}")

class CurrentAccount(Account):
    def __init__(self, acc_no, balance,holder_name, overdraft_limit):
        super().__init__(acc_no, balance,holder_name)
        self.overdraft_limit = overdraft_limit

    def check_overdraft(self, amount):
        return self.balance + self.overdraft_limit >= amount

    def withdraw(self, amount):
        if self.check_overdraft(amount):
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.acc_no}. New balance: {self.balance}")
        else:
            print(f"Insufficient funds in account {self.acc_no}. Current balance: {self.balance}")

# Create instances of each class
savings_account = SavingsAccount("SA001", 5000, "John Doe", 5.0)
current_account = CurrentAccount("CA001", 10000, "Jane Smith", 2000)

# Perform banking operations
savings_account.deposit(1000)
savings_account.calculate_interest()
savings_account.withdraw(2000)

current_account.deposit(500)
current_account.withdraw(8000)
current_account.withdraw(5000)


# In[15]:


class Account:
    def __init__(self, account_number, balance, account_holder_name):
        self.account_number = account_number
        self.balance = balance
        self.account_holder_name = account_holder_name

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print(f"Insufficient funds in account {self.account_number}. Current balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance, account_holder_name, interest_rate):
        super().__init__(account_number, balance, account_holder_name)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest of {interest} added to account {self.account_number}. New balance: {self.balance}")

class CurrentAccount(Account):
    def __init__(self, account_number, balance, account_holder_name, overdraft_limit):
        super().__init__(account_number, balance, account_holder_name)
        self.overdraft_limit = overdraft_limit

    def check_overdraft(self, amount):
        return self.balance + self.overdraft_limit >= amount

    def withdraw(self, amount):
        if self.check_overdraft(amount):
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print(f"Insufficient funds in account {self.account_number}. Current balance: {self.balance}")

# Create instances of each class
savings_account = SavingsAccount("SA001", 5000, "John Doe", 5.0)
current_account = CurrentAccount("CA001", 10000, "Jane Smith", 2000)

# Perform banking operations
savings_account.deposit(1000)
savings_account.calculate_interest()
savings_account.withdraw(2000)

current_account.deposit(500)
current_account.withdraw(8000)
current_account.withdraw(5000)


# In[16]:


class Employee:
    def __init__(self):
        return 0
class Manager(Employee):
    def __init__(self,base_salary,bonus):
        self.base_salary=base_salary
        self.bonus=bonus
    def calculate_salary(self):
        return self.base_salary+self.bonus
class Developer(Employee):
    def __init__(self,hourly_wage,hours_work):
        self.hourly_wage=hourly_wage
        self.hours_work=hours_work
        
    def calculate_salary(self):
        return self.hourly_wage*self.hours_work 
class Designer(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary
    
    def calculate_salary(self):
        return self.monthly_salary
s1=Manager(base_salary=100000,bonus=20000) 
s2=Developer(hourly_wage=4000000,hours_work=10)
s3=Designer(monthly_salary=250000)
manager_salary = s1.calculate_salary()
developer_salary =s2.calculate_salary()
designer_salary = s3.calculate_salary()

# Output results
print("Manager's Salary:", manager_salary)
print("Developer's Salary:", developer_salary)
print("Designer's Salary:", designer_salary)


# In[ ]:




