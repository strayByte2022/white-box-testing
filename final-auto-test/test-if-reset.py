import time
import schedule
from test_completion_conditioning import InitTesting

def scheduled_job():
    InitTesting().test_case_stu_manually_mark_completion_reminder_year_of_2023()
    time.sleep(5)

schedule.every().hour.at(":59:59").do(scheduled_job)

while True:
    schedule.run_pending()
    time.sleep(60)  # Check for scheduled tasks every 60 seconds
