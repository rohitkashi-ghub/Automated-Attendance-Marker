from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

PATH = "/Users/rohitkashi/Desktop/PythonCourse/chromedriver"
# Change the path to wherever you've installed chromedriver. It'll be C:\..... for windows

driver = webdriver.Chrome(PATH)
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(7)  # gives an implicit wait for 7 seconds

driver.get("https://lms-practice-school.bits-pilani.ac.in/login/index.php")
link = driver.find_element_by_link_text("Google")
link.click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='email']")))
element.send_keys(os.environ.get('email_user'))  # enter your email ID
element.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
element.send_keys(os.environ.get('email_pass'))  # enter your password
element.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, '5949'))) # replace x by the 4 numbers that correspond to your course on lms
element.click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='instancename'] ")))
link1 = driver.find_elements_by_xpath("//span[@class='instancename'] ")
for attendance in link1:
    if attendance.text == "Attendance":
        attendance.click()
        break

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Submit attendance')))
element.click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, '//input [@id="id_status_641"]')))
element.click()

time.sleep(3)

submit = driver.find_element_by_xpath("//input[@id='id_submitbutton']")
submit.click()
time.sleep(2)
driver.close()


