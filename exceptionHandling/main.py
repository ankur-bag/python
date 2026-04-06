# Excpetion Handling

'''
-Exception is an error that occurs during the execution of a program.
-Exception Handling is a mechanism to handle these errors and prevent the program from crashing.
-Syntax: try, except, else, finally

-Syntax error
-Indentation error
'''

a = int(input("tell your number: "))
try:
    print(10/a)

# except ZeroDivisionError:
#     print("you can not divide by zero")
except Exception as err:
    print("Sry , there is an err as" , {err})

print("ok i have done the division")