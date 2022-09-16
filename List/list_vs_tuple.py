
# lists are mutable-changed/modified, allocate more memory, extend the size of the list.
# creating and accessing of list is slower whereas in tuple elements is faster.
# tuples are immutable-can't changed-these are fixed size,
# python allocates min memory block required for data.
#
# count_list = 0
# for each in dir(list):
#     count_list += 1
# print(count_list)
# print(dir(list))
# 47 available methods on lists
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__','__dir__', '__doc__',
# '__eq__','__format__','__ge__','__getattribute__', '__getitem__','__gt__', '__hash__', '__iadd__','__imul__',
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
# '__sizeof__','__str__',
# '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
# 'remove', 'reverse', 'sort']
# count_tuple = 0
# for each in dir(tuple):
#     count_tuple += 1
# print(count_tuple)
# print(dir(tuple))
# 34 available methods on tuples.
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count','index']

import sys
list_a = [1,2,3,4,5,6,7,8,9,10]
print(sys.getsizeof(list_a))
# 152 bytes for list object
list_a[2]=22
print(list_a)
# shows mutability
# [1, 2, 22, 4, 5, 6, 7, 8, 9, 10]
tuple_a = (1,2,3,4,5,6,7,8,9,10)
print(sys.getsizeof(tuple_a))
# 120 bytes for tuple object
# tuple_a[2]=22
# print(tuple_a)
# TypeError: 'tuple' object does not support item assignment. because of immutable.

# In dictionary, we can create keys using tuples. because of hashable and immutable nature.
value = {('ram','nikhil'):121} #Valid
print(value.keys())
# In dictionary, we can't use lists as keys. because of unhashable and mutable in nature.
value_1 = {['ram','nikhil']:123}  #Invalid
print(value_1.keys())
# TypeError: unhashable type: 'list'
