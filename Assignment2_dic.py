# Factorial of number from 1 to 10 and store in dictionary
d = {}
fac=1
a=1
for i in range(1,11):
    while a<=i:
        fac=fac*a
        a=a+1
    d[f'Factorial of {i}'] = fac
print(d)    
# output: {'Factorial of 1': 1,'Factorial of 2': 2,'Factorial of 3': 6,'Factorial of 4': 24,'Factorial of 5': 120,'Factorial of 6': 720, 'Factorial of 7': 5040, 'Factorial of 8': 40320, 'Factorial of 9': 362880, 'Factorial of 10': 3628800} 

# Find Duplicate Numbers
li = [4,3,6,2,1,6,3,4]
d ={}
d1 = {}
for i in li:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for key,value in d.items():
    if value>=2: 
        d1[key]=value
print(d1)                   
# Output : {4: 2, 3: 2, 6: 2} 

# Most Frequent Element
li = [1,3,2,1,5,1,3,2,2]
d={}
max_count=0
for i in li:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for key,value in d.items():
    if value>max_count:
        max_count=value
        most_frequent_element=key
print("Most Frequent Element is",most_frequent_element,"appeared",max_count,"times")  
# Output : Most Frequent Element is 1 appeared 3 times

# Find common element in mutliple list using dictionary
list1 = [1,2,3,4]
list2 = [2,3,5,6]
list3 = [3,7,8,2]
d = {}
d1= {}
d2= {}
for i in list1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in list2:
    if i in d:
        if i in d1:   
            d1[i]+=1
        else:
            d1[i]=1 
for i in list3:
    if i in d1:
        if i in d2:   
            d2[i]+=1
        else:
            d2[i]=1                                       
keys_list=list(d2.keys())
print(keys_list)
# Output : [3, 2]

# Find missing number from a list
li = [1,2,3,4,5,6,7,9,10]
full_set=set(range(1,11))
current_set=set(li)
missing_number=full_set-current_set
print("The missing element is",missing_number)
# Output : The missing element is {8}

# Find common element in mutliple list using set
list1 = [1,2,3,4]
list2 = [2,3,5,6]
list3 = [3,7,8,2]
set1 = set(list1)
set2 = set()
set3 = set()
for i in list2:
    if i in set1:
        set2.add(i)
for i in list3:
    if i in set2:
        set3.add(i)
print(set3)  
# Output = {2, 3}

# Count the frequency of element in a list
li = [1,2,2,3,3,3,4]
d = {}
for i in li:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1    
print(d) 
# # Output : {1: 1, 2: 2, 3: 3, 4: 1}

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
# # Output : {'a': 1, 'b': 3, 'c': 1}

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
# # Output : {3: ['cat', 'dog', 'bat'], 8: ['elephant']}  

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
# # Output : Max frequency amoung the character is : a having count as : 2

# Invert a dictionary
d1={'a':1,'b':2,'c':1}
d ={}
for key,value in d1.items():
    if value in d:
       d[value].append(key) 
    else:
        d[value]=[key]
print(d) 
# # Output : {1: ['a', 'c'], 2: ['b']} 
