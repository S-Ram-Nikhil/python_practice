
# implementation of class method and static method
# create a class Students
class Students:
    # class variables are defined inside the class outside the methods.
    # All the objects of that class can use that variables.
    # class variables
    # we can call this variable using class and also using objects
    # class variables are shared by all objects.
    total_stud = 960
    total_teach = 50
    uniform_code = "yellow"

    # constructor
    # initializing here
    # instance variables are owned by instance of  class
    # For each object, instance variable are different
    def __init__(self, name, standard):
        # instance variable
        self.name = name
        self.standard = standard

    # instance method (first parameter as self)
    # They can acess unique data of their instance
    def show(self):
        # access instance variables
        print("student:", self.name, self.standard)
        # access class variables
        # print("dress code:", self.uniform_code)

    #  a class method
    @classmethod
    # cls method don't need self as argument and need cls which shows as class.
    # Class method and static method are bound to the class.
    # so we should access them using the class name.
    # cls as the first parameter in the class method.
    def code_change(cls, code):
        # access class variable
        print("previous code:", cls.uniform_code)
        cls.uniform_code = code
        print("uniform code changed to", Students.uniform_code)

    # static method to check if a student got the highest marks or not.
    # static method doesn't take instance or class as a parameter
    # because they don't have access to instance variables and class variables.
    # no need of parameter. it works as regular function but belongs to class.
    @staticmethod
    def highest(math_marks):
        if math_marks > 90:
            print("The student got highest math marks")
        else:
            print("The student got less than 90 marks")


# create object
# for each object(s1,s2),instance variable are different (name,standard)
s1 = Students('Ram', 9)
print(s1.name)
# calling instance method
s1.show()
print(s1.uniform_code)
s2 = Students('Nikhil',10)
print(s2.name)
# calling instance method
s2.show()
print(s2.uniform_code)


# calling the class method using the cls
Students.code_change('red')
s1.code_change('Blue')

# call static method using the class
Students.highest(76)
