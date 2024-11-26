from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_post_creation():
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    try:
        # Step 1: Navigate to the login page
        driver.get("http://127.0.0.1:5000/auth/login")

        # Step 2: Enter username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("test_user")  # Replace "test_user" with your test username

        # Step 3: Enter password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        ).send_keys("test_password")  # Replace "test_password" with your test password

        # Step 4: Click the submit button
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        ).click()

        # Step 5: Navigate to the post creation page
        driver.get("http://127.0.0.1:5000/new_post")  # Adjust route as necessary

        # Step 6: Enter a new post
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "post"))
        ).send_keys("This is a test post")

        # Step 7: Submit the post
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        ).click()

        # Step 8: Verify the post appears
        assert "This is a test post" in driver.page_source
        print("Post creation test passed!")

    finally:
        # Step 9: Quit the WebDriver
        driver.quit()
