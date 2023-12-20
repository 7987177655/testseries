#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q.1 Difference between Python version 2 and version 3 ? How do you check current version of python ?

# 1.xrange() used for loop in python2 and range() used for loop in python3
# 2. python version 2 work on ASCI value and python version 3 work on unicode . 
# 3 . in python version 2 print() function was not compulsory but in python version 3 print() function is compulsory . 

# checking version of python : python --version


# In[4]:


# Difference between local variable vs global variable ?examples ?
# local variables are those variable which is ddefined/created inside the function and its access is limited,
# (means we can access it only inside the function not outside the function).
# globar variable are those variable which is defined/created outside the function , 
# and we can access it inside the function and outside the function .
# example :- 
a = 10  # here a is a global variable.
def myfunc1():
    print(a)
    
def myfunc2():
    print(a)
    
# example :- 
def myfunc1():
    a = 10   # here a is a local variable. 
    print(a)
def myfunc2():
    print(a) # it will give error because a is local variable we can not access it .
    

    


# In[5]:


# What are the data types in python ?

# there are following data type which we use in python :- 
#     1 . integer data type(int) - like 10 , 20 , 30 (means all positive and negative value )
#     2. string data type(str) - like 'mohit' , 'kriti' , 'nikita' , '5' 
#     (means whatever we write inside the single qoute '' and double qoute " " called string)
#     3. float data type - like 10.20 , 30.33 (means decimal value)
#     4. boolean data type - (return true if condition is true and false in false condition )


# In[14]:


# What is difference between Mutable and Immutable Data types ? How many data types are mutable or not ?
# Please provide reason with examples?

# mutable data type -  a data type which is changeable in run time called mutable data type . 
# immutable data type - a data type which is unchangeable in run time called immutable data type . 

# mutable data type - list , dictionary , normal set(mutable)
# immutable data type - tuple , frozen set . 

# list exmaple :- 
    
a = [1,2,3,4,5,6,7] #here variable a is list and mutable because we can do changes in list .
a[1] = 3
print(a)

# dictionary example :-
a = { 'name' : 'sam' , 'class' : 'twelve' , 'school' : 'excellence'} # here variable a is a dictionary and mutable 
                                                                     #because of changes possibilities .
a['name'] = 'ram'
print(a)

# Normal Set example:- 

a = {'rahul' , 'manish' , 'anoop'} # here a is a normal set and mutable because updation is possible . 
a.add('sandhya')
print(a)


# immutable data type - like tuple and frozen set . 

# tuple example :- 

a = ( 'manish' , '5' , 'krishna' , 'bhanu') #here a is tuple and updation is not possible because it is immutable data type.
a[1] = ram
print(a)

# frozen set :-

a = frozenset({'radhika' , 'kriti' , 'ram'}) #here a is a frozenset and immutable because updation not possible in run time.
a.add('shweta')
print(a)


# In[2]:


#  Q.5 Why we use loops ? Please provide 3 examples of for loop and 3 examples of while loop ?
 
#     loop :- we use loop when we have to execute block of code multiple time ,
#     there are two type of loop 1.for loop , 2. while loop

# for loop :- we use for loop when we know how many times block of code we have to execute .(fixec condition) 
    
# example number 1. print table of 10.
for i in range(10,110,10):
    print(i)
    
#example number 2 . print number from 1-10
for i in range(1,11,1):
    print(i)
    
#example number 3 . print kriti vertically . 
a = 'kriti'
for i in a:
    print(i)
    
# while loop :- we use while loop when we dont know how many times we have to execute block of code .(condition is not fixed)
    
#example number 1 . sum of digit from 1 to n . 
i = 1
n = int(input("enter last number:")) # entered last number is 10 .
sum = 0
while(i<=n):
    sum = sum + i
    i = i+1
print("sum of digit from 1 to n is :" , sum)

# example number 2 :- sum of cube from 1 to n . 

i = 10
n = int(input("enter last number:")) # entered last number is n = 10 .
sum = 0
while(i<=n):
    sum = sum + i*i*i
    i = i + 1
print("sum of cube from 1 to n is :" , sum)

# example number 3 :- write a program for the average value of 10 number of ineger . 

i = 10
sum = 0
while(i>0):
    sum = sum + i
    i = i - 1
print("average value of 10 integer is :" , sum/10)

    


# In[27]:


# Q.6 Why we use functions ? Difference between lambda , filter , reduce , map function with examples ? 

# Functions :- we use functions to perform a specific task because every functions have their specific work . 
    
#   lambda function - it can take any number of arguments but have only one expression , 
#   filter function - in filter function items are filtered thourgh a function to test ,
#   reduce function - reduce function is used to apply a particular function passed in its argument 
#   to all of the list elements mentioned in the sequence passed along . this function is defined in the "functool" module.
#   map function - map execute a specified item for each part of the iterable . 
#   the item is sent to the functions as parameter . 

# lambda Function example :- add two number using lambda function .

x = lambda a,b : a + b
print("sum of two number is = ", x(5,7))

# Filter function example :-

ages = [2,3,4,5,20,45,22,15,18]
def myfunc(a):
    if(a<=30):
        return True
    else :
        return False
people_under_30_age = list(filter(myfunc , ages))
print("people_under_30_age = " , people_under_30_age)

# Reduce function example :-  find cumulative sum of list

from functools import reduce 
def myfunc(a,b):
    return a+b
val = [1,2,3,4,5,6]
add = reduce(myfunc , val)
print(add)

# Map functions example : - 

a = ['1','2','4','5','6','7']
b = list(map(int,a))
print(b)

a = [ 4 , 6, 9 , 10 , 20 ]
def cube(a):
    return a*a*a
b = list(map(cube , a))
print(b)


# In[13]:


# Q.7 Difference between list and tuple ?
# Please provide index() , insert() , append(), reverse() , pop() explain with examples ?

# Ans :- 1. list is collection of  different type of item or values ,tuple is also a collection of item or diffrent value
#        2. list is a mutable data type , tuple is a immutable data type .
#        3. list is identified by square bracket[] , tuple is identified by bracket () . 
#        4. list indexing start from 0 and lenth from 1 , tuple indexing start from 0 and lenth from 1 . 
        
# index() function with example :- we use this function to check the indexing of element .
    
a = [ 1, 2, 3, 4, 5,6]
a.index(2)

# insert() function with example :- this function is used to insert element at given index.

a = ['ram' , 'saurabh' , 'krati' , 'toshi']
a.insert(2,'radhika')
print(a)

# append function() with example :- this function we use to insert element in last indexing
a = ['radhika' , 'prince' , 'sachin']
a.append('manish')
print(a)

# reverse function() with example :- this function we use to reverse an element 

a = ['radhika' , 'prince' , 'sachin']
a.reverse()
print(a)

# pop function() with example :- this function we use to delet last element from the list . 

a =  ['ram' , 'saurabh' , 'krati' , 'toshi']
a.pop()
print(a)


# In[15]:


# Q.8 Difference between dictionary vs set ?Please provide keys() ,
#values() ,items() example of dictionary and union() , intersection() in sets ? Is FrozenSet is mutable or not ? 

# Ans - 1. dictionary is collection of items in keys and values which is ordered and changable and indexed,
#     set is a collection of items which is unordered , unchangable and unindexed . 

#       2. dictionary and list both identified by curly bracket {}.

a = {'name':'kriti' ,'dept':'it' , 'salary' : '50000' , 'company_name' : 'tcs'}

a.keys()  # it extract all the keys.

a.values() # it extract all the values . 

a.items() # it extract both keys and values . 


# union of sets() :- 

a = {'radhika' , 'prince' , 'sachin'}
b = {'ram' , 'saurabh' , 'krati' , 'toshi'}
c = a.union(b)
print(c)

#intersection of two sets :- 

a = {'radhika' , 'prince' , 'sachin'}
b = {'ram' , 'sachin' , 'krati' , 'radhika'}
c = a.intersection(b)
print(c)

# frozen sets is not mutable because we can not change in run time


# In[ ]:


# Q.9 What are decorators ? Please provide example ?
# Decorators are a very powerful and useful tool in Python since it allows programmers to modify 
# the behaviour of a function or class. Decorators allow us to wrap another function in order to extend 
# the behaviour of the wrapped function, without permanently modifying it.


# In[1]:


# Q.10 What is list comprehension ? Please provide example ?
#  list is a collection of different type of items and value and it is a mutable data type 
#     we identify list by square bracket [] . element is separated by commas . 
#  example - creat user defined list

a = []
size = int(input("enter size of list"))
for i in range(size):
    val = input("enter value :")
    a.append(val)
print(a)


# In[4]:


# Q.11 How do you create an array from a user defined list ?
# Ans :- 

a = []
size = int(input("enter size of list"))
for i in range(size):
    val = input("enter value :")
    a.append(val)
print(a)
import numpy as np
b = np.array(a)
b


# In[12]:


# Q.12 Difference between hstack() vs vstack() with example ?

# Ans :- when we want to add two or more array horizontally it is called hstack(). 
#     and when we want to add two or more array vertically called veritcal stacking().

# vstack example :- 
import numpy as np
a = np.array([1,2,3,4])
b = np.array([3,4,5,6])
np.vstack((a,b))  

# hstack example :- 

a = np.array(['riya' , 'ritee' , 'shweta'])
b = np.array(['pradeep' , 'anoop' , 'manish'])
np.hstack((a,b))


# In[5]:


# Q.13  What is Broadcasting in NumPy ? Please provide an example ? 
# The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.

import numpy as np
a = []
size = int(input("enter size of list"))
for i in range(size):
    val = input("enter value :")
    a.append(val)
print(a)
import numpy as np
b = np.array(a)
b 
c = np.arange(1,10)
c*2


# In[16]:


# Q.14 What is zeros() , ones() , eye() , diag() , randint() , rand() , seed(), 
# linspace() , unique() in NumPy ? please provide explanation with example ?

# zeros() : - this function creates an array either one dimensional or multi dimentional 
# and all fill all the value with zero
# example :- 
import numpy as np
b = np.zeros((5,5)) # means 5 row and 5 column . 
b

# ones() :- this function creates an array either one dimensional or multi dimentional 
# and all fill all the value with one . 

# example :- 
import numpy as np
b = np.ones((5,5)) # means 5 row and 5 column . 
b

# eye():- this function creates an array with all diagonal values are one and rest is zero . 

# example :-

c = np.eye(5,5)
c

# diag() :- in this function of array we can pass our value in diagnonal position of matrix rest will be zero . 

# example :-
d = np.array([1,2,3,4])
e = np.diag(d)
e


# randint() : - this function is used to generate random number between given range . 
# example :-

import numpy as np

f = np.random.randint(1,10 , 4)
f

#Rand() :- this function is used to generate random number between 0 to 1 . 
#example :-

import numpy as np
g = np.random.rand(4)
g

#seed () :- this function is uded to fix random number (data ) . 
import numpy as np
np.random.seed(5)
g = np.random.randint([1,5,1])
g

#lispace() : - this function return a value between given range and same gap between consecutive element . 
#example :- 
a = np.linspace(1,10,5)
a

#unique() :- this function used to return unique value and their index and their frequency count . 
#example :- 

a = np.array([10,20,10,20,30,40,30,40])
a
np.unique(a , return_index = True , return_counts = True)


# In[24]:


# Q.15 How can you reshape your array in NumPy? What is argmin() and argmax() in NumPy ? Please explain with example ?

# Ans :- with the help of reshape() method we can reshape my array
    
# for example my array size 4row and 3 coloumn 

a = np.random.randint(1,20,12)
a
a.shape
a.reshape(4,3)
a.reshape(3,4)

# Argmin() :- we use it to check indexing of minimum element/value.
a = np.array([1,2,3,4,5])
a
a.argmin()

#Argmax() :- we use it to check indexing of Maximum element/value.
a = np.array([1,2,3,4,5])
a
a.argmax()

