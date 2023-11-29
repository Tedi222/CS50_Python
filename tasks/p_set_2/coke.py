def buy_coke(price):
    due = price
    inserted = 0
    while due > 0:
        print("Amount Due:", due)
        inserted = int(input("Insert coin: "))
        due = due - inserted
        if due == 0:
            print("Amount Due:", due)
            break
        elif due < 0:
            print("Amount Owed:", abs(due))
            break
        else:
            continue


def main():
    buy_coke(price=50)


if __name__ == "__main__":
    main()