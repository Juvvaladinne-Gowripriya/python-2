#!/usr/bin/env python
# coding: utf-8

# In[7]:


a=input()
match a:
    case "hello":
        print("Hello All")
    case "Bye":
        print("Bye All")
    case other:
        print("Invalid Input")
        


# # Swap two numbers without using third variable

# In[8]:


a=int(input())
b=int(input())
a,b=b,a
print(a)
print(b)


# In[9]:


a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print(a)
print(b)


# In[10]:


a=int(input())
b=int(input())
a=a^b
b=a^b
a=a^b
print(a)
print(b)


# # using match (like switch)

# In[6]:


a=int(input())
b=int(input())
n=int(input())
match n:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a/b)
    case 4:
        print(a%b)
    case 5:
        print(a*b)
    case 6:
        print(a//b)
    case 7:
        print("EXIT")


# In[16]:


import math
for i in range(1,10,1):
    print((i))


# # STRINGS

# In[1]:


a=input()
print(a)


# In[2]:


a=input()
print(a.upper())


# In[3]:


a=input()
print(a.lower())


# In[4]:


a=input()
print(a.swapcase())


# In[5]:


a=input()
print(a.isalpha())


# In[6]:


a=input()
print(a.isdigit())


# In[9]:


a=input()

print("letters:",len(a))


# #                                  #functions#

# In[6]:


def add(n1,n2):
    sum=n1+n2
    print(sum)
add(5,5)


# In[14]:


a=int(input())
b=int(input())


def operation(a,b):
    print("addition of",a,"and",b,"is :",a+b)
    print("subtraction of",a,"and",b,"is :",a-b)
    print("multiplication of",a,"and",b,"is :",a*b)
    print("division of",a,"and",b,"is :",a/b)
    print("modulo of",a,"and",b,"is :",a%b)
    print("floor of",a,"and",b,"is :",a//b)
operation(a,b)


# In[ ]:




