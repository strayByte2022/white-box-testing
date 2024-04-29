import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
base_url = "https://school.moodledemo.net/login/index.php"
username = "teacher"
password = "moodle"


class InitTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(base_url)
        self.username = username
        self.password = password

    def login(self):
        driver = self.driver

        username_box = driver.find_element(By.ID, "username")
        username_box.send_keys(self.username)
        password_box = driver.find_element(By.ID, "password")
        password_box.send_keys(self.password + Keys.RETURN)

    def test_login(self):
        self.login()

    def choose_course(self):
        self.login()
        driver = self.driver
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "History: Russia in Revolution"))
        )
        course = driver.find_element(By.PARTIAL_LINK_TEXT,"History: Russia in Revolution")
        course.click()

    def test_choose_course(self):
        self.choose_course()

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()

