import sys
from pyfiglet import Figlet
import random



def isProperArg(arg):
    if len(arg) == 1:
        return True
    elif len(arg) == 3:
        if (arg[1] == "-f" or arg[1] == "--font"):
            if not (arg[2] in Figlet().getFonts()):
                print("Invalid arguments")
                sys.exit()
            return False
        else:
            print("Invalid arguments")
            sys.exit()
    else:
        print("Invalid arguments")
        sys.exit()




def main():
    arg = sys.argv
    figlet = Figlet()

    randomFont = isProperArg(arg)

    if(randomFont == True):
        fontList = figlet.getFonts()
        f = random.sample(fontList,1)
        f = f[0]
    elif(randomFont == False):
        f = arg[2]

    figlet.setFont(font=f)

    str = input("Input: ")
    print(figlet.renderText(str))


if __name__ == '__main__':
    main()