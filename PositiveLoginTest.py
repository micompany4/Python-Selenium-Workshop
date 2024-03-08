from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class PositiveLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testlogin(self):
        driver = self.driver

        # Open page
        driver.get("https://the-internet.herokuapp.com/login")

        # type username into username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("tomsmith")

        # type password in password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("SuperSecretPassword!")

        # click submit button
        submit_locator = driver.find_element(By.XPATH, "//i[@class='fa fa-2x fa-sign-in']")
        submit_locator.click()

        # verify new login page
        self.assertEqual("https://the-internet.herokuapp.com/secure", driver.current_url, "wrong url")

        # verify page has success msg
        self.assertIn("You logged into a secure area!", driver.find_element(By.ID, "flash").text,
                      "wrong banner message")

        # verify logout button is displayed
        self.assertTrue(driver.find_element(By.XPATH, "//i[@class='icon-2x icon-signout']").is_displayed(),
                        "logout button is not displayed")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
