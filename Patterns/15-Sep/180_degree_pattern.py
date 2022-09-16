# 180 degree pyramid
n= int(input("Enter the number"))
num=(2*n)-2

for row in range(n):
    for col in range(0,num):
        print(end=" ")
    num=num-2
    for col in range(row+1):
        print("*",end=" ")
    print()