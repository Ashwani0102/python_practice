## Jump Game
li = [3,3,1,0,4]
jump_list = []
safe_place=len(li)-1
for i in range(len(li)-1,-1,-1):
    if i+li[i]>=safe_place:
        safe_place=i
        jump_list.append(i)
if safe_place==0:
    print("Possible")
    # print(jump_list)
    print(list(reversed(jump_list)))
else:
    print("Not Possible")
