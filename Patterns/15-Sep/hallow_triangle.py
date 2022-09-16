# hallow triangle
n=int(input("Enter Number"))
for row in range(n):
    for col in range(0,n):
        if (row==0 or col==(n-1)) or (row==col):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
