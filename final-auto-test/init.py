import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

base_url = "https://school.moodledemo.net/login/index.php"
username = "teacher"
password = "moodle"


class InitTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(base_url)
        self.username = username
        self.password = password

    def test_login(self):
        driver = self.driver

        username_box = driver.find_element(By.ID, "username")
        username_box.send_keys(self.username)
        password_box = driver.find_element(By.ID, "password")
        password_box.send_keys(self.password+Keys.RETURN)
    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()

