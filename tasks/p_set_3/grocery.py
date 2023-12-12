def get_groceries():
    item_list = []
    while True:
        try:
            item = input().strip().lower()
            item_list.append(item)
        except EOFError:
            print("\n")
            break
    sorted_item_set = sorted(set(item_list))
    counts = []
    for i, item in enumerate(sorted_item_set):
        count = 0
        for k in item_list:
            if k == item:
                count += 1
        counts.append(count)
    for item, count in zip(sorted_item_set, counts):
        print(f"{count} {item.upper()}")


def main():
    get_groceries()
    ...



if __name__ == '__main__':
    main()