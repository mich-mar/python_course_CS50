
def convertToSnake(text):
    tempString = ""

    for char in text:
        if char.islower():
            tempString = tempString + char
        elif char.isupper():
            tempString = tempString + "_" + char.title()

    return tempString

def main():
    string = input("camelCase: ")
    string = convertToSnake(string)
    print("snake_case:", string)

main()