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
from selenium.webdriver.common.action_chains import ActionChains



with open('input_completion_mark.json') as json_file:
    data = json.load(json_file)

course = data['courseName']
course_link = data['courseLink']
activity = data['activityLink']
reminder_date_list = data['reminder_date_list']
attempt_list = data['attempts']
base_url = data['base_url']
username = data['username']
password = data['password']
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
        try:
            course_name = driver.find_element(By.PARTIAL_LINK_TEXT, course)
            course_name.click()
        except NoSuchElementException:
            driver.get(course_link)




    def switch_button(self):
        self.choose_course()
        driver = self.driver
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div//input[@data-context='934']"))

        )

        button = driver.find_element(By.XPATH, "//div//input[@data-context='934']")
        button.click()
        time.sleep(2)

    def choose_edit_condition(self):
        self.switch_button()
        driver = self.driver
        # completion_button = driver.find_elements(By.XPATH, "//button[@data-toggle='dropdown']")
        # completion_button[1].click()
        # choose_edit_button = driver.find_element(By.XPATH,"//a[@class='btn btn-sm px-2 py-0' and contains(@href, 'https://school.moodledemo.net/course/modedit.php?update=562&showonly=activitycompletionheader')]")
        # choose_edit_button.click()
        self.driver.get(activity)
        time.sleep(2)

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

    def test_case_stu_manually_mark_completion_no_reminder(self,):
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
        self.stu_manually_mark_completion_reminder_enable(
                                                          data['normal_date']['date'],
                                                          data['normal_date']['month'],
                                                          data['normal_date']['year'],
                                                          data['normal_date']['hour'],
                                                          data['normal_date']['min'])

    def test_case_stu_manually_mark_completion_reminder_28_Feb_leap_year(self):
        self.stu_manually_mark_completion_reminder_enable(
                                                          data['28_Feb_leap_year']['date'],
                                                          data['28_Feb_leap_year']['month'],
                                                          data['28_Feb_leap_year']['year'],
                                                          data['28_Feb_leap_year']['hour'],
                                                          data['28_Feb_leap_year']['min'])

    def test_case_stu_manually_mark_completion_reminder_29_Feb_leap_year(self):
        self.stu_manually_mark_completion_reminder_enable(
                                                          data['29_Feb_leap_year']['date'],
                                                          data['29_Feb_leap_year']['month'],
                                                          data['29_Feb_leap_year']['year'],
                                                          data['29_Feb_leap_year']['hour'],
                                                          data['29_Feb_leap_year']['min'])

    def test_case_stu_manually_mark_completion_reminder_30_Feb_leap_year(self):
        self.stu_manually_mark_completion_reminder_enable(
                                                          data['30_Feb_leap_year']['date'],
                                                          data['30_Feb_leap_year']['month'],
                                                          data['30_Feb_leap_year']['year'],
                                                          data['30_Feb_leap_year']['hour'],
                                                          data['30_Feb_leap_year']['min'])

    def test_case_stu_manually_mark_completion_reminder_28_Feb_non_leap(self):
        self.stu_manually_mark_completion_reminder_enable(
                                                          data['28_Feb_non_leap_year']['date'],
                                                          data['28_Feb_non_leap_year']['month'],
                                                          data['28_Feb_non_leap_year']['year'],
                                                          data['28_Feb_non_leap_year']['hour'],
                                                          data['28_Feb_non_leap_year']['min'])

    def test_case_stu_manually_mark_completion_reminder_29_Feb_non_leap(self):
        self.stu_manually_mark_completion_reminder_enable(
                                                          data['29_Feb_non_leap_year']['date'],
                                                          data['29_Feb_non_leap_year']['month'],
                                                          data['29_Feb_non_leap_year']['year'],
                                                          data['29_Feb_non_leap_year']['hour'],
                                                          data['29_Feb_non_leap_year']['min'])

    def test_case_stu_manually_mark_completion_reminder_30_Feb_non_leap(self):
        self.stu_manually_mark_completion_reminder_enable(
                                                          data['30_Feb_non_leap_year']['date'],
                                                          data['30_Feb_non_leap_year']['month'],
                                                          data['30_Feb_non_leap_year']['year'],
                                                          data['30_Feb_non_leap_year']['hour'],
                                                          data['30_Feb_non_leap_year']['min'])

    def test_case_stu_manually_mark_completion_reminder_31_April(self):
        self.stu_manually_mark_completion_reminder_enable(
                                                          data['30_April']['date'],
                                                          data['30_April']['month'],
                                                          data['30_April']['year'],
                                                          data['30_April']['hour'],
                                                          data['30_April']['min'])

    def test_case_stu_manually_mark_completion_reminder_year_of_2023(self):
        self.stu_manually_mark_completion_reminder_enable(
                                                          data['year_of_2023']['date'],
                                                          data['year_of_2023']['month'],
                                                          data['year_of_2023']['year'],
                                                          data['year_of_2023']['hour'],
                                                          data['year_of_2023']['min'])

    # for reading from list
    def test_case_stu_manually_mark_completion_reminder_with_cases_from_list(self):
        for case in reminder_date_list:
            self.stu_manually_mark_completion_reminder_enable(
                                                              reminder_date_list[case]['date'],
                                                              reminder_date_list[case]['month'],
                                                              reminder_date_list[case]['year'],
                                                              reminder_date_list[case]['hour'],
                                                              reminder_date_list[case]['min'])
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
        self.case_stu_manually_mark_completion_reminder_set_min_attempt(data['attempt_minus'])

    def test_case_stu_manually_mark_completion_reminder_set_min_attempt_zero(self):
        self.case_stu_manually_mark_completion_reminder_set_min_attempt(0)

    def test_case_stu_manually_mark_completion_reminder_set_min_attempt_one(self):
        self.case_stu_manually_mark_completion_reminder_set_min_attempt(data['attempt_positive'])

    def test_case_stu_manually_mark_completion_reminder_set_min_attempt_max_val_lower_bound(self):
        self.case_stu_manually_mark_completion_reminder_set_min_attempt(9223372036854775806)

    def test_case_stu_manually_mark_completion_reminder_set_min_attempt_max_val_limit(self):
        self.case_stu_manually_mark_completion_reminder_set_min_attempt(99223372036854775807)

    def test_case_stu_manually_mark_completion_reminder_set_min_attempt_max_val_upper_bound(self):
        self.case_stu_manually_mark_completion_reminder_set_min_attempt(9223372036854775808)
    def test_case_stu_manually_mark_completion_reminder_set_min_attempt_illegal(self):
        illegal_list = data['wrong_format_attempt']
        for attempt in illegal_list:
            self.case_stu_manually_mark_completion_reminder_set_min_attempt(attempt)

    def test_case_stu_manually_mark_completion_reminder_set_min_attempt_from_list(self):
        for case in reminder_date_list:
            self.case_stu_manually_mark_completion_reminder_set_min_attempt(attempt_list[case])

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
