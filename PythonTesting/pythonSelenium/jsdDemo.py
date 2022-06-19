# JS DOM can access any element on web page just as selenium
# selenium have a method to execute javascript code in it
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\xcnh76\Desktop\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll down
time.sleep(3)
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))  # JS language

shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)





