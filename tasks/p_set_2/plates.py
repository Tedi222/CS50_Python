def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    elif not s[0:2].isalpha():
        return False

    for i, character in enumerate(s):
        if character.isdecimal() or character.isalpha():
            pass
        else:
            return False

        if character.isdecimal():
            if int(character) == 0:
                return False
            elif not s[i:].isdecimal():
                return False
            else:
                return True

    return True




if __name__ == "__main__":
    main()
