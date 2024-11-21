from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


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

def test_user_login_and_greet(driver):
    driver.get("http://127.0.0.1:5000/auth/login")

    driver.find_element(By.ID, "username").send_keys("prajwal")
    driver.find_element(By.ID, "password").send_keys("Prajwal@123")
    driver.find_element(By.ID, "submit").click()

    assert driver.current_url == "http://127.0.0.1:5000/index"

    greeting_message = driver.find_element(By.XPATH, "//h1[contains(text(), 'Hi, prajwal')]")
    assert greeting_message.is_displayed()

def test_post_submission(driver):
    driver.get("http://127.0.0.1:5000/index")
    post_content = "This is a test post."
    driver.find_element(By.ID, "post").send_keys(post_content)

    driver.find_element(By.ID, "submit").click()

    alert = driver.find_element(By.CLASS_NAME, "alert-info").text
    assert "Your post is now live!" in alert

def test_explore_redirect(driver):
    driver.get("http://127.0.0.1:5000/index")

    explore_link = driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/explore']")

    explore_link.click()

    assert driver.current_url == "http://127.0.0.1:5000/explore"

def test_brand_redirect(driver):
    driver.get("http://127.0.0.1:5000/index")

    explore_link = driver.find_element(By.CSS_SELECTOR, "a.navbar-brand[href='/index']")

    explore_link.click()

    assert driver.current_url == "http://127.0.0.1:5000/index"


def test_home_redirect(driver):
    driver.get("http://127.0.0.1:5000/index")

    explore_link = driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/index']")

    explore_link.click()

    assert driver.current_url == "http://127.0.0.1:5000/index"

def test_profile_redirect(driver):
    driver.get("http://127.0.0.1:5000/index")

    explore_link = driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/user/prajwal']")

    explore_link.click()

    assert driver.current_url == "http://127.0.0.1:5000/user/prajwal"

def test_logout(driver):
    driver.get("http://127.0.0.1:5000/index")

    explore_link = driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/auth/logout']")

    explore_link.click()

    assert driver.current_url == "http://127.0.0.1:5000/auth/login?next=%2Findex"



