from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

@pytest.fixture(scope="module")
def driver():
    # Setup WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


# Feature 1: User Registration
def test_user_register_with_registered_username(driver):
    driver.get("http://127.0.0.1:5000/auth/register")
    driver.find_element(By.ID, "username").send_keys("prajwal")
    driver.find_element(By.ID, "email").send_keys("prajwalbanakar040999@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Prajwal@123")
    driver.find_element(By.ID, "password2").send_keys("Prajwal@123")
    driver.find_element(By.ID, "submit").click()

    # Find the error message on the page
    invalid_feedback = driver.find_element(By.CLASS_NAME, "invalid-feedback").text
    assert invalid_feedback == "Please use a different username."


def test_user_register_with_valid_details(driver):
    driver.get("http://127.0.0.1:5000/auth/register")
    driver.find_element(By.ID, "username").send_keys("test12345")
    driver.find_element(By.ID, "email").send_keys("test12345@gmail.com")
    driver.find_element(By.ID, "password").send_keys("test@12345")
    driver.find_element(By.ID, "password2").send_keys("test@12345")
    driver.find_element(By.ID, "submit").click()

    # Assert that the URL has changed to the login page
    assert driver.current_url == "http://127.0.0.1:5000/auth/login"

    # Assert that the success alert message is displayed
    alert_message = driver.find_element(By.CLASS_NAME, "alert-info").text
    assert "Congratulations, you are now a registered user!" in alert_message