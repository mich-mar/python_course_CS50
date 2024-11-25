import random

def askLevel():
    while True:
        lvl = int(input("Enter a level: "))
        if lvl > 0:
            return lvl

def generateInt(lvl):
    return random.randint(1, lvl)


def main():
    lvl = askLevel()

    randInt = generateInt(lvl)

    while True:
        guess = input("Enter a number: ")

        if int(guess) == randInt:
            print("You guessed correctly!")
            break
        elif int(guess) < randInt:
            print("You guessed too low!")
        elif int(guess) > randInt:
            print("You guessed too high!")

if __name__ == "__main__":
    main()