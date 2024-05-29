#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
root=tk.Tk()
label=tk.Label(root,text="Hello GUI")
label.pack()
root.mainloop()


# In[3]:


import tkinter as tk
root=tk.Tk(screenName="mainscreen",baseName="hello",className="my app",useTk=1)
root.mainloop()


# In[10]:


#grid
import tkinter as tk
root=tk.Tk()
label=tk.Label(root,text="hamdan")
label.grid(row=0,column=0)
root.mainloop()


# In[12]:


import tkinter as tk
root=tk.Tk()
label=tk.Label(root,text="hamdan")
label.place(x=100,y=50)
root.mainloop()


# In[15]:


from tkinter import *
root=Tk()
frame=Frame(root)
frame.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
redbutton=Button(frame,text="red",fg="red",)
redbutton.pack(side=LEFT)
root.mainloop()


# In[16]:


import tkinter as tk
root=tk.Tk()
button=tk.Button(root,text="Hello Button")
button.pack()
root.mainloop()


# In[21]:


import tkinter as tk
from tkinter import messagebox
top=Tk()
top.geometry("100x100")
def helloCallBack():
    msg=messagebox.showinfo("hello Python","How are you")
b=Button(top,text="hello",command=helloCallBack)
b.place(x=50,y=50)
top.mainloop()


# In[23]:


import tkinter as tk
from tkinter import messagebox
top=Tk()
top.geometry("100x100")
def helloCallBack():
    msg=messagebox.showinfo("CHEAAAAA","NALLAY BEROZGAR")
b=Button(top,text="CHAPRI",command=helloCallBack)
b.place(x=40,y=50)
top.mainloop()


# In[31]:


import tkinter as tk
from tkinter import messagebox
messagebox.showinfo("information","you are in danger")
root.mainloop()


# In[33]:


import tkinter as tk
from tkinter import messagebox
messagebox.askokcancel("ok/cancel","do you want to proceed")
root.mainloop()


# In[34]:


import tkinter as tk
from tkinter import messagebox
messagebox.askyesno("yes/no","do you want to proceed")
root.mainloop()


# In[35]:


import tkinter as tk
from tkinter import messagebox
messagebox.askretrycancel("retry/cancel","kindly retry")
root.mainloop()


# In[42]:


import tkinter as tk
from tkinter import messagebox
def info():
    messagebox.showinfo("information","this is an information msg")
def error():
    messagebox.showerror("error","go back ")
def warn():
    messagebox.showwarning("warning","warning message")
def ask_questions():
    response=messagebox.askquestions("questions","do you want to proceed")
    print("response: ",response)
def yesorno():
    answer=messagebox.askyesno("yes/no","do you want to proceed")
    print("answer: ",answer)
def ok():
    answer=messagebox.askokcancel("ok/cancel","do you want to proceed")
    print("answer: ",answer)
def hi():
    answer=messagebox.askretrycancel("retry/cancel","do you want to proceed")
    print("answer: ",answer)    
root.mainloop()    


# In[43]:


import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("Information", "This is an information message")

def show_warning():
    messagebox.showwarning("Warning", "This is a warning message")

def show_error():
    messagebox.showerror("Error", "This is an error message")

def ask_question():
    response = messagebox.askquestion("Question", "Do you like Python?")
    print("Response:", response)

def ask_ok_cancel():
    response = messagebox.askokcancel("Ok/Cancel", "Do you want to proceed?")
    print("Response:", response)

def ask_yes_no():
    response = messagebox.askyesno("Yes/No", "Do you agree?")
    print("Response:", response)

def ask_retry_cancel():
    response = messagebox.askretrycancel("Retry/Cancel", "Do you want to retry?")
    print("Response:", response)

root = tk.Tk()
root.title("Tkinter Messagebox Example")

info_button = tk.Button(root, text="Show Info", command=show_info)
info_button.grid(row=0, column=0)

warning_button = tk.Button(root, text="Show Warning", command=show_warning)
warning_button.grid(row=0, column=1)

error_button = tk.Button(root, text="Show Error", command=show_error)
error_button.grid(row=0, column=2)

question_button = tk.Button(root, text="Ask Question", command=ask_question)
question_button.grid(row=1, column=0)

ok_cancel_button = tk.Button(root, text="Ask Ok/Cancel", command=ask_ok_cancel)
ok_cancel_button.grid(row=1, column=1)

yes_no_button = tk.Button(root, text="Ask Yes/No", command=ask_yes_no)
yes_no_button.grid(row=1, column=2)

retry_cancel_button = tk.Button(root, text="Ask Retry/Cancel", command=ask_retry_cancel)
retry_cancel_button.grid(row=2, column=0)

root.mainloop()


# In[44]:


from tkinter import *
root = Tk()
entry = Entry(root, width=30)
entry.pack()
root.mainloop()


# In[49]:


import tkinter as tk
root=tk.Tk()
entry=Entry(root,width=50)
entry.pack()
root.mainloop()


# In[53]:


import tkinter as tk
root=tk.Tk()
frame=tk.Frame(root,name="hi",bg="blue",bd=2,relief=tk.SOLID)
frame.pack()
label=tk.Label(frame,text="this is label inside me",bg="blue",fg="white")
label.pack(padx=10,pady=5)
butt=tk.Button(frame,text="click me")
butt.pack(padx=10,pady=5)
root.mainloop()


# In[54]:


import tkinter as tk
root=tk.Tk()
label=tk.Label(root,text="this is label inside me",bg="blue",fg="white")
label.pack(padx=10,pady=5)
root.mainloop()


# In[58]:


import tkinter as tk
root=tk.Tk()
listbox=tk.Listbox(root)
for items in["apple","banana","cheery"]:
    listbox.insert(tk.END,items)
listbox.pack()
root.mainloop()


# In[60]:


import tkinter as tk

# Create the main application window
root = tk.Tk()

# Create a Menu widget
menu = tk.Menu(root, tearoff=False)  # tearoff=False prevents the menu from being detached

# Add items to the Menu
menu.add_command(label="Option 1")
menu.add_command(label="Option 2")
menu.add_command(label="Option 3")

# Create a Menubutton widget
menubutton = tk.Menubutton(root, text="Options")

# Attach the Menu to the Menubutton
menubutton.config(menu=menu)

# Pack the Menubutton widget to make it visible in the window
menubutton.pack()

# Start the Tkinter event loop
root.mainloop()


# In[1]:


import tkinter as tk

def hello():
    print("Hello!")

def quit_app():
    root.quit()

# Create the main application window
root = tk.Tk()
#Create a top-level menu
menubar= tk.Menu(root)

# Create a File menu
file_menu= tk.Menu(menubar, tearoff=0)

file_menu.add_command(label="New", command=hello)
file_menu.add_command(label="Open", command=hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_app)

# Create an Edit menu
edit_menu = tk.Menu(menubar, tearoff=0)

edit_menu.add_command(label="Cut", command=hello)
edit_menu.add_command(label="Copy", command=hello)
edit_menu.add_command(label="Paste", command=hello)
#Add the File and Edit menus to the menubar
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
# Configure the root window to use the menubar
root.config(menu=menubar)
root.mainloop()


# In[3]:


import tkinter as tk
root=tk.Tk()
message=tk.Message(root,text="this is a multiline message box .you can eassyliy remember it")
message.pack()
root.mainloop()


# In[6]:


import tkinter as tk

def hello():
    print("hello")
def quit():
    root.quit
root=tk.Tk()
menu=tk.Menu(root)
file_menu=tk.Menu(menu,tearoff=0)
file_menu.add_command(label="New",command=hello)
file_menu.add_command(label="open",command=hello)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quit)
edit_menu = tk.Menu(menu, tearoff=0)

edit_menu.add_command(label="Cut", command=hello)
edit_menu.add_command(label="Copy", command=hello)
edit_menu.add_command(label="Paste", command=hello)
#Add the File and Edit menus to the menubar
menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Edit", menu=edit_menu)
# Configure the root window to use the menubar
root.config(menu=menu)
root.mainloop()
    


# In[8]:


import tkinter as tk
from tkinter import ttk

def show_selected_option():
    print(f"Selected option: {selected_option.get()}")

# Create the main application window
root = tk.Tk()
root.title("Tkinter Radio Button Example")

# Define a Tkinter variable to hold the value of the selected radio button
selected_option = tk.IntVar()
selected_option.set(1)  # Setting a default value

# Create Radio Button widgets
radio1 = ttk.Radiobutton(root, text="Option 1", variable=selected_option, value=1)
radio2 = ttk.Radiobutton(root, text="Option 2", variable=selected_option, value=2)
radio3 = ttk.Radiobutton(root, text="Option 3", variable=selected_option, value=3)

# Arrange the Radio Buttons using the pack geometry manager
radio1.pack(anchor=tk.W)
radio2.pack(anchor=tk.W)
radio3.pack(anchor=tk.W)

# Create a button to display the selected option
button = tk.Button(root, text="Show Selected Option", command=show_selected_option)
button.pack()

# Start the Tkinter event loop
root.mainloop()


# In[9]:


import tkinter as tk
def show(value):
    print(f"selected value:{value}")
root=tk.Tk()
root.title("scale")
scale=tk.Scale(root,from_=0,to_=100,orient=tk.HORIZONTAL,command=show)
scale.pack()
root.mainloop()


# In[10]:


import tkinter as tk
root=tk.Tk()
text=tk.Text(root)
text.pack()
text.insert(tk.END,"hello","how are you")
root.mainloop()


# In[12]:


import tkinter as tk
root=tk.Tk()
text=tk.Spinbox(root,from_=0,to_=100)
text.pack()
root.mainloop()


# In[14]:


import tkinter as tk
root=tk.Tk()
pw=tk.PanedWindow(root,orient=tk.HORIZONTAL)
left=tk.Label(pw,text="left")
right=tk.Label(pw,text="right")
pw.add(left)
pw.add(right)
pw.pack(fill=tk.BOTH,expand=True)
root.mainloop()


# In[ ]:




