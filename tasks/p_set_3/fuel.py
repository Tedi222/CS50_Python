def calc_fuel():
    while True:
        try:
            frac = input("Fraction: ")
            x, y = frac.split("/")
            x = int(x)
            y = int(y)
            result = x/y
        except ValueError:
            print("numerator and denominator must be an integer")
        except ZeroDivisionError:
            print("division by 0")
        else:
            break
    return round(result*100)


def main():
    remaining_fuel = calc_fuel()
    if remaining_fuel <= 1:
        print("E")
    elif remaining_fuel >= 99:
        print("F")
    else:
        print(f'{remaining_fuel}%')


if __name__ == "__main__":
    main()