def order(menu):
    total = 0
    while True:
        try:
            item = input("Item:").title()
            if item in menu:
                total += menu[item]
                print("Total:", total)
        except KeyError:
            print("item not on the menu")
        except EOFError:
            print("End order\n")
            break
    return total




def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    total = order(menu)
    print("Total:",total)

if __name__ =="__main__":
    main()
