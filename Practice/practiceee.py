#
# purpose key in tuple
# coordinates = { (0,0) : 100, (1,1) : 200}
# coordinates[(1,0)] = 150
# coordinates[(0,1)] = 125
#
# print(coordinates)

# tuple operations :   sort
# numbers = [10, 33, 7, 80, 55, ]
# # numbers=tuple(sorted(numbers))
# numbers.sort()
# print(numbers)

# str1=['1','1','2']
# str2=['2','3','4']
# print(str1.__eq__(str2))
'''
operator overloading
+  __add__
-  __sub__
*  __mul__
/  __div__
== __eq__
+= __iadd__

'''

# string = ['ram','venkat','vijay']
# # new_string = string.replace('a', 'h', 1)
# # print(new_string)
#
# a=string.split()
# print(a)

# txt = "hello, my name is Peter, I am 26 years old"
#
# x = txt.split("n")
# #
# print(x)

# string= "book"
#
# dict={}
#
# for each in string:
#     dict[each]=dict.get(each,0)+1
# print(dict)

# lst1 = ["company", "emp_id", "emp_name", "role", "project"]
# lst2 = ["Msys", "3128", "srinivas", "developer"]
# dict_emp = {}  # empty dict for store values
# for i in range(len(lst1)):   # for loop retrieve values from list
#     dict_emp[lst1[i]] = lst2[i]  # to assignee the values to dict
# print(dict_emp)
# # dict_emp = dict(zip(lst1, lst2))
# # print(dict_emp)

# v = {5: 1, 4: 2, 3: 3, 2: 4, 1: 5}
#
# print("The original dictionary: ", v)
#
# # sorting by key
# a = dict(sorted(v.items(), key=lambda x: x[0]))
# print("After sorting by key: ", a)


# # how do converting two list into dict
# # using ZIP
# list_1 = ["company", "emp_id", "emp_name", "role", "project"]
# list_2 = ["Msys", "3128", "srinivas", "developer",]
#
# while len(list_1) > len(list_2):
#   list_2.append(None)
#
# # final_dict={}
# # for i in range(len(list_2)):
# #     final_dict[list_1[i]]=list_2[i]
#
# final_dict= dict(zip(list_1,list_2))
# print(final_dict)

# str_1 = "employee - ram , company - msys, ID - 25"
# # print("String_1 is ",string_1)
# #using strip() and split()
# res_dic= dict((a.strip(), (b.strip()))
# for a, b in (element.split('-')
#              for element in str_1.split(', ')))
#
# #printing converted dictionary
# print("The resultant dictionary is: ", res_dic)
# print(type(res_dic))


# dict1 = {1: 8, 2: 9, 3: 4}
# sorted_values = sorted(dict1.values())
# sorted_dict = {}
#
# for i in sorted_values:
#     for k in dict1.keys():
#         if dict1[k] == i:
#             sorted_dict[k] = dict1[k]
#             break
#
# print(sorted_dict)



# str = "empl=ram;comp=msys;id=25"
#
# d = dict(x.split("=") for x in str.split(";"))
# print(d)
#
# for k, v in d.items():
#     print(k, v)
#
#
# # A Python program to demonstrate working of OrderedDict
# from collections import OrderedDict
#
# print("This is a Dict:\n")
# d = {}
# d['a'] = 1
# d['c'] = 2
# d['b'] = 3
# d['d'] = 4
#
# for key, value in d.items():
#     print(key, value)
#
# print("\nThis is an Ordered Dict:\n")
# od = OrderedDict()
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# od['d'] = 4
#
# for key, value in od.items():
#     print(key, value)


# map(function, iterables)
# def function(a):
#     return a*a
# x = map(function, (1,2,3,4))  #x is the map object
# print(x)
# print(set(x))

# filter (function, iterables)
# def func(x):
#     if x>=3:
#         return x
# y = filter(func, (1,2,3,4))
# print(y)
# print(list(y))

