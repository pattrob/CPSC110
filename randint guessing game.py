from random import randint, seed

MyInt = randint(0, 10)


G = int(input("Please enter an int: "))

i = 0

while i < 5:
    if G == MyInt:
        print("You found it!")
        break
    elif G < MyInt:
        print("Too small, guess again")
    else:
        print("Too big, guess again")
    G = int(input("Please enter an int: "))
    i = i + 1
    if i == 5:
        print("Game over!")
        

    
        
