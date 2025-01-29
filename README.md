# Logout-a-Person-using-Automation
Selenium Logout Automation Script

This script automates the logout process on the “Automation Exercise” website using Selenium WebDriver. It performs the following actions:
	1.	Navigates to the website.
	2.	Logs in using predefined user credentials.
	3.	Verifies that the login is successful.
	4.	Logs out of the account.
	5.	Verifies that the logout was successful and the login page is displayed.

Prerequisites

Before running this script, ensure you have the following:
	•	Python installed on your machine.
	•	Selenium WebDriver installed. You can install it using pip:

pip install selenium


	•	ChromeDriver installed for the Chrome browser. Ensure the version of ChromeDriver matches the version of your Chrome browser.
You can download ChromeDriver from here.

Script Overview
	1.	Opening Browser: The script opens the Chrome browser using Selenium WebDriver.
	2.	Navigating to Website: The script navigates to “https://www.automationexercise.com”.
	3.	Verifying Home Page: The script checks if the homepage loads successfully by verifying the page title.
	4.	Login: It clicks the “Signup / Login” button, enters the login credentials, and submits the login form.
	5.	Verifying Login: The script verifies if the user is successfully logged in by checking the login status on the page.
	6.	Logout: The script clicks the “Logout” button.
	7.	Verifying Logout: It checks if the login page is displayed after the logout action.

How to Run the Script
	1.	Clone or download this repository.
	2.	Open a terminal or command prompt.
	3.	Navigate to the directory containing the script.
	4.	Run the script using Python:

python logout_automation.py



Code Explanation
	•	webdriver.Chrome(): Starts the Chrome browser.
	•	driver.get(): Navigates to the specified URL.
	•	assert: Verifies that the page title or element is correct. If the assertion fails, an error message is printed.
	•	driver.find_element(): Locates an element on the page using its locator (e.g., XPath, link text).
	•	send_keys(): Enters text into an input field.
	•	click(): Simulates a mouse click on the element.
	•	time.sleep(): Pauses the execution for a specified amount of time to ensure elements have loaded before interacting with them.

Error Handling
	•	AssertionError: If the assertion fails (e.g., page not loaded, incorrect element visible), an error message is displayed.
	•	General Exception: Any other errors that occur during the execution will be caught and displayed.

Conclusion

This script demonstrates how to use Selenium WebDriver to automate logging in and logging out from a website. It’s helpful for automating repetitive tasks such as user authentication testing or logging in/out scenarios for websites.
