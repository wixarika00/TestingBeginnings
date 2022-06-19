# Implicit wait
# Explicit wait
# pause the test for some seconds
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


validateText = "Option3"
# wait until 5 seconds if object is not displayed
driver = webdriver.Chrome(executable_path="C:\\Users\\xcnh76\Desktop\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

list1 = []

list2 = []

for button in buttons:
    list1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)  # we want text from this element
    button.click()
print(list1)


driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

veggies = driver.find_elements_by_css_selector("p.product-name")
for veggie in veggies:
    veggie.text
    list2.append(veggie.text)
print(list2)

assert list1 == list2
originalAmount = driver.find_element_by_css_selector(".discountAmt").text

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
discountAmount = driver.find_element_by_css_selector(".discountAmt").text

assert float(discountAmount) < float(originalAmount)

print(driver.find_element_by_css_selector("span.promoInfo").text)

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in amounts:
    amount.text
    sum = sum + float(amount.text)

print(sum)
totalAmount = float(driver.find_element_by_class_name("totAmt").text)
assert sum == totalAmount