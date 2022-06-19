from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--stat-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="C:\\Users\\xcnh76\Desktop\chromedriver_win32\chromedriver.exe",options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)