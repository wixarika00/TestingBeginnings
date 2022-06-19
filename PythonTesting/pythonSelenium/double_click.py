from selenium import webdriver
#iframe, frameset,
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\xcnh76\Desktop\chromedriver_win32\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action = ActionChains(driver)

# action.double_click(driver.find_element_by_xpath("//button[@ondblclick='myFunction()']")).perform()
action.context_click(driver.find_element_by_id("double-click")).perform()# right click
action.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert
assert alert.text == "You double clicked me!!!, You got to be kidding me"
alert.accept()
