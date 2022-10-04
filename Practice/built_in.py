# we get the character using chr()
x = chr(90)
# A-Z = 65 to 90
print(x)

y = chr(122)
# a- z = 97 to 122
print(y)

# ord() returns the unicode code of a character.
x = ord("A")
print(x)

# abs() - gives absolute number.
a = abs(-7.25)
print(a)
print(abs(3+5j))

# all()- check if all are true.
list_1 = [1,1,1]
print(all(list_1))

# any()- check if aby itemns in a list are true.
list_1 = [0,0,1]
print(any(list_1))

# bin() - returns the binary version of integer
x = bin(7)
print(x)

# bool() - return true, unless for [],{}.(), False, 0 , None
print(bool(False))

# callable()- checks the function callable or not
def x():
  a = 5


# zip()- paired together
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
j = zip(a, b)
print(tuple(j))

# eval() - it evaluates the specific expression.

g = 'print(55)'
eval(g)






