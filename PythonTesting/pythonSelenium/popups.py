import time
from selenium import webdriver
validateText = "Option3"

driver = webdriver.Chrome(executable_path="C:\\Users\\xcnh76\Desktop\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("input[id='name']").send_keys('Option3') #can be ('#name')
driver.find_element_by_id('alertbtn').click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
time.sleep(2)
alert.accept()
# alert.dismiss()  --> negative scenario




