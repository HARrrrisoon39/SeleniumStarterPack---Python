from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome(
    chrome_options=options, executable_path=r'C:/Users/Buddha/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
driver.get('https://www.techwithtim.net/')
print(driver.title)

search = driver.find_element_by_name('s')
# search = driver.find_element_by_class_name('s')
search.send_keys("html")
search.send_keys(Keys.RETURN)  


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    summary = element.find_elements_by_tag_name('article')
    for article in summary:
        title = article.find_element_by_class_name('entry-summary')
        print(title.text)

finally:
    driver.quit()
    
