# Any pytest files should start with test_
# pytest method names should start with test
# Any code should be wrapped in method only
import pytest


@pytest.mark.smoke
def test_first_program(setup):
    print('Hello')

@pytest.mark.xfail  # you want to run this test because you think that it is crucial for other operations, but it will not report
def test_second_credit_card():
    print("Good Morning")

def test_cross_browser(cross_browser):
    print(cross_browser[1])




