import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\xcnh76\Desktop\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)  #needed because it would be to fast for selenium. list opens after some time
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a") # for css is a, for xpath is /a
print(len(countries))  # liczy ilosc countries
for country in countries:
    if country.text == "India":
        country.click()
        break
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"  #selenium will not recognize that India text