from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    # find_elements_by_css_selector(".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
    checkout = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getCheckoutItems(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
