# Naming conventions :

# Function name should be lowercase
# Wrong
def Function():
    pass
def My_function():
    pass
# '(' is missing
def function:
    pass


# Expected 2 blank lines
# Correct
def function():
    pass


def my_function():
    pass

# Class name should use CamelCase convention
# Wrong
class model:
    name = "ram"
    pass


class mymodel:
    pass

# correct
class Model:
    age = 10
    pass


class MyClass:
    age = 20
    pass

# Method definition inside classes with a single line
class MyName:
    def first_name(self):
        return None

    def second_name(self):
        return None

# Recommended
name_variable = 10
age_variable = 11
final_variable = 12
# breaking before a operator
total = (name_variable
         + age_variable
         - final_variable)
# Not Recommended
# Breaking after a operator
final = (name_variable +
         age_variable -
         final_variable        )

# Indentation:
x = 2
# Wrong
if x>1:
# 4 consecutive spaces missing
print("highest")
# Correct
if x>4:
    print("highest")

# Wrong
# Booloeans - they don't need comparisons
if my_boolean == True:
    get_result()
if my_boolean is True:
    get_result()

# Correct
if some_variable:
    get_result()


"""
1.missing whitespace around operator.
2. unexpected spacs around keyword/operator equals. 
"""






