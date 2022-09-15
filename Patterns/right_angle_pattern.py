# Program to run a rignt angle '*' pattern.

# end helps to give space to next print.
# print("hi");print("hello")
# print("hi", end=' ')
# # print()
# print("hello")
#
#
n = int(input("Enter the number of rows:- "))
# iterate through rows
for i in range(1,n+1):
    # iterate through columns
    for j in range(1,i+1):
        print("*", end=' ')
    print()

# n = 5
# for i in range(1, n+1):
#     print(i * "* ", end=" ")
#     print()

# n = 6
# i = 1
# while i <= n:
#     print(i * "* ")
#     i += 1




