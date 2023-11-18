from calculator_pytest import cubed
import pytest


# def test_cubed():
#     assert cubed(2) == 8
#     assert cubed(3) == 27
#     assert cubed(-2) == -8
#     assert cubed(-3) == -27
#     assert cubed(0) == 0

# to check this with pytest we use the COMMAND LINE
# cmd: "pytest .\test_calculator_pytest.py"

# however using one function to test everything is not ideal
# because only the first error is being shon

# instead we could break up the big function above into smaller functions so all functions
# are attempted even if only one fails

def test_positive():
    assert cubed(2) == 8
    assert cubed(3) == 27


def test_negative():
    assert cubed(-2) == -8
    assert cubed(-3) == -27


def test_zero():
    assert cubed(0) == 0


# to check this with pytest we use the COMMAND LINE
# cmd: "pytest .\test_calculator_pytest.py"
# NOW ALL 3 TESTS ARE SHOWN

def test_str():
    with pytest.raises(TypeError):
        cubed("cat")
