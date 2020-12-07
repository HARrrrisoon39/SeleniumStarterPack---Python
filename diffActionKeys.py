from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome(
    chrome_options=options, executable_path=r'C:/Users/Buddha/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
driver.get('https://orteil.dashnet.org/cookieclicker/')
driver.implicitly_wait(7)

bigCookie = driver.find_element_by_id('bigCookie')
bigCookieCount = driver.find_element_by_id('cookies')
terms = driver.find_elements_by_id('productPrice0')
action = ActionChains(driver) 
action.click(bigCookie) 

for i in range(7000):
    action.perform()
    count = int(bigCookieCount.text.split()[0])
    for term in terms:
        value = int(term.text)
        if value <= count:
            action.click(term) 
            action.perform()
            print("Hello World!")


    # while int(count) <= 20:
        


# time.sleep(7)
# driver.quit()