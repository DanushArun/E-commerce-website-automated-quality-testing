# E-commerce-website-automated-quality-testing

Description
This repository contains automation scripts for testing various functionalities of an e-commerce website, specifically for Nike's India site. The scripts are built using Python and Selenium, and aim to validate essential e-commerce features such as product search, adding items to the cart, login functionality, UI elements, form validation, and error handling.

Features Tested
Product Search and Add to Cart: Validates the ability to search for products and add them to the shopping cart.
Valid Login Functionality: Tests login using valid credentials.
Homepage UI Elements: Checks the presence and visibility of key UI elements.
Form Validation: Validates that required fields trigger appropriate error messages.
Error Handling for Non-existent Elements: Ensures proper handling and reporting when an element is not found.

Prerequisites:
Python 3.x
Chrome browser
ChromeDriver (handled automatically using webdriver-manager)

Dependencies:

Install the required dependencies by running:
!pip install selenium webdriver-manager

Installation
Clone this repository:
git clone https://github.com/DanushArun/E-commerce-website-automated-quality-testing.git

Navigate to the project directory:
cd E-commerce-website-automated-quality-testing

Install dependencies:
pip install -r requirements.txt

Setting up Login Credentials
Note: The test for valid login requires valid credentials to work. Create a file named credentials.json in the root directory of the repository with the following structure:

json
Copy code
{
  "email": "your-email@example.com",
  "password": "your-password"
}
Make sure to enter a valid username and password for the Nike website in this file before running the tests.

Running the Tests
To execute the automation tests, run the following command:
python ecommerce_automation.py

Test Report

After running the tests, a detailed log file (test_execution.log) will be generated in the root directory with a summary of the executed tests, including successes and any failures.

Contributing
Feel free to submit a pull request if you'd like to improve the scripts or add new features.

License
This project is licensed under the MIT License - see the LICENSE file for details.

