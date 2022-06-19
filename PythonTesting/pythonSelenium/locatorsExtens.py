from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\xcnh76\Desktop\chromedriver_win32\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=eu")

# driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_css_selector("#username").send_keys("Rahul") # tagname[attribute='value'] for css
driver.find_element_by_css_selector(".password").send_keys("Rahul")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()  # only for <a>
driver.find_element_by_xpath("//input[@name='cancel']").click()
driver.find_element_by_xpath("//div[@id='usernamegroup']/label")  # parent way
driver.find_element_by_xpath("//div[@id='usernamegroup']/label")
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)  # grandparent way
# print(driver.find_element_by_css_selector("form[name='login']/label").text)