# File Handling

'''
open function 

-r => read
-w => write
-a => append
-x => create
-t => text
-b => binary
-r+ => read and write
-w+ => write and read
-a+ => append and read
'''
p = open (r'file.txt')
print (p.read())
p.close()

r = open("file.txt", "w")
r.write("I read in 2nd year , RCCIIT")
r.close()

r = open("file.txt", "a")
r.write(" Now im appending some stuff in the file")
r.close()

