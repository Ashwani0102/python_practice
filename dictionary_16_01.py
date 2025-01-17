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
