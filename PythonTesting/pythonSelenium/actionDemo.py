from selenium import webdriver
import time
#iframe, frameset,
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\xcnh76\Desktop\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
menu = driver.find_element_by_id('mousehover')
action.move_to_element(menu).perform()
action.move_to_element(driver.find_element_by_link_text("Top")).click().perform()

action = ActionChains(driver)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(2)
# action.double_click(driver.find_element_by_xpath("//button[@ondblclick='myFunction()']")).perform()
action.double_click(driver.find_element_by_xpath("//body/button")).perform()