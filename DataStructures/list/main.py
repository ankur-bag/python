# List powers
'''
- mutable:

s = [1,2,3,4,5]
s[0] = 10
print(s)

- duplicates :

s = [1,2,3,4,5,1,2,3,4,5]
print(s)

- ordered :

s = [1,2,3,4,5]
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

- heterogenous :

s = [1,2,3,4,5,"hello",True,3.14]
print(s)

'''


a = [12,13,14,15,16,17,18,19]


#1st way - using index
# for i in range (len(a)):
#     print(a[i])
    
# #2nd way - directly on values

# for i in a:
#     print(i)
    

# l = [1,2,3,4,5,6] #append function

# l.append(80)
# l.append(40)

# print(l)


l = [1,2,3,4,5,6]
l.insert(0,2)

print(l)

