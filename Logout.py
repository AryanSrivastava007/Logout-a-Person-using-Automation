from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys


#starting the browser driver
driver = webdriver.Chrome()

#navigate to URL
try:
    driver.get('https://www.automationexercise.com')
    driver.maximize_window()
    time.sleep(1)

#checking if the home screen is available or not
    assert "Automation Exercise" in driver.title
    print("Home page is visible successfully.")

#clicking on Login button
    driver.find_element(By.LINK_TEXT,"Signup / Login").click()
    time.sleep(1)

#checking if login page is visible or not
    assert driver.find_element(By.XPATH,"//h2[text()='Login to your account']").is_displayed()
    print("Login page is visible")

#enter the details of the user
    driver.find_element(By.XPATH,"//input[@type='email']").send_keys("aryansrivastava04643@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@type='password']").send_keys("password123")
    time.sleep(1)

#click on login button
    driver.find_element(By.XPATH,"//button[text()='Login']").click()
    time.sleep(1)

#check weather login as user is shown or not
    assert driver.find_element(By.XPATH,"//a[text()=' Logged in as ']").is_displayed()
    print("It is sucessfully logged in")

#click on logout button
    driver.find_element(By.XPATH,"//a[text()=' Logout']").click()
    time.sleep(1)

#verify if is it showing login page
    assert driver.find_element(By.XPATH,"//h2[text()='Login to your account']").is_displayed()
    print("The person is successfully logged out")

except AssertionError as e:
    print("AssertionError:", e)
except Exception as e:
    print("Error:", e)
finally:
    # Close the browser
    driver.quit()



