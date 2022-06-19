from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\xcnh76\Desktop\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[1].click()
assert radiobuttons[1].is_selected()

