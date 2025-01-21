# Multiplication table of a number till 10
number = int(input("Enter the number for multiplication table :")) #Input asked from user
for i in range(1,11): # Loop initilizing from 1 to 10
     output=number*i   # Multiplying number
     print(number,"*",i,"=",output) #Output

# Array Sum and Average
number = int(input("Enter the number for calculating sum of array and average :")) #Input asked from user
sum=0 # Initilizing initial value to 0
i=1   # Initilizing the loop to start from 1
while i<=number: # Loop set to run from 1 to input number
     sum=sum+i    # Suming up the input number
     i=i+1        # Incremental the value of i to 1
average=sum/number # Calculating average of number in float
# Output the results
print("The sum of numbers in an array till input number is :",sum)
print("The average of numbers in an array till input number is :",average)

# Maximum and Minimum in an array
smallest=float('inf')  # Initialize smallest to positive infinity
largest=float('-inf')  # Initialize largest to negative infinity
while True:  # Starting a Infinite Loop
    number = int(input("Enter the numbers to find the smallest and largest among those(Negative number to stop):")) #Input
    if number<1:  # Check if the entered number is negative
        break     # Exit the loop if a negative number is entered
    elif number < smallest: # Check if the number is smaller than the current smallest
        smallest=number     # Update smallest if a smaller number is found
    else:
        largest=number      # Update largest if a larger number is found
# Output the results
print("The smallest number entered is:",smallest)
print("The largest number entered is:",largest)

# Binary Search for index
li=[1,2,3,4,5,6]
target=4
left=0
right=len(li)-1
while left<=right:
    mid=(left+right)//2
    if li[mid]==target:
       print("The target number is present in index :",mid)
       break
    elif li[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print("Target number not found")
