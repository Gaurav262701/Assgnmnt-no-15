#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Answer no 1
def numGenerator(n):
    for i in range(n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i
            
n = int(input())
values = []
for i in numGenerator(n):
    values.append(str(i))
    
print(",".join(values))


# In[4]:


#Answer no 2
def evenGenerator(n):
    i=0
    while i<=n:
        if i % 2 == 0:
            yield i
        i+=1
n = int(input())
values = []
for i in evenGenerator(n):
    values.append(str(i))
print(",".join(values))


# In[7]:


#Answer no 3
nTerms = int(input("how many terms?"))
n1,n2 = 0,1
count = 0 
if nTerms <= 0:
    print("plz enter a +ive number")
elif nTerms == 1:
    print("fibonacci sequence up to ",nterms)
    print(n1)
else:
    print("fibonacci sequence:")
    while count < nTerms:
        print(n1)
        nth = n1 + n2
        n1 = n2 
        n2 = nth
        count +=1


# In[10]:


#Answer no 4
test = "john@google.com"
print("The original string is:"+str(test))
res = test.split('@')[0]
print("The extracted domain name:"+str(res))


# In[12]:


#Answer no 5
class shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class square(shape):
    def __init__(self,lenght = 0):
        shape.__init__(self)
        self.lenght = lenght
        
    def area(self):
        return self.lenght*self.lenght
    
Asqr = square(3)
print(Asqr.area())
        
        


# In[ ]:




