def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    strip_currency = d.strip("$")
    to_float = float(strip_currency)
    return to_float


def percent_to_float(p):
    strip_percent = p.strip("%")
    to_float = float(strip_percent)
    return to_float/100


if __name__ == "__main__":
    main()
