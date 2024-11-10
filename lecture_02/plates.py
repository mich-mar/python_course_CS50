# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

def twoFirstLetters(string):
    for i in range(2):
        char = string[i]
        if not char.isalpha():
            return False
    return True

def goodLength(string):
    if(2 < len(string) < 6):
        return True
    else:
        return False

def allGoodChars(string):
    for char in string:
        if not char.isalpha() and not char.isdigit():
            return False
    return True

def numbersInGoodPlace(string):
    wasDigit = False

    for char in string:
        if char.isdigit() and wasDigit == False:
            if char == "0":
                return False
        if char.isdigit():
            wasDigit = True
        if char.isalpha() and wasDigit == True:
            return False

    return True


def is_valid(s):
    if not goodLength(s):
        return False
    if not numbersInGoodPlace(s):
        return False
    if not allGoodChars(s):
        return False
    if not numbersInGoodPlace(s):
        return False
    return True


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


main()
