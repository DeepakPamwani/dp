#!/usr/bin/env python
# coding: utf-8

# # TASK 1
# 

# 1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce() 
#  
#  

# In[10]:


def myreduce(func, list):
    result = list[0]
    for i in list[1:]:
        result = func(result, i)
    return result


# In[11]:


def sum(a,b):
    return a+b


# In[12]:


sum(4,5)


# In[13]:


l= [4,5,6,7]


# In[14]:


myreduce(sum, l)


# 1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter() 

# In[15]:


def myfilter(function, list_1):
    result = []
    for i in list_1:
        if function(i):
            result.append(i)
    return result        


# In[16]:


c = [2,8,9,10]


# In[17]:


list(myfilter(lambda x: x%2==0, c))


# 2. Implement List comprehensions to produce the following lists. 
#  
#    
#  Write List comprehensions to produce the following Lists 
#  
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’] 
#  
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] 
#  
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz'] 
# 
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
#  
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] 
#  
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)] 

# In[18]:


#2.1 ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]

word = 'ACADGILD'
p =[]

for i in  'ACADGILD':
    p.append(i)
print(p)    


# In[19]:


#2.2 ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] 

g= []
for i in 'xyz':
    for j in range(1,5):
        g.append(i*j)
    
print(g)    


# In[20]:


[i*j for j in range(1,5) for i in 'xyz']


# In[21]:


# 2.3 ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']

h =[]
for i in ['x', 'y', 'z']:
    for j in range(1,5):
        h.append(i*j)
         
print(h)           
        


# In[22]:


[i * j for j in range(1, 5) for i in ['x', 'y', 'z']]


# In[23]:


#2.4 [[2], [3], [4], [3], [4], [5], [4], [5], [6]] 

[[i + j] for j in [0, 1, 2] for i in range(2, 5)]


# In[24]:



# 2.5 [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] 
[[i + j for j in [0, 1, 2, 3]] for i in range(2, 6)]


# In[25]:



#2.6 [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)] 

[(i,j) for j in [1, 2, 3] for i in [1, 2, 3]]


# In[ ]:





# 3. Implement a function longestWord() that takes a list of words and returns the longest one. 
#  
#  

# In[26]:


def longestWord():
    a = input('Please Input the list of words:')
    longest = 0
    
    for i in a.split():
        if len(i) > longest:
            longest = len(i)
    print('The Longest word is in list is', i, 'with lengh', longest)


# In[27]:


longestWord()


# # TASK 2

# 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below formula. 
#  
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 
#  
# Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass. 
#  
#  

# In[28]:


x =5


# 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are 
# longer than n. 

# In[29]:


def filter_long_words(words, n):
    return filter(lambda x: len(x) > n, words)


list(filter_long_words(['trust', 'ab', 'should'], 3))            


# In[ ]:





# 2.1 Write a Python program using function concept that maps  list of words into a list of integers representing the lengths of the corresponding words​. 
#  Hint: ​If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4] 
#  Here 2,3 and 4 are the lengths of the words in the list. 

# In[30]:


words = ['ab', 'cde', 'erty']

def wordlenth(words):
    
    
    return list(map(lambda x : len(x), words))
print(str(wordlenth(words)))


# In[ ]:





# 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise. 

# In[31]:


def vowel(char):
    if char.lower() in 'aeiou':
        return True
    if char.upper() in 'AEIOU':
        return TRUE
    else:
        return False


# In[32]:


vowel('A')


# In[ ]:





# In[ ]:





# In[ ]:




