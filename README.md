# E-commerce-website-automated-quality-testing

Description <br>
This repository contains automation scripts for testing various functionalities of an e-commerce website, specifically for Nike's India site. The scripts are built using Python and Selenium, and aim to validate essential e-commerce features such as product search, adding items to the cart, login functionality, UI elements, form validation, and error handling.

Features Tested <br>
Product Search and Add to Cart: Validates the ability to search for products and add them to the shopping cart.
Valid Login Functionality: Tests login using valid credentials.
Homepage UI Elements: Checks the presence and visibility of key UI elements.
Form Validation: Validates that required fields trigger appropriate error messages.
Error Handling for Non-existent Elements: Ensures proper handling and reporting when an element is not found.

Prerequisites: <br>
Python 3.x <br>
Chrome browser <br>
ChromeDriver (handled automatically using webdriver-manager) <br> <br>

Dependencies: <br>

Install the required dependencies by running: <br>
!pip install selenium webdriver-manager <br> <br>

Installation <br>
Clone this repository: <br>
git clone https://github.com/DanushArun/E-commerce-website-automated-quality-testing.git 
<br> <br>
Navigate to the project directory: <br>
cd E-commerce-website-automated-quality-testing
<br> <br>
Install dependencies: <br>
pip install -r requirements.txt
<br> <br>
Setting up Login Credentials <br>
Note: The test for valid login requires valid credentials to work. Create a file named credentials.json in the root directory of the repository with the following structure: 
<br> <br>
{ <br>
  "email": "your-email@example.com", <br>
  "password": "your-password" <br>
} <br> <br>
Make sure to enter a valid username and password for the Nike website in this file before running the tests. <br> <br>

Running the Tests <br>
To execute the automation tests, run the following command: <br>
python ecommerce_automation.py <br> <br>

Test Report <br>

After running the tests, a detailed log file (test_execution.log) will be generated in the root directory with a summary of the executed tests, including successes and any failures. <br> <br>

Contributing <br>
Feel free to submit a pull request if you'd like to improve the scripts or add new features.
