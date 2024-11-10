def askFraction():

    while True:
        frac = input("Fraction: ")

        if "/" in frac:
            try:
                values = frac.split('/')
                x = int(values[0])
                y = int(values[1])
                output = x / y
            except ValueError:
                pass
            except ZeroDivisionError:
                pass
            else:
                break

    return output


def main():
    frac = askFraction()

    if frac > 0.99:
        print("F")
    elif frac < 0.01:
        print("E")
    else:
        frac = int(frac * 100)
        print(f"{frac}%")


if __name__ == '__main__':
    while True:
        main()

