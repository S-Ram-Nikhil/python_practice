
# Accessing the index.
from array import *
arr1 = array('i', [1, 2, 3, 4, 5])
arr2 = array('i', [6, 7, 8, 9, 10])


def access_element(array, index):
    if index >= len(array):
        print("There is no element in this index")
    else:
        print(arr1[index])


access_element(arr1, 8)

# Traverse-
for i in arr2:
    print(i)

# Finding an element index.


def find_element(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "element not found"


print(find_element(arr1, 5))

# deleting an element from array -
arr1.remove(5)
print(arr1)

# append-

arr1.append(5)
print(arr1)

# Insert -
arr2.insert(4, 6)
print(arr2)

# Extend -
my_array = array("i", [11, 12, 13])
# arr2.extend([11,12,13])
arr2.extend(my_array)
print(arr2)

# Add items from list into array using fromlist() method -
temp_list = [20, 21, 22]
my_array.fromlist(temp_list)
print(my_array)

# Remove -
my_array.remove(22)
print(my_array)

# remove- last element using pop() method-
my_array.pop()
print(my_array)

#  any element using index() -
my_array.index(20)
print(my_array)

# reverse a  python array - using reverse() method-

my_array.reverse()
print(my_array)

# get array buffer information - through buffer_info method
# gives the address of the memory and number of elements in array.
print(my_array.buffer_info())

# count()- method.
# check number of occurrences of a given element.
print(my_array.count(13))

# convert an array to list-
# print(my_array.tolist())

#  slice elements - from an array-

print(my_array[1:3])
