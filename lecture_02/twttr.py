def twttr(str):
    tempStr = ""
    vovel = {"a", "e", "i", "o", "u", "y"}

    for char in str:
        if char.lower() in vovel:
            tempStr += ""
        else:
            tempStr += char

    return tempStr

def main():
    twitterStr = input("Input: ")
    print("Output:",twttr(twitterStr))

main()
