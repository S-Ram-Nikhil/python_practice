# number pattern
n=int(input("Enter Number"))
space=2*n-2
for row in range(n):
    for col in range(0,space):
        print(end=" ")
    space=space-2
    num=1
    for col in range(row+1):
        print(num,end=" ")
        num=num+1
    print()