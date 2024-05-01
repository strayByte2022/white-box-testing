import time
import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
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

    def switch_button(self):
        self.choose_course()
        driver = self.driver
        WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.XPATH,"//div//input[@data-context='934']"))

        )

        button = driver.find_element(By.XPATH,"//div//input[@data-context='934']")
        button.click()
        time.sleep(2)

    def test_switch_button(self):

        self.switch_button()

    def choose_edit_condition(self):
        self.switch_button()
        driver = self.driver
        completion_button = driver.find_elements(By.XPATH, "//button[@data-toggle='dropdown']")
        completion_button[1].click()
        choose_edit_button = driver.find_element(By.XPATH,"//a[@class='btn btn-sm px-2 py-0' and contains(@href, 'https://school.moodledemo.net/course/modedit.php?update=562&showonly=activitycompletionheader')]")
        choose_edit_button.click()
        time.sleep(2)

    def test_choose_edit_condition(self):
        self.choose_edit_condition()

    def save_and_return(self):
        driver = self.driver
        save_button = driver.find_element(By.ID,"id_submitbutton2")
        save_button.click()

    def unlock_completion_setting(self):
        self.choose_edit_condition()
        driver = self.driver
        try:
            unlock_button = driver.find_element(By.ID, "id_unlockcompletion")
            unlock_button.click()
        except NoSuchElementException:
            print("Unlock button not found. Already clicked or not available.")

    def test_case_no_completion_condition(self):
        self.unlock_completion_setting()
        driver = self.driver
        none_button = driver.find_element(By.ID,"id_completion_0")
        none_button.click()
        self.save_and_return()

    def case_stu_manually_mark_completion_no_reminder(self):
        self.unlock_completion_setting()
        driver = self.driver
        manual_mark_button = driver.find_element(By.ID,"id_completion_1")
        manual_mark_button.click()

    def test_case_stu_manually_mark_completion_no_reminder(self):
        self.case_stu_manually_mark_completion_no_reminder()
        self.save_and_return()

    def stu_manually_mark_completion_reminder_enable(self):
        self.unlock_completion_setting()
        driver = self.driver
        enable_button = driver.find_element(By.ID,"id_completionexpected_enabled")
        enable_button.click()

    def test_case_stu_manually_mark_completion_reminder_normal_date(self):
        self.stu_manually_mark_completion_reminder_enable()
        self.save_and_return()

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()

