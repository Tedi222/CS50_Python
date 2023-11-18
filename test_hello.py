from hello import hello_print, hello_return


def test_hello_print():
    hello_print("Tedi") == "hello, Some other name"
    hello_print("Tedi") == "hello, Tedi"
    # ^^^ doesn't do anything because
    # function "hello" does not return a value, only prints out to the stdout


def test_hello_return_default():
    assert hello_return() == "hello, world"


def test_hello_return_argument():
    assert hello_return("Tedi") == "hello, Tedi"

