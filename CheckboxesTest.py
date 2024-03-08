import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCheckboxes:

    @pytest.mark.checkboxes
    def test_checkboxes(self):
        driver = webdriver.Chrome()

        # Open page
        driver.get("https://the-internet.herokuapp.com/checkboxes")

        checkbox1 = driver.find_element(By.XPATH, "//input[1]")
        checkbox2 = driver.find_element(By.XPATH, "//input[2]")

        # verify default settings for the checkboxes
        assert not checkbox1.is_selected()
        assert checkbox2.is_selected()

        # check the first checkbox and uncheck the second checkbox
        checkbox1.click()
        checkbox2.click()

        # verify that checkbox1 is checked and checkbox2 is unchecked
        assert checkbox1.is_selected()
        assert not checkbox2.is_selected()

        driver.quit()
