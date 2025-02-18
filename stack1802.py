# Parenthesis
stack = []
dic = { '[':']', '{':'}', '(':')' }
s="[{()}()]"
for i in s:
    if i in dic:
        stack.append(i)
    else:
        if dic[stack[-1]]==i:
            stack.pop()
        else:
            print("False")
            break
if len(stack)==0:
    print("True")  
