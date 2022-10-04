
# # def outer_function():
# #     # b in the local namespace.
# #     b = 20
# #     def inner_func():
# #         # c is in the nested local namespace.
# #         c = 30
# # # a is the global namespace.
# # a = 10
#
#
# # def outer_function():
# #     a = 20
# #
# #     def inner_function():
# #         a = 30
# #         print('a =', a)
# #
# #     inner_function()
# #     print('a =', a)
# #
# #
# # a = 10
# # outer_function()
# # print('a =', a)
#
# def outer_function():
#     global a
#     a = 20
#
#     def inner_function():
#         global a
#         a = 30
#         print('a =', a)
#
#     inner_function()
#     print('a =', a)
#
#
# a = 10
# outer_function()
# print('a =', a)

#
# # built-in Namespace
# # Module: Global  Namespace
# # Fuction: Local Namespace
#
#
# # def outer_function():
# #     # b in the local namespace.
# #     b = 20
# #     def inner_func():
# #         # c is in the nested local namespace.
# #         c = 30
# # # a is the global namespace.
# # a = 10
#
#
# # def outer_function():
# #     a = 20
# #
# #     def inner_function():
# #         a = 30
# #         print('a =', a)
# #
# #     inner_function()
# #     print('a =', a)
# #
# #
# # a = 10
# # outer_function()
# # print('a =', a)
#
# def outer_function():
#     global a
#     a = 20
#
#     def inner_function():
#         global a
#         a = 30
#         print('a =', a)
#
#     inner_function()
#     print('a =', a)
#
#
# a = 10
# outer_function()
# print('a =', a)

# x = "global"
#
# def foo():
#     # global x
#
#     # x = x * 2
#     print(x)
#
#
# foo()
# # UnboundLocalError: local variable 'x' referenced before assignment
#
#
# def foo():
#     y = "local"
#
#
# foo()
# print(y)
# # NameError: name 'y' is not defined

x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()
# global global
# local




