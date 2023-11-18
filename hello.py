def main():
    name = input("What's your name? ")
    hello_print(name)
    print(hello_return(name))


def hello_print(to="world"):
    print("hello,", to)


def hello_return(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()

