# triangle pattern
n=int(input("Enter number"))
space=n-1
for row in range(n):
    for col in range(0,space):
        print(end=" ")
    space=space-1
    for col in range(row+1):
        print("*",end=" ")
    print()