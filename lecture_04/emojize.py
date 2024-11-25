import emoji

def main():
    str = input("Input: ")
    print(emoji.emojize(f'Output: {str}'))

if __name__ == '__main__':
    while True:
        main()
