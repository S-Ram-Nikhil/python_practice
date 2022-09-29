#  Time complexity types

array = [1, 2, 3, 4, 5]

""" Constant time complexity """
print('######  Constant time complexity  #######')
# Accessing a specific element in an array  -O(1)
print(array[0])

""" Linear time complexity """
print('######  Linear time complexity  #######')
# A simple “for” loop from 0 to n ( with no internal loops) - O(N)
for element in array:
    print(element)


""" Logarithmic time complexity """
print('######  Logarithmic time complexity  #######')
# finding an element in a sorted array - (O(logN)
for index in range(0, len(array), 3):
    print(array[index])


""" Quadratic time complexity  """
print('######  Quadratic time complexity  #######')
# A nested loop of the same type takes quadratic time complexity
# looking an every index in the array twice.  O(N2) - N square
for x in array:
    for y in array:
        print(x, y)


""" Exponential time complexity """
print('######  Exponential time complexity  #######')
# Double recursion in fibonacci - O(2powerN)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
