import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Chrome()
driver.get("https://school.moodledemo.net/login/index.php")

enter_username = driver.find_element(By.ID, "username")
enter_username.clear()
enter_username.send_keys("teacher")

enter_password = driver.find_element(By.ID, "password")
enter_password.send_keys("moodle")
submit = driver.find_element(By.ID, "loginbtn")
submit.submit()

time.sleep(10)
