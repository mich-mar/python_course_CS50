menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    sum = 0

    while True:
        try:
            item = input("Item: ")
            item = item.lower().title()
            sum += menu[item]
            print("Total: ",sum,"$",sep="")
        except KeyError:
            pass
        except EOFError:
            break


if __name__ == '__main__':
    main()
