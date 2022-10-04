# def f_to_c(F):
#     C = (F - 32) * (5 / 9)
#     return round(C,4)
# temp_F= [100, 95, 98, 105, 110, 32]
#
# temp_C_map = list(map(f_to_c,temp_F))
# print((temp_C_map))

# names = ("John", "Adam", "STANLEY", "toNy", "Alisha")
# print(list(map(str.lower,names)))

# list_1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list = list(filter(lambda x: (x%2 !=0),list_1))
# print((final_list))
#
# ages = [13, 90, 17, 59, 21, 60, 5]
# adults = list(filter(lambda x: x>18,ages))
# print(adults)
#
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# print(list(map(lambda x: x*2, li)))
#
# animals = ['dog', 'cat', 'parrot', 'rabbit']
# print(list(map(lambda x:x.upper(),animals)))

def myfunc(n):
  return len(n)

x = list(map(myfunc, ('apple', 'banana', 'cherry')))
x = tuple(map(myfunc, ('apple', 'banana', 'cherry')))
print(x)



