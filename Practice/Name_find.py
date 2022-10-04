#https://zoom.us/j/6282753513?pwd=T0lNbEtBdE9iOXprb0lIdUhTM2FJZz09

name =['Ram', 'Vijay', 'Venkat']
user = input("Enter the username: ")
for n in name:
    if n == user:
        pass
    else:
        print(n)

name =['Ram', 'Vijay', 'Venkat']
user = input("Enter the username: ")
for n in name:
    if n in user:
        pass
    elif user not in name:
        print('Name not in list')
        break
    else:
        print(n)

# # names =['Ram', 'Vijay', 'Venkat']
# # user = input("Enter the username: ")
# # for i in names:
# #     if i == user:
# #         pass
# #     else:
# #         print(i)
# #         pass
# # if i!= user:
# #     print('name is not in list')
#
# name =['Ram', 'Vijay', 'Venkat']
# user = input("Enter the username: ")
#
# for n in range(0,len(name)):
#     if user in name[n]:
#         pass
#     elif user not in name:
#         print('Name not in list')
#         break
#     else:
#         print(name[n])
# lis1 = [10, 18, 15, "venkat", "vijay", "ram"]
# lis2 = []
# for i in range(1,len(lis1)+1):
#     lis2.append(lis1[-i])
# print(lis2)

