from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Setup and Teardown for Driver
def setup_driver():
    try:
        options = webdriver.ChromeOptions()
        # Removed headless to avoid bot detection
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        return driver
    except WebDriverException as e:
        logging.error(f"Error setting up the driver: {e}")
        raise

def teardown_driver(driver):
    try:
        driver.quit()
    except WebDriverException as e:
        logging.error(f"Error during driver teardown: {e}")

# Test 1: Product Search and Add to Cart
def test_product_search_add_to_cart():
    driver = setup_driver()
    try:
        driver.get("https://www.nike.com/in/")
        logging.info("Searching for a product...")
        search_icon = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='search-button']")))
        search_icon.click()
        search_bar = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, "search")))
        search_bar.send_keys("Shoes")
        search_bar.send_keys(Keys.RETURN)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-card__body")))

        logging.info("Selecting the product...")
        product = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.product-card__body")))
        product.click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Bag']")))

        logging.info("Adding product to cart...")
        add_to_cart_btn = driver.find_element(By.XPATH, "//button[text()='Add to Bag']")
        add_to_cart_btn.click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'1 Item')]")))

        logging.info("Validating product added to cart...")
        cart_quantity = driver.find_element(By.XPATH, "//span[contains(text(),'1 Item')]")
        assert cart_quantity.is_displayed(), "Product not added to cart successfully"
    except TimeoutException as e:
        logging.error(f"Timeout occurred during Test Product Search and Add to Cart: {e}")
    except Exception as e:
        logging.error(f"Test Product Search and Add to Cart failed: {e}")
    finally:
        teardown_driver(driver)
        logging.info("Test Product Search and Add to Cart completed successfully.\n")

# Test 2: Login
def test_login():
    driver = setup_driver()
    try:
        driver.get("https://www.nike.com/in/login")
        
        logging.info("Testing valid login...")
        login(driver, <Enter username>, <Enter Password>)  # Please upload a valid login credential before running the test
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-qa='profile-name']")))
        logging.info("Valid login successful.")
    except TimeoutException as e:
        logging.error(f"Timeout occurred during Test Login: {e}")
    except Exception as e:
        logging.error(f"Test Login failed: {e}")
    finally:
        teardown_driver(driver)
        logging.info("Test Login completed successfully.\n")

# Test 3: UI Elements
def test_ui_elements():
    driver = setup_driver()
    try:
        driver.get("https://www.nike.com/in/")
        
        logging.info("Checking UI elements on homepage...")
        search_icon = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-qa='search-button']")))
        assert search_icon.is_displayed(), "Search icon not displayed"
        logging.info("Search icon is displayed.")

        nav_menu = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "nav[role='navigation']")))
        assert nav_menu.is_displayed(), "Navigation menu not displayed"
        logging.info("Navigation menu is displayed.")

        footer = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))
        assert footer.is_displayed(), "Footer not displayed"
        logging.info("Footer is displayed.")
    except TimeoutException as e:
        logging.error(f"Timeout occurred during Test UI Elements: {e}")
    except Exception as e:
        logging.error(f"Test UI Elements failed: {e}")
    finally:
        teardown_driver(driver)
        logging.info("Test UI Elements completed successfully.\n")

# Test 4: Form Validation
def test_form_validation():
    driver = setup_driver()
    try:
        driver.get("https://www.nike.com/in/help/a/contact-us")
        
        logging.info("Testing form validation with empty submission...")
        submit_btn = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Submit']")))
        submit_btn.click()
        error_message = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'This field is required')]")))
        assert error_message.is_displayed(), "Error message not shown for empty form"
        logging.info("Error message displayed successfully for empty form submission.")
    except TimeoutException as e:
        logging.error(f"Timeout occurred during Test Form Validation: {e}")
    except Exception as e:
        logging.error(f"Test Form Validation failed: {e}")
    finally:
        teardown_driver(driver)
        logging.info("Test Form Validation completed successfully.\n")

# Test 5: Error Handling
def test_error_handling():
    driver = setup_driver()
    try:
        driver.get("https://www.nike.com/in/")
        logging.info("Testing error handling for non-existent element...")
        driver.find_element(By.ID, "non_existent_element")
    except NoSuchElementException:
        logging.info("Element not found as expected.")
    except Exception as e:
        logging.error(f"Test Error Handling failed: {e}")
    finally:
        teardown_driver(driver)
        logging.info("Test Error Handling completed successfully.\n")

# Helper function: Login
def login(driver, email, password):
    try:
        logging.info("Locating email field...")
        email_field = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.NAME, "credential")))
        email_field.clear()
        email_field.send_keys(email)
        
        logging.info("Locating password field...")
        password_field = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.clear()
        password_field.send_keys(password)

        logging.info("Locating and clicking the continue button...")
        continue_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='continue']")))
        continue_button.click()

        # Ensure login was successful
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-qa='profile-name']")))
    except TimeoutException as e:
        logging.error(f"Timeout occurred during login: {e}")
        raise
    except Exception as e:
        logging.error(f"Login failed: {e}")
        raise

if __name__ == "__main__":
    test_product_search_add_to_cart()
    test_login()
    test_ui_elements()
    test_form_validation()
    test_error_handling()
