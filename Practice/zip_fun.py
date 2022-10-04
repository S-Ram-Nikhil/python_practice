# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")
# x = zip(a,b)
# # zip(iterator1, iterator2, iterator3 ...)
# print(list(x))
# # [('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]
# print(tuple(x))

# slice(start, end, step)

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 5, 3)
print(a[x])