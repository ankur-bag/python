from pathlib import Path

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}, {items}")


def createfile():
    try:
        readfileandfolder()
        name = input("please enter the name of the file you want to create: ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("what you want to write in this file: ")
                fs.write(data)
            print("file created successfully")
        else:
            print("file already exists")
    except Exception as e:
        print("an err occured ",e)



def readfile():
    try:
        readfileandfolder()
        name = input("please enter the name of the file you want to read: ")
        p = Path(name)
        if p.exists():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)
        else:
            print("file not found")
    except Exception as e:
        print("an err occured ",e)


def appendfile():
    try:
        readfileandfolder()
        name = input("please enter the name of the file you want to append: ")
        p = Path(name)
        if p.exists():
            with open(p,"a") as fs:
                data = input("what you want to append in this file: ")
                fs.write(data)
            print("file appended successfully")
        else:
            print("file not found")
    except Exception as e:
        print("an err occured ",e)



def deletefile():
    try:
        readfileandfolder()
        name = input("please enter the name of the file you want to delete: ")
        p = Path(name)
        if p.exists():
            p.unlink()
            print("file deleted successfully")
        else:
            print("file not found")
    except Exception as e:
        print("an err occured ",e)


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for appending a file")
print("press 4 for deleting a file")

check = int(input("please tell your response: "))

if check ==1:
    createfile()
