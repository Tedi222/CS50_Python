from calculator import square


def main():
    test_square()


def test_square():

    ## DON'T USE THE METHOD BELOW ##
    # if square(2) != 4:
    #     print("2 squared was not 4")
    # if square(3) != 9:
    #     print("3 squared was not 9")


    ## USE "assert" INSTEAD! <3 ## <<< this method works with pycharm
    # assert square(2) == 4
    # assert square(3) == 9

    ## BUT We can also combine it with "try" and "except ##
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")

    try:
        assert square(-1) == 4
    except AssertionError:
        print("-2 squared was not 4")

    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")


if __name__ == "__main__":
    main()
