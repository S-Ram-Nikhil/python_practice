
# Python program to find the factorial of a number
num = int(input("Enter a number: "))

factorial = 1

# checking the number is negative, positive or zero
if num < 0:
   print(" factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)