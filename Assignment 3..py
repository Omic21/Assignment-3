#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Q 2. 
# Sample input: '1234abcd'
# Sample output:'dcba4321'

def value_reverse(value):
    reverse= value[::-1]
    print(reverse)
    
sample_input = '1234abcd'
result = value_reverse(sample_input)


# In[41]:


# Q 3.


string : 'The quick Brow Fox'

    
upper, lower = 0, 0

for a in string:
    #first we've to count the total number of upper case characters in the string
    if (a.isupper()):
        upper = upper + 1
     #then we've to count the total number of lower case characters in the string   
    elif (a.islower()):
        lower = lower +1
        
print("No. of upper case characters", upper)
print("No. of lower case characters", lower)


# In[14]:


# Q.1

# l = (8, 2, 3, 0, 7)
# print(sum(l))

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total 
    
    
# l = (8, 2, 3, 0, 7)
print(sum((8,2,3,0,7)))


# In[ ]:





# In[ ]:




