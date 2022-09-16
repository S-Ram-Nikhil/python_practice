# number pattern increase
n=int(input("Enter Number"))
num=1
for row in range(n):
    # num=1
    for col in range(row+1):
        print(num,end=" ")
        num=num+1
    print()