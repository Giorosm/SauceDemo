import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the WebDriver and open the website
driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(4)

# Step 1: Login
username_input = driver.find_element(By.ID,"user-name")
username_input.send_keys("standard_user")

password_input = driver.find_element(By.ID,"password")
password_input.send_keys("secret_sauce")

login_button = driver.find_element(By.ID,"login-button")
login_button.click()
time.sleep(4)

# Step 2: Add first item to cart
add_to_cart_button = driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
add_to_cart_button.click()
time.sleep(4)

# Step 3: Go through cart/checkout
cart_icon = driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
cart_icon.click()

checkout_button = driver.find_element(By.ID,"checkout")
checkout_button.click()
time.sleep(3)

# fill the registration form and submit
firstName_input = driver.find_element(By.ID,"first-name")
firstName_input.send_keys("john")

lastName_input = driver.find_element(By.ID,"last-name")
lastName_input.send_keys("smith")

zipCode_input = driver.find_element(By.ID,"postal-code")
zipCode_input.send_keys("123456")

continue_button = driver.find_element(By.ID,"continue")
continue_button.click()
time.sleep(5)

# finish
finish_button = driver.find_element(By.ID, "finish")
finish_button.click()
time.sleep(4)

# step 4: Check if the "Thank you" message is present on the page
thank_you_message = driver.find_element(By.XPATH,"//h2[contains(text(), 'Thank you for your order')]")
assert thank_you_message.is_displayed(), "Thank you message not found on the page."
time.sleep(5)

# Close the browser
driver.quit()
