import pytest


@pytest.fixture(scope='class')  # for pre-requisite, like setting up browser etc
def setup():
    print("I will be executing first")  # example - open browser
    yield  # stops, and comes bck after that
    print("I will be executed last")  # late close it and delete cookies

@pytest.fixture()
def data_load():
    print("user profile data is being created")
    return ["Rahul", "Shetty", "jshhdhsfh"]


@pytest.fixture(params=[("chrome", "Rahul"), "Firefox", "IE"])  # running with items one by one
def cross_browser(request):
    return request.param
