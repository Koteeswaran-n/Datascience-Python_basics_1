#!/usr/bin/env python
# coding: utf-8

# ### 1. Get the input for 2 variables though “input” function and pass them to a function to return the addition of two variables

# In[1]:


def add_function(input1,input2):
    """This function will add given two numbers and return the Sum"""
    Sum=input1+input2
    return Sum


# In[2]:


Value1 = int(input("Please enter number 1: "))
Value2 = int(input("Please enter number 2: "))
Add_value = add_function(Value1,Value2)
print("Sum of Two given numbers is : ", Add_value)


# ### 2. What happens if we try to add an int with str and vice versa. Please print out the error

# #### a) Adding Integer with String

# In[3]:


Value1 = int(input("Please enter number 1: "))
Value2 = int(input("Please enter number 2: "))
Add_value = add_function(Value1,Value2)
print("Sum of Two given numbers is : ", Add_value)


# In[5]:


Value1 = input("Please enter number 1: ")
Value2 = input("Please enter number 2: ")
Add_value = add_function(Value1,Value2)
print("Sum of Two given numbers is : ", Add_value)


# In[6]:


Value1 = int(input("Please enter number 1: "))
Value2 = input("Please enter number 2: ")
Add_value = add_function(Value1,Value2)
print("Sum of Two given numbers is : ", Add_value)


# #### b) Adding String With Integer

# In[7]:


Value1 = input("Please enter number 1: ")
Value2 = input("Please enter number 2: ")
Add_value = add_function(Value1,Value2)
print("Sum of Two given numbers is : ", Add_value)


# In[8]:


Value1 = input("Please enter number 1: ")
Value2 = int(input("Please enter number 2: "))
Add_value = add_function(Value1,Value2)
print("Sum of Two given numbers is : ", Add_value)


# ### 3. Create a string variable for the word “Data Science” and see if the letter “s” is present in it using membership operators

# In[9]:


String_val = 'Data Science'
input_val = input("Please enter the letter to find if it is present :")
if input_val in String_val:
    print("Given letter is Present")
else:
    print("Given letter is NOT Present")


# In[10]:


input_val = input("Please enter the letter to find if it is present :")
if input_val in String_val:
    print("Given letter is Present")
else:
    print("Given letter is NOT Present")


# ### 4. Write a function and pass a number list as an argument to the function. And return True if the first and last number of a given list is same. If numbers are different then return False

# In[11]:


def funct_List_compare(arg1):
    """Function to compare return True if the first and last number of a given list is same. If numbers are different then return False"""
    print(arg1)
    if arg1[0] == arg1[-1]:
        print("First and last number of the given list is same")
        return True
    else:
        print("First and last number of the given list is different")
        return False


# In[12]:


List1 = [1,2,3,4,5]
funct_List_compare(List1)


# In[13]:


List2 = [1,2,3,4,1]
funct_List_compare(List2)


# ### 5. Iterate the given list of numbers (l1) and print only those numbers which are divisible by 5. (l1 = [10, 20, 33, 46, 55])

# In[14]:


l1 = [10,20,33,46,55]
list_iter = [i for i in l1 if i%5 == 0]
print("The numbers which are divisible by 5 are :", list_iter)


# ### 6. Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

# #### a. Hint: Separate return values with a comma

# In[19]:


def calculation(arg1,arg2):
    """Function to return addition and subtraction results of the values passed"""
    print("The first value entered is : ", arg1)
    print("The second value entered is : ", arg2)
    ## Addition 
    Add_result = arg1 + arg2
    ## Subtraction
    Sub_result = arg1 - arg2
    if Sub_result < 0:
        Sub_result = Sub_result * -1
    
    ## Returning the results
    return Add_result, Sub_result


# In[17]:


input1 = int(input("Enter the First Number : "))
input2 = int(input ("Enter the Second Number : "))

add_value, sub_value = calculation(input1,input2)

print("Calculated value for Addition of 2 given numbers is : ", add_value)
print("Calculated value for Subtraction of 2 given numbers is : ", sub_value)


# In[18]:


## When the input value 2 is greater than first value entered 

input1 = int(input("Enter the First Number : "))
input2 = int(input ("Enter the Second Number : "))

add_value, sub_value = calculation(input1,input2)

print("Calculated value for Addition of 2 given numbers is : ", add_value)
print("Calculated value for Subtraction of 2 given numbers is : ", sub_value)


# ### 7. Write a program to demonstrate the following Syntax error

# #### a. SyntaxError: non-default argument follows default argument

# In[20]:


def syn_err_arg(var1 = 'Koteeswaran', var2):
    print("First argument :", var1)
    print("Second argument :", var2)


# In[21]:


def syn_err_arg(100, var2):
    print("First argument :", var1)
    print("Second argument :", var2)


# In[22]:


def syn_err_arg(var1 = 100, var2):
    print("First argument :", var1)
    print("Second argument :", var2)


# ### 8. What’s recursion? Explain in your own words and write a program to create a recursive function to calculate the sum of numbers from 0 to 10

# Recursion is a repeated action being performed or a function which can call itself to perform any repreated operation

# In[27]:


def recursion_add(arg1):
    """recursion function to add sum of number given and the below numbers"""
    ##print("The number entered is : ", arg1)
    if arg1 <=0:
        print("The entered number should be greater than Zero")
        return
    elif arg1 == 1:
        return arg1
    else:
        return (arg1 + recursion_add(arg1-1))


# In[28]:


input1 = int(input("Enter the number : "))
result = recursion_add(input1)
print("The sum of numbers is : ", result)


# In[29]:


input1 = int(input("Enter the number : "))
result = recursion_add(input1)
print("The sum of numbers is : ", result)


# ### 9. Use filter and lambda function to calculate square for below numbers only if they are odd number
# ### a. [12, 11, 53, 22, 21, 77, 87, 88, 98]

# In[2]:


lista = [12, 11, 53, 22, 21, 77, 87, 88, 98]
list_odd = list(filter(lambda x:x%2 != 0, lista))
print(list_odd)


# In[3]:


list_square = list(map(lambda x: x*x,list_odd))
print(list_square)


# In[4]:


lista = [12, 11, 53, 22, 21, 77, 87, 88, 98]
list_odd = list(filter(lambda x:x%2 != 0, lista))
list_square = list(map(lambda x: x*x,list_odd))
print(list_square)


# In[5]:


list_square = list(map(lambda x: x*x,list(filter(lambda x:x%2 != 0, lista))))
print(list_square)


# ### 10. Write a function (not a lambda function) and use it to demonstrate an example for map function (any logical function of your choice)

# In[6]:


def map_function(list5):
    """This is a logical function similar to perform the same operation of map operation in question 9"""
    print("The elements in list are :",list5)
    list_square = []
    for i in list5:
        if (i%2 != 0):
            list_square.append(i*i)
        else:
            continue
    return list_square


# In[7]:


listb = [12, 11, 53, 22, 21, 77, 87, 88, 98]
output = map_function(listb)
print("output of square of odd number from the given list", output)


# In[ ]:




