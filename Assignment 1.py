#!/usr/bin/env python
# coding: utf-8

# 1.	Import the necessary package to
# a.	Set the current working directory
# b.	Change the working directory

# In[1]:


import my_package


# In[2]:


from my_package import test_package


# In[3]:


test_package.name


# In[4]:


test_package.email


# 2.	Create the string, int and float variable and delete them all in the next cell

# In[5]:


a = 'Koteeswaran' ; b = 10 ; c = 7.5


# In[6]:


print(a,b,c)


# In[7]:


del (a,b,c)


# In[8]:


print(a,b,c)


# 3.	What’s the result of assigning a value to a ‘keyword’?
# a.	Please highlight the error

# In[9]:


for = 'Koteeswaran'


# 4.	How to write a multi-line statement and assign it to a variable (Note: Without using a backslash “\” at the end of each line)

# In[10]:


Multi_line_variable = (12 + 15 + 22 + 
41 + 36 + 52 + 
66 + 89 + 20)
print(Multi_line_variable)


# 5.	Print the list of numbers from 100 to 999 with an interval (step size) of 8 between the numbers

# In[11]:


for i in range(100,999,8): print(i)


# 6.	Write a “for” loop to print out the ‘n’ values and break out of the statement if the value is ‘n/2’

# In[12]:


value = int(input("Please input the value:"))
for i in range(value):
    print (i/2)
    if (i == value/2):
        break


# 7.	Write a simple function and call the docstring from outside the function

# In[17]:


def multiply_function(value1,value2):
    """My first function to multiply the value given values and print the same"""
    Result = value1 * value2
    print(Result)


# In[18]:


multiply_function(3,4)


# In[19]:


print(multiply_function.__doc__)


# 8.	Create a user-defined package in ‘site-packages’ with below 3 variables a, b and c. Import these variables and write a function to calculate the area of triangle for below 3 sides (a, b, c). Calculate the semi-perimeter (s) first, to calculate the area of triangle (area) at last
# << Formula to calculate semi-perimeter: s = (a+b+c )/2
# << Formula to calculate area = (s*(s-a) * (s-b) * (s-c)) ** 0.5 >>
# a.	15
# b.	51
# c.	17

# In[20]:


from my_package import triangle_area_calc


# 9.	Write a list comprehension to print the odd numbers from 0 to 100

# In[23]:


List1 = [a for a in range(0, 100) if a%2 != 0]
print(List1)


# 10.	 Create a variable (ex: name) and store your full name in it. Then write a list comprehension to print your name excluding vowels (a, e, i, o, u)
# a.	Ex: name = Imran
# b.	Output = [‘m’, ‘r’, ‘n’]

# In[24]:


Name = [a for a in input("Please input your name: ") if a not in 'aeiou']
print(Name)


# In[ ]:




