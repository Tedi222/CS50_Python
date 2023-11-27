def main():
    time = convert(input("What time is it? "))
    # print(time)

    # breakfast - 7:00 - 8:00
    if 7 <= time <= 8:
        print("breakfast time")
    # lunch - 12:00 - 13:00
    elif 12 <= time <= 13:
        print("lunch time")
    # dinner - 18:00 - 19:00
    elif 18 <= time <= 19:
        print("dinner time")
    # nothing - 19:00 - 7:00
    else:
        pass


def convert(time):
    if time.find("a") != -1:
        time, _ = time.split("a")
        hh, mm = time.strip().split(":")
        if hh == "12":
            hh = 0

    elif time.find("p") != -1:
        time, _ = time.split("p")
        hh, mm = time.strip().split(":")

    else:
        hh, mm = time.strip().split(":")

    hh = int(hh)
    mm = int(mm)
    return hh + (mm / 60)


if __name__ == "__main__":
    main()
