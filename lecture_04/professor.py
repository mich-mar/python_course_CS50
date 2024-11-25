import random

from scipy.constants import point


def get_level():
    while True:
        lvl = int(input("Enter a level: "))
        if lvl == 1 or 2 or 3:
            return lvl


def generate_integer(level):
    return random.randint(1, pow(10,level))


def main():
    lvl = get_level()
    points = 0

    for i in range(10):
        error = 0

        num1 = generate_integer(lvl)
        num2 = generate_integer(lvl)
        sum = num1 + num2

        while error < 3:
            temp_str = str(num1) + " + " + str(num2) + " = "

            usr_input = input(temp_str)

            if int(usr_input) != sum:
                print("EEE")
                error += 1
            else:
                points += 1
                break

    print("Score: " + str(points))


if __name__ == "__main__":
    main()