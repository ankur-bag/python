# LAMDA FUNCTIONS
# -A lamda func is an anonymous , inline function defined using the lamda keyword
# -Its often used for short , simple functions that are used only once or temporarily
# -You can have multiple args but there will be only one expression


# without using lambda func
# def add(a,b):
#     print(a+b)
# add(12,25)


# #using lambda func
# add = lambda a,b:a+b
# print (add(12,15))


# add = lambda a:"even" if a%2 ==0 else"odd"
# print (add(12))


# MAP AND FILTER
# - MAP is used for applying a fuction to multiple items
# - Applies the aame func to every item in that list 

a= [1,2,3,4,5]
# result = map (lambda x: x*2, a)
# print(list(result))


# a= [1,2,3,4,5]
# def double (a):
#     return a*2
# result = map(double,a)

# print(list(result))
    
# List
# def even(a):
    # if a%2 ==0:
    #     return True
    # else:
    #     return False

result = filter(lambda a: True if a%2 ==0 else False ,a)
print(list(result))

