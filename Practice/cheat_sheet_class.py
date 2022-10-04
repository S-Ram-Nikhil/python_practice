# Define a class
# use class keyword
# class Person:
#     pass


# person is an instance of the Person class
# Create an object Person class
# person = Person()

# Adds the name attribute to the person object
# person.name = "Ram"

""" if another Person object created, the new object won't have the name attribute"""


# To define and initialize an attribute for all instances of a class use __init__method.
class Person:
    # class attributes are shared by all instances of a class
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter +=1

    """when we craete a Person object, python automatically calls the __init__ method to initialize the instance 
    attribute. """

    def greet(self):
        return f"Hi, it's {self.name}"

#     Like a class attribute, class method is shared by all instances of the class
    @classmethod
    def new_member(cls):
        return Person('anonymous', 22)
#     Static method is not bound to a class or any instances of the class.
# syntax- ClassName.static_method_name()
class TemparatureConverter:
    @staticmethod
    def c_to_f(c):
        return 9 * c/5 +32


# person = Person('ram', 27)
# print(person.name)
# print(person.greet())
# var = Person.counter
# print(var)
# # a = person.counter
# # print(a)
# p1 = Person("nikhil", 23)
# p2 = Person("rams", 26)
# print(Person.counter)

anonymous = Person.new_member()
print(anonymous.name)
f = TemparatureConverter.c_to_f(50)
print(f)


# Employee class that inherits from the Person class
# the employee class can access the attributes and methods of the parent class
class Employee(Person):
    def __init__(self, name, age, job_title):
        # super() allows a child class to access a method of the parent class
        super().__init__(name,age)
        self.job_title = job_title

    def greet(self):
        return super().greet() + f" I'm a {self.job_title}"

emp = Employee("Ram", 25, "software engineer")
print(emp.greet())

