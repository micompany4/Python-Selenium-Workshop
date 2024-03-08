from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Open page
driver.get("https://the-internet.herokuapp.com/login")

# type incorrect username into username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("samthomas")

# type password in password field
password_locator = driver.find_element(By.ID, "password")
password_locator.send_keys("SuperSecretPassword!")

# click submit button
submit_locator = driver.find_element(By.XPATH, "//i[@class='fa fa-2x fa-sign-in']")
submit_locator.click()

# verify that we're still on the login page
assert "https://the-internet.herokuapp.com/login" == driver.current_url

# verify page has invalid username msg
assert "Your username is invalid!" in driver.find_element(By.ID, "flash").text



driver.quit()
