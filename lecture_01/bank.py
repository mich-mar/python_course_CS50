
def main():
    greeting = input("Greeting: ")

    # splitting whole input into array of strings
    words = greeting.split()

    if words[0] == "Hello" or words[0] == "hello":
        print("0$")
    elif words[0][0] == "H" or words[0][0] == "h":
        print("20$")
    else:
        print("100$")

main()