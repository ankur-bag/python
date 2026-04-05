#Tuple - immutable (unlike list) {otherwise everything same like List}

a = (1,5,7,8,9,5,5,5,5)
print(type(a))

print(a[2])

index = a.index(5) #index methods
print(index)

count = a.count(5) #count methods
print(count)

#tuple unpacking 
a,b,c,d = {1,2,3,4}
print(a)