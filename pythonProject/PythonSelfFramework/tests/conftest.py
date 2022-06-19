import pytest
from selenium import webdriver
import time
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\xcnh76\Desktop\chromedriver_win32\chromedriver.exe")
        driver.maximize_window()
    elif browser_name == "firefox":  # firefox invocation, Gecko Driver
        driver = webdriver.Firefox(executable_path="C:\\Users\\xcnh76\Desktop\geckodriver-v0.20.1-win64\geckodriver.exe")
    elif browser_name == "IE":  # IE driver
        print("IE driver")

    driver.get("https://qaclickacademy.github.io/protocommerce/")
    driver.maximize_window()
    request.cls.driver = driver  # driver will be sent to class object in file test_e2e
    # cls.driver is nothing but this driver in the class
    # whichever class with uses that setup fixture, will use driver if there is driver variable
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """"
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
