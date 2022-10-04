# # # Python program to demonstrate the use of NumPy arrays
# # import numpy as np
# #
# # list1 = [1, 2, 3, 4, 5, 6]
# # list2 = [10, 9, 8, 7, 6, 5]
# #
# # # Convert list1 into a NumPy array
# # a1 = np.array(list1)
# # # print(a1)
# #
# # # Convert list2 into a NumPy array
# # a2 = np.array(list2)
# #
# # print(a1*a2)
#
#
# # Python program to demonstrate
# # the use of index arrays.
# import numpy as np
#
# # Create a sequence of integers from 10 to 1 with a step of -2
# a = np.arange(10, 1, -2)
# print("\n A sequential array with a negative step: \n",a)
#
# # Indexes are specified inside the np.array method.
# newarr = a[np.array([3, 1, 2 ])]
# print("\n Elements at these indices are:\n",newarr)
#
# # import numpy as np
# #
# # # NumPy array with elements from 1 to 9
# # x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# #
# # # Index values can be negative.
# # arr = x[np.array([1, 3, -3])]
# # print("\n Elements are : \n",arr)
#
# # You may wish to select numbers greater than 50
# import numpy as np
#
# a = np.array([10, 40, 80, 50, 100])
# print(a[a>50])
#


# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
# # loop fell through without finding a factor
#     else:
#         print(n, 'is a prime number')

# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found an odd number", num)

# from datetime import date
# today= date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)

matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],]


for i in range(4):
    for row in matrix:
        print([row[i]],)

# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]