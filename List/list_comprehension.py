
# list comprehension used to convert one list into another list or creates new list from iterables.

# y = [i for i in range(10)]
# print(y)
#
# cubes = [i**3 for i in range(1,4)]
# print(cubes)

# list_1 = [2,3,4]
# new_list = [i*2 for i in range(4)]
# print(new_list)
#
# list_words = ["hi","this","is","Ram"]
# new_list = [word[0] for word in list_words]
# print(new_list)
#
# letters = [let for let in "python"]
# print(letters)

# map() with lamda
# letters = list(map(lambda x: x ,'python'))
# print(letters)

list1 = [2,3,4,5,6,7,8]
# list1 = list(map(int,list1))
# new_list = list(filter(lambda x: x%2, list1))
# print(new_list)
new_list = [x for x in list1 if x%2==0]
print(new_list)
new_list = [x for x in list1 if x%2!=0]
print(new_list)
new_list = [x for x in list1 if x%2 if x%5]
print(new_list)

list1 =  [2,3,4,5,6,7,8]
new_list = sum([x for x in list1])
print(new_list)

even_odd = [f'{x} is even' if x%2==0 else f'{x} is odd' for x in range(10)]
print(even_odd)





