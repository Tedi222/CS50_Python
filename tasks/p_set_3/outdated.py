# pad a string with 0 when lenght < 0
# print(f"{n:0=2}") pads with zero or anything before the "=" sign
# print(f"{n:02}") pads with zero
# print(f"{n}".zfill(2)) pads with zero


# output YYYY-MM-DD
# if x:
#     date = 'mm-dd-yyyy'  # 9/8/1636
# if x:
#     date = 'month dd, year'  # September 8, 1636

def convert_date(s, month_list):
    s = s.strip()
    if s.count("/") == 2:
        try:
            mm, dd, yyyy = [int(i.strip()) for i in s.split('/')]
        except ValueError:
            pass
    elif s.count(' ') == 2:
        try:
            mm, dd, yyyy = [i.strip() for i in s.split(' ')]
            mm = month_list.index(mm.title()) + 1
            dd = int(dd.strip(','))
            yyyy = int(yyyy)
        except ValueError:
            pass
    else:
        raise ValueError

    return dd, mm, yyyy



def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            date = input("Date: ")
            dd, mm, yyyy = convert_date(date, months)
            if 1 > mm or mm > 12 or 1 > dd or dd > 31:
                raise ValueError
            print(f"{yyyy:0=2}-{mm:0=2}-{dd:0=2}")
        except ValueError:
            pass
        else:
            break



if __name__ == "__main__":
    main()


