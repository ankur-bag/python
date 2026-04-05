# SETS

'''
-mutable
-evey element should be unique
-unorderd : no index access
-heterogenous:  can store -> string, numbers,tuples , but not everything

'''


# s = {1,2,3,4,5}

# a = "hello"
# b = hash(a) # hash func (everytime the hash value will be diff)
# print(b)


#Set traversal - can not traverse through index value

# a = {1,2,3,4,"hello",5,6,7,8,9}

# for i in a:
#     print(i)
    
# a= {2,1,3,4}

# # a.remove(2) #remove and discard functions are same
# # print(a)

# a.pop() # first element ~ low hash value  ,eg-> 1
# print(a)

a= {1,2,3,4,5}
b = {4,5,6,7,8}

# s = a.union(b)
# s = a|b #same as union function
# print(s)

#s = a.intersection(b)
s= a&b  #same as intersection function
#print(s)

# s = a-b #difference function
# print(s)

s = b^a #symetric difference
print (s)