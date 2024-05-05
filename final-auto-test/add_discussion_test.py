import time
import unittest
import os
import json
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from input_discussion import TITLE_254, TITLE_255, TITLE_256


with open('input_discussion.json') as json_file:
    data = json.load(json_file)

course = data['courseName']
course_link = data['courseAlternative']
activity = data['activityLink']
base_url = data['base_url']
username = data['username']
password = data['password']


class DiscussionTesting(unittest.TestCase):
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
        try:
            course_name = driver.find_element(By.PARTIAL_LINK_TEXT, course)
            course_name.click()
        except NoSuchElementException:
            driver.get(course_link)

    def enter_discussion_page(self):
        self.choose_course()
        driver = self.driver
        class_discussion = driver.find_element(By.PARTIAL_LINK_TEXT, "Class discussions")
        class_discussion.click()

    def add_discussion(self):
        self.enter_discussion_page()
        driver = self.driver
        add_discussion_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Add discussion topic")
        add_discussion_button.click()

    def post_to_forum(self):
        driver = self.driver
        post_to_forum = driver.find_element(By.ID, "id_submitbutton")
        post_to_forum.click()

    def add_discussion_test_subject_limit(self, characters, message):
        self.add_discussion()
        driver = self.driver
        subject_box = driver.find_element(By.ID, "id_subject")
        subject_box.send_keys(characters)
        time.sleep(10)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        p_element = driver.find_element(By.XPATH, "/html/body/p")

        # Send text to the <p> tag element
        p_element.send_keys(message)
        driver.switch_to.default_content()

    def test_add_discussion_test_subject_limit_254(self):
        self.add_discussion_test_subject_limit(TITLE_254, "Hello World")
        self.post_to_forum()

    def test_add_discussion_test_subject_limit_255(self):
        self.add_discussion_test_subject_limit(TITLE_255, "Hello World")
        self.post_to_forum()

    def test_add_discussion_test_subject_limit_256(self):
        self.add_discussion_test_subject_limit(TITLE_256, "Hello World")
        self.post_to_forum()

    def test_add_discussion_test_empty_message(self):
        self.add_discussion_test_subject_limit(TITLE_254, "")
        self.post_to_forum()

    def add_discussion_with_file(self, title, message, fileName):
        driver = self.driver
        self.add_discussion_test_subject_limit(title, message)
        advanced_button = driver.find_element(By.ID, "id_advancedadddiscussion")
        advanced_button.click()
        time.sleep(2)
        upload_frame = driver.find_element(By.XPATH, "//a/i[@class='icon fa fa-file-o fa-fw ']")
        upload_frame.click()
        time.sleep(2)
        choose_file = driver.find_element(By.XPATH, "//input[@type='file' and @name='repo_upload_file']")
        choose_file.send_keys(os.getcwd() + f'\{fileName}')
        time.sleep(10)
        upload_this_file = driver.find_element(By.XPATH, "//button[@class='fp-upload-btn btn-primary btn']")
        upload_this_file.click()
        time.sleep(10)
        self.post_to_forum()

    # test file upload limitation
    def test_add_discussion_with_file_1mb(self):
        self.add_discussion_with_file(TITLE_254, "Hello World", 'file-1mb')

    def test_add_discussion_with_file_2mb(self):
        self.add_discussion_with_file(TITLE_254, "Hello World", 'file-2mb')

    def test_add_discussion_with_file_10kb(self):
        self.add_discussion_with_file(TITLE_254, "Hello World", 'file-10kb')

    def test_add_discussion_with_parameter_from_file(self):
        case = data['case_n']
        self.add_discussion_with_file(case['title'], case['message'], case['file_name'])

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
