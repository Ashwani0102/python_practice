# Factorial using Recursion Function
def fac(n):
    if n==0:
        return 1
    return n * fac(n-1)
print(fac(5))

# Sum of the digits using Recursion function
def sum_of_digits(n):
    if n==0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(2346))

# Print numbers using recursion as 1 to n
def print_number(n):
    if n<1:
        return 
    print_number (n-1)
    print(n)
print_number(10)

# Print numbers using recursion as n to 1
def print_number(n):
    if n<1:
        return 
    print(n)
    print_number (n-1)
print_number(10)

# Pallindrom using recursion
def pall(li,left,right):
    if li[left]!=li[right]:
        return False
    if left>right:
        return True
    return pall(li,left+1,right-1)
print(pall("madam",0,4))    

# Swapping using recursion
def swap(li,left,right):
    if left>=right:
        return
    li[left],li[right]=li[right],li[left]
    swap(li,left+1,right-1)
arr=[1,2,3,4]    
swap(arr,0,3)
print(arr)

# Table of a number till 10
def table(n):
    li=[]
    for i in range(1,11):
        li.append(n*i)
    return li
print(table(2))    

# Count the digit using recursion
def count_digit(n):
    if n==0:
        return 0
    return 1 + count_digit(n//10)
print(count_digit(1234))

# Table using recursion
def table(n,mul,limit):
    if mul>limit:
        return
    print(n*mul)
    table(n,mul+1,limit)
table(2,1,10)  

# Fabonacci Series
def fab(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        # return fab(n-1)+fab(n-2)
        a,b=0,1
        for i in range(2,n+1):
            a,b=b,a+b
        return b
def fab_series(limit):
    for i in range(limit):
        print(fab(i))        
print(fab(5))
fab_series(5)

# Power Function
def power(base,po):
    if po==0:
        return 1
    return base * power(base,po-1)
print(power(2,8))
