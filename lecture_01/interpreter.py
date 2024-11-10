def main():
    expresion = input("Expresion: ")

    pieces = expresion.split(" ")
    x = float(pieces[0])
    y = float(pieces[2])
    symbol = pieces[1]

    match symbol:
        case "+":
            value = x + y
        case "-":
            value = x - y
        case "/":
            if y != 0:
                value = x / y
            else:
                print("Illegal division by 0")
                exit()
        case "*":
            value = x * y

    print(round(value, 1))

main()