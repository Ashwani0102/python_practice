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
