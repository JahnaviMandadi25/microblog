from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_post_creation():
    driver = webdriver.Chrome()
    try:
        # Navigate to the login page
        driver.get("http://127.0.0.1:5000/auth/login")

        # Wait for the username field and enter the username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("test_user")

        # Wait for the password field and enter the password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        ).send_keys("test_password")

        # Wait for the submit button and click it
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        ).click()

        # Navigate to the post creation page
        driver.get("http://127.0.0.1:5000/new_post")

        # Wait for the post textarea and enter a post
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "post"))
        ).send_keys("This is a test post")

        # Wait for the submit button and click it
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        ).click()

        # Verify the post appears
        assert "This is a test post" in driver.page_source
        print("Post creation test passed!")
    finally:
        driver.quit()
