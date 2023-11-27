def main():
    expression = input("Expression: ")
    x, y, z = expression.strip().split(" ")

    x = int(x)
    z = int(z)

    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '/':
        try:
            z != 0
        except ZeroDivisionError:
            raise
        result = x / z
    elif y == '*':
        result = x * z

    print('{:.1f}'.format(result))


if __name__ == "__main__":
    main()
