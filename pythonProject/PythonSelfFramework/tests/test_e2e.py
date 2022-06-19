from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckoutPage


class TestOne(BaseClass):

    def test_e2e(self): # if you define anything in class you should have 'self' parameter
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutPage.getCardTitle()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        confirmPage =  checkoutPage.getCheckoutItems()
        log.info("Entering country name as ind")
        self.driver.find_element_by_id("country").send_keys("ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        log.info("text received from application " + textMatch)
        assert ("Success! Thank you!" in textMatch)