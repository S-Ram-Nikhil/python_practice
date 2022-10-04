# def map_case(num):
#     lst1 = list(map(str, num))
#     print(lst1)
#     str_num= int(''.join(lst1))
#     return str_num
#
# num1 = [4,5,6]
# num2=[1,2,3]
# # 654 + 321 =    975  output : [5,7,9]
# str_1=map_case(num1)
# str_2=map_case(num2)
# # add two numbers :
# add = str( str_1 + str_2)
# final_list=list(add)
# print(final_list)
# final_list=list(map(int,final_list))
# print(final_list)

# num1.reverse()
# print(num1)
# lst1 = list(map(str, num1))
# str1 = int(''.join(lst1))
# print(str1)

# num2.reverse()
# lst2 = list(map(str, num2))
# str2 = int(''.join(lst2))
# print(str2)

#
# def f():
#     # local variable
#     s = "I love Geeksforgeeks"
#     print("Inside Function:", s)
#
#
# # Driver code
# f()
# print(s)

def f():
    s += 'GFG'
    print("Inside Function", s)


# Global scope
s = "I love Geeksforgeeks"
f()