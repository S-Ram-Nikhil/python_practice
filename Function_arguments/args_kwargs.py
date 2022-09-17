

# function arguments- pass value to funtion
def multiply(x, y):
    return x*y


print(multiply(2, 3))
# 6


# *args (non-Keyword arguments)
# *args allow a function to take any number of positional arguments.
def myfun(*argv):
    for arg in argv:
        print(arg)


myfun('Hello', 'i', 'am', 'ram')

#  Ex-2
# *args
# with a first extra argument
def myfun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myfun('Hello', 'i', 'am', 'ram')

# ex -3
def func(a,*args):
    print("Value of a is:", a)
    for i in args:
        print(f' args are -> {i} ')

func('Hey', 'How', 'are', 'you?')

# Ex-4
def add(*args):
   result = 0
   for i in args:
      result += i
   return result

print(add(1,5))


# **kwargs - that allows us to pass a variable length of keyword arguments to the function.
# ex-1
def Person(**kwargs):
    for key, value in kwargs.items():
        print("{} -> {}".format(key, value))    # OR print(f'{key} -> {value}')

Person(Name = 'Ram', Sex = 'Male', Age = 27, City = 'AP', Mobile = 9878003)

# Ex-2
def employee(**kwargs):
    for i in kwargs:
        print(i)


employee(emp="ram", salary=9000, age=27)

# ex-2
# using both args and kwargs.
def func(a, b, *args, option = True, **kwargs):
    print(a, b)
    print(args)
    print(option)
    print(kwargs)

func(1, 3, 10, 20, Name = 'Ram', Salary = 60000)
