import time
import unittest
import os
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from input_discussion import TITLE_254, TITLE_255, TITLE_256
from selenium.webdriver.common.action_chains import ActionChains

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
        course = driver.find_element(By.PARTIAL_LINK_TEXT, "History: Russia in Revolution")
        course.click()

    def test_choose_course(self):
        self.choose_course()

    def switch_button(self):
        self.choose_course()
        driver = self.driver
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div//input[@data-context='934']"))

        )

        button = driver.find_element(By.XPATH, "//div//input[@data-context='934']")
        button.click()
        time.sleep(2)

    def test_switch_button(self):

        self.switch_button()

    def choose_edit_condition(self):
        self.switch_button()
        driver = self.driver
        # completion_button = driver.find_elements(By.XPATH, "//button[@data-toggle='dropdown']")
        # completion_button[1].click()
        # choose_edit_button = driver.find_element(By.XPATH,"//a[@class='btn btn-sm px-2 py-0' and contains(@href, 'https://school.moodledemo.net/course/modedit.php?update=562&showonly=activitycompletionheader')]")
        # choose_edit_button.click()
        self.driver.get('https://school.moodledemo.net/course/modedit.php?update=574&showonly=activitycompletionheader')
        time.sleep(2)

    def test_choose_edit_condition(self):
        self.choose_edit_condition()

    def save_and_return(self):
        driver = self.driver
        save_button = driver.find_element(By.ID, "id_submitbutton2")
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
        none_button = driver.find_element(By.ID, "id_completion_0")
        none_button.click()
        self.save_and_return()

    def case_stu_manually_mark_completion_no_reminder(self):
        self.unlock_completion_setting()
        driver = self.driver
        manual_mark_button = driver.find_element(By.ID, "id_completion_1")
        manual_mark_button.click()

    def test_case_stu_manually_mark_completion_no_reminder(self):
        self.case_stu_manually_mark_completion_no_reminder()
        self.save_and_return()

    def stu_manually_mark_completion_reminder_enable(self, date, month, year, hour, min):
        self.unlock_completion_setting()
        driver = self.driver
        enable_button = driver.find_element(By.ID, "id_completionexpected_enabled")
        enable_button.click()
        # set date-month-year hour-min
        date_box = Select(driver.find_element(By.ID, "id_completionexpected_day"))
        date_box.select_by_value(date)
        month_box = Select(driver.find_element(By.ID, "id_completionexpected_month"))
        month_box.select_by_visible_text(month)
        year_box = Select(driver.find_element(By.ID, "id_completionexpected_year"))
        year_box.select_by_visible_text(year)

        hour_box = Select(driver.find_element(By.ID, "id_completionexpected_hour"))
        hour_box.select_by_visible_text(hour)
        min_box = Select(driver.find_element(By.ID, "id_completionexpected_minute"))
        min_box.select_by_visible_text(min)
        self.save_and_return()

    def test_case_stu_manually_mark_completion_reminder_normal_date(self):
        self.stu_manually_mark_completion_reminder_enable('15', 'April', '2024', '00', '00')

    def test_case_stu_manually_mark_completion_reminder_28_Feb_leap_year(self):
        self.stu_manually_mark_completion_reminder_enable('28', 'February', '2024', '00', '00')

    def test_case_stu_manually_mark_completion_reminder_29_Feb_leap_year(self):
        self.stu_manually_mark_completion_reminder_enable('29', 'February', '2024', '00', '00')

    def test_case_stu_manually_mark_completion_reminder_30_Feb_leap_year(self):
        self.stu_manually_mark_completion_reminder_enable('30', 'February', '2024', '00', '00')

    def test_case_stu_manually_mark_completion_reminder_28_Feb_non_leap(self):
        self.stu_manually_mark_completion_reminder_enable('28', 'February', '2023', '00', '00')

    def test_case_stu_manually_mark_completion_reminder_29_Feb_non_leap(self):
        self.stu_manually_mark_completion_reminder_enable('29', 'February', '2023', '00', '00')

    def test_case_stu_manually_mark_completion_reminder_30_Feb_non_leap(self):
        self.stu_manually_mark_completion_reminder_enable('30', 'February', '2023', '00', '00')

    def test_case_stu_manually_mark_completion_reminder_31_April(self):
        self.stu_manually_mark_completion_reminder_enable('31', 'April', '2023', '00', '00')

    def test_case_stu_manually_mark_completion_reminder_year_of_2023(self):
        self.stu_manually_mark_completion_reminder_enable('15', 'April', '2023', '00', '00')

    def input_min_attempt(self, attempt):
        driver = self.driver
        minimum_attempt_input = driver.find_element(By.ID, "id_completionminattempts")
        minimum_attempt_input.clear()
        minimum_attempt_input.send_keys(attempt)

    def case_stu_manually_mark_completion_reminder_set_min_attempt(self, attempt):
        self.unlock_completion_setting()
        driver = self.driver
        add_requirements_button = driver.find_element(By.ID, 'id_completion_2')
        add_requirements_button.click()
        minimum_attempt_checkbox = driver.find_element(By.ID, "id_completionminattemptsenabled")
        if minimum_attempt_checkbox.is_selected():
            self.input_min_attempt(attempt)
        else:
            minimum_attempt_checkbox.click()
            self.input_min_attempt(attempt)
        self.save_and_return()

    def test_case_stu_manually_mark_completion_reminder_set_min_attempt_minus_val(self):
        self.case_stu_manually_mark_completion_reminder_set_min_attempt(-1)

    def test_case_stu_manually_mark_completion_reminder_set_min_attempt_zero(self):
        self.case_stu_manually_mark_completion_reminder_set_min_attempt(0)

    def test_case_stu_manually_mark_completion_reminder_set_min_attempt_one(self):
        self.case_stu_manually_mark_completion_reminder_set_min_attempt(1)

    def test_case_stu_manually_mark_completion_reminder_set_min_attempt_max_val_lower_bound(self):
        self.case_stu_manually_mark_completion_reminder_set_min_attempt(9223372036854775806)

    def test_case_stu_manually_mark_completion_reminder_set_min_attempt_max_val_limit(self):
        self.case_stu_manually_mark_completion_reminder_set_min_attempt(9223372036854775807)

    def test_case_stu_manually_mark_completion_reminder_set_min_attempt_max_val_upper_bound(self):
        self.case_stu_manually_mark_completion_reminder_set_min_attempt(9223372036854775808)

    # Test add discussion function from here

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

    def add_discussion_test_subject_limit(self, characters, messasge):
        self.add_discussion()
        driver = self.driver
        subject_box = driver.find_element(By.ID, "id_subject")
        subject_box.send_keys(characters)
        time.sleep(10)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        p_element = driver.find_element(By.XPATH, "/html/body/p")

        # Send text to the <p> tag element
        p_element.send_keys(messasge)
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

    def add_discussion_with_file(self, fileName):
        driver = self.driver
        self.add_discussion_test_subject_limit(TITLE_254, "Hello World")
        advanced_button = driver.find_element(By.ID, "id_advancedadddiscussion")
        advanced_button.click()
        time.sleep(2)
        upload_frame = driver.find_element(By.XPATH, "//a/i[@class='icon fa fa-file-o fa-fw ']")
        upload_frame.click()
        time.sleep(2)
        choose_file = driver.find_element(By.XPATH, "//input[@type='file' and @name='repo_upload_file']")
        choose_file.send_keys(os.getcwd() + f'\{fileName}')
        time.sleep(10)
        upload_this_file = driver.find_element(By.XPATH,"//button[@class='fp-upload-btn btn-primary btn']")
        upload_this_file.click()
        time.sleep(10)
        self.post_to_forum()

    def test_add_discussion_with_file_1mb(self):
        self.add_discussion_with_file('file-1mb')


    def test_add_discussion_with_file_2mb(self):
        self.add_discussion_with_file('file-2mb')


    def test_add_discussion_with_file_10kb(self):
        self.add_discussion_with_file('file-10kb')


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
