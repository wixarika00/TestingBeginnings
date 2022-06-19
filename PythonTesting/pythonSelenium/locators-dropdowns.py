from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\xcnh76\Desktop\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_css_selector("input[name='name']").send_keys("Rahul") # tagname[attribute='value'] for css
driver.find_element_by_name("email").send_keys("Shetty")
driver.find_element_by_xpath("//input[@type='submit']").click()  # xpath
driver.find_element_by_id("exampleCheck1").click()
# select class provide the methods to handle the options
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

print(driver.find_element_by_class_name('alert-success').text)
print(driver.find_element_by_css_selector("div[class*='alert-success']").text) # takes part of expression
print(driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text)  # takes part but xpath

driver.find_element_by_xpath("//input[@type='submit']").click()

message = driver.find_element_by_class_name("alert-success").text

assert "success" in message # assert expects True


