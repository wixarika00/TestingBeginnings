from selenium import webdriver

# brower exposes an executable file
# Through Selenium test we need to invoke th eexecutable file which will then invoke acual browser
driver = webdriver.Chrome(executable_path="C:\\Users\\xcnh76\Desktop\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/") # get method to hit url on borwser

print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/practice-project")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()  # only current window get closed
