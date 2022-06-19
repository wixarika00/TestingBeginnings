from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#iframe, frameset,
driver = webdriver.Chrome(executable_path="C:\\Users\\xcnh76\Desktop\chromedriver_win32\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
# frameid, frame name, index valu

# preferred_name_field.send_keys(Keys.SHIFT, Keys.ARROW_UP)
# preferred_name_field.send_keys(Keys.DELETE)
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()  # not clearing
driver.find_element_by_css_selector("#tinymce").send_keys("WRITTEN SUCCESSFULLY") # not printing
driver.switch_to.default_content()

print(driver.find_element_by_tag_name("h3").text)
