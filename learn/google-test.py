import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# FIND ELEMENT BY CLASS NAME
search_box = driver.find_element(By.CLASS_NAME,"gLFyf")
search_box.clear()
search_box.send_keys("Tottenham Hotspurs"+Keys.RETURN)
# assume that search box is not loaded immediately
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)
# find a link with the text: partial - part of the text
site_link = driver.find_element(By.PARTIAL_LINK_TEXT,"Tottenham Hotspur: Official Spurs Website")

site_link.click()
time.sleep(10)
driver.quit()





