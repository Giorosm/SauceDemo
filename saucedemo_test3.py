import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSauceDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        time.sleep(4)

    def test_shopping_process(self):
        # Login
        username = "standard_user"
        password = "secret_sauce"
        self.driver.find_element(By.ID,"user-name").send_keys(username)
        self.driver.find_element(By.ID,"password").send_keys(password)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(3)

        # Add first item to cart
        add_to_cart_button = self.driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
        add_to_cart_button.click()
        time.sleep(4)

        # Go to cart
        self.driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

        # Proceed to checkout
        self.driver.find_element(By.ID,"checkout").click()
        time.sleep(4)

        # fill the registration form and submit
        firstName_input = self.driver.find_element(By.ID,"first-name")
        firstName_input.send_keys("john")

        lastName_input = self.driver.find_element(By.ID,"last-name")
        lastName_input.send_keys("smith")

        zipCode_input = self.driver.find_element(By.ID,"postal-code")
        zipCode_input.send_keys("123456")

        continue_button = self.driver.find_element(By.ID,"continue")
        continue_button.click()
        time.sleep(4)

        # finish
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()
        time.sleep(4)# fill the registration form and submit
        firstName_input = self.driver.find_element(By.ID,"first-name")
        firstName_input.send_keys("john")

        lastName_input = self.driver.find_element(By.ID,"last-name")
        lastName_input.send_keys("smith")

        zipCode_input = self.driver.find_element(By.ID,"postal-code")
        zipCode_input.send_keys("123456")

        continue_button = self.driver.find_element(By.ID,"continue")
        continue_button.click()
        time.sleep(4)

        # finish
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()
        time.sleep(4)

        # Verify "Thank you" page
        #WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "title"), "THANK YOU FOR YOUR ORDER"))
        
        #def thankYou_page(self):
        thank_you_text = self.driver.find_element(By.XPATH,"//h2[text()='THANK YOU FOR YOUR ORDER']").text
        self.assertEqual(thank_you_text, "THANK YOU FOR YOUR ORDER", "Thank you page not displayed")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
