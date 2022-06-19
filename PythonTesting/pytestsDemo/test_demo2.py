# Any pytest files should start with test_
# pytest method names should start with test
# Any code should be wrapped in method only
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_third_program():
    msg = "Hello"
    assert msg == "Hello", "Test failed because strings do not match"


def test_forth_credit_card():
    a = 4
    b = 6
    assert a+2==6, "Test failed because strings do not match"


# run from command cd directory
# py.test -v -s
# running specific file: py.test test_demo2.py -v -s
# running with specific frase in method name: py.test -k CreditCard -v -s
# using mark (tag): py.test -m smoke -v -s
# you can skip tests with @pytest.mark.skip
# you want to run test but not report: @pytest.mark.xfail


