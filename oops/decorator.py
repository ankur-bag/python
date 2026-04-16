# Definition :

# A decorator is a function that adds extra functionality to another function without changing its original code.

# Simple Analogy

# Think of a decorator like a wrapper on a gift 

# Gift = original function
# Wrapper = decorator
# You don’t change the gift, you just add something outside


# class Animal:
    
#     @property
#     def show(self):
#         print("hello how are you")

# obj = Animal()
# obj.show

# def decorate(func):
#     def wrapper():
#         print("I will print myself before the function")
#         func()
#         print("I will print after the function")
    
#     return wrapper

# @decorate
# def hello():
#     print("hello I am ankur bag")

# hello()

# def decorate(func):
#     def wrapper(a,b):
#         print("Than you for choosing our calculator")
#         func(a,b)
#         print("Thank you for your time")
#     return wrapper

# @decorate
# def add(a,b):
#     print(f"total : {a+b}")
    
# add(5,6)


#agrs & kargs : arguments in tupple format


def add(*args):
    print(args)

add(12,15,81,32)
