from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome(
    chrome_options=options, executable_path=r'F:/selenium/chromedriver_win32/chromedriver.exe')
driver.get('https://www.techwithtim.net/')




element = driver.find_element_by_link_text("Community") 
   
# create action chain object 
action = ActionChains(driver) 
   
# click the item 
action.move_to_element(element) 
   
# perform the operation 
action.perform() 