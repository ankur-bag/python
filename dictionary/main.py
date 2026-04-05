# Dictionary -> mutable


'''
-mutable -> can update the values, not the keys
-duplicates -> keys must be unique
-order -> it follows insertion order
-heterogenous -> it can store diff types of keys and values, like integers, strings,lists,or even another dictionary.

'''

# d= {1: "hello", 2:50}

# print(type(d))

# d = {10:100,20:200,30:300,40:400}
# d[10] = 1000 #updating
# d[50] = 500 #creating
# del d[30] #deleting 

# print(d)

# dictionary traversal
d = {10:100,20:200,30:300,40:400}
# d2 = d.copy() #creates a shallow copy of d in d2

# for i in d:
#     print(d[i])


# help(dict)

print(d.items())




