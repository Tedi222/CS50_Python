def main():
    variable = input("camel case: ")
    snake_case = camel_to_snake(variable)
    print(snake_case)
    ...

def camel_to_snake(camel):
    new = ""
    for i, letter in enumerate(camel):
        if letter.isupper():
            new = new + "_" + letter
        else:
            new = new + letter
    return new.lower()

if __name__ == "__main__":
    main()