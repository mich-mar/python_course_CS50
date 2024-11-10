def addToList(item_dict, item, count=1):
    item = item.lower()

    if item in item_dict:
        item_dict[item] += count
    else:
        item_dict.update({item: count})

    return item_dict


def main():
    item_dict = {}

    while True:
        try:
            item = input()
            item_dict = addToList(item_dict, item)
        except KeyError:
            pass
        except EOFError:
            break

    sorted_items = sorted(item_dict.items())

    for item, count in sorted_items:
        print(count, item.upper())


if __name__ == '__main__':
    main()
