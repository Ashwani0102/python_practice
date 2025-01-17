# Program to find whether any 2 no's sum in an array equals target using dictionary
li=[2,3,5,7]
target = 10
flag = False
d = {}
for i in range(len(li)):
    d[li[i]]=i
for i in range(len(li)):
    search_element = target-li[i]
    if search_element in d  and i != d[search_element]:
        flag = True
        print(i,d[search_element])
        break
if flag==False:
    print("Not Possible")  

# Random Number Generate
import random
count=0
while True:
    num=random.randint(0,6)
    count=count+1
    print("Random numbers generate is",num)
    if num==5:
        break 
print("Count after which we got the desired number is ",count)

# Saving index as well as value using loop in dictionary
li =[1,2,3,4,5,6]
d={}
for i in range(len(li)):
    d[li[i]]=i
print(d)  

# Finding the character count from a given string
s="ashwani"
d={}
for i in s:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1   
print(d)   

# Finding the vowels character count only from a string using dictionary 
s="ashwani"
d={}
vowels ={"a","e","i","o","u"}
for i in s:
    if i in vowels:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
print(d)

# Count the frequency of element in a list
li = [1,2,2,3,3,3,4]
d = {}
for i in li:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1    
print(d) 

# Merge 2 dictionary
d1={"a":1,"b":2}
d2={"b":1,"c":1} 
d={}
for key,value in d1.items():
    # d[key]=d1.get(key,value)
    d[key]=value
for key,value in d2.items():
    if key not in d:
        d[key]=value
    else:
        d[key]=d[key] +1       
print(d)

# Group words by length in dictionary where keys are the lengths of words and value are lists of words of that length
words =['cat','dog','elephant','bat']
d = {}
for i in words:
    length=len(i)
    if length in d:
        d[length].append(i)
    else:
        d[length]=[i]    
print(d) 

# Most Frequent Character in a String
word="ashwani"
d={}
for i in word:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
max_count=0
max_frequent_charater =""
for key,value in d.items():
    if value>max_count:
        max_count=value
        max_frequent_charater=key
print("Max frequency amoung the character is :",max_frequent_charater,"having count as :",max_count) 

# Invert a dictionary
d1={'a':1,'b':2,'c':1}
d ={}
for key,value in d1.items():
    if value in d:
       d[value].append(key) 
    else:
        d[value]=[key]
print(d) 
