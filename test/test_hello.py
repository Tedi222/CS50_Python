from hello import hello_return


def test_hello_return_default():
    assert hello_return() == "hello, world"


def test_hello_return_argument():
    assert hello_return("Tedi") == "hello, Tedi"


# because we have the init file
# now we can run multiple test files by just simply passing
# the name of the folder "test" in the commandline
# cmd: "pytest test"
