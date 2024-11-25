import sys
import inflect

def main():
    names = []
    while True:
        try:
            print("Name: ",end="")
            temp = input()
            names.append(temp)
        except EOFError:
            break

    print(f"Adieu, adieu, to {format_names(names)}")

def format_names(names):
    p = inflect.engine()

    if len(names) == 1:
        return names[0]
    else:
        return p.join(names)

if __name__ == "__main__":
    main()
