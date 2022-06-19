from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(executable_path="C:\\Users\\xcnh76\Desktop\chromedriver_win32\chromedriver.exe")
driver.get("https://qaclickacademy.github.io/protocommerce/")

driver.maximize_window()
driver.find_element_by_css_selector("a[href*='shop']").click()
cards = driver.find_elements_by_css_selector(".card-title a")
i = -1
for card in cards:
    i = i + 1
    cardText = card.text
    print(cardText)
    if cardText == "Blackberry":
        driver.find_elements_by_css_selector(".card-footer button")[i].click()
driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
# time.sleep(5)
element = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()
textMatch = driver.find_element_by_css_selector("[class*='alert-success']").text
assert ("Success! Thank you!" in textMatch)