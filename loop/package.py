import random

num = random.randint(1,10)
tries =0

while True:
    guess = int(input("please guess your number between 1 to 10: "))
    if num == guess:
        tries +=1
        print(f"you are correct, you guessed the number in {tries} tries")
        break

    elif num<guess:
        tries +=1
        print("too high")
    
    elif num>guess:
        tries +=1
        print("too low")

        
