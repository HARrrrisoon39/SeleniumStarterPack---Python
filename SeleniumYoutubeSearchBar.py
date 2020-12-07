from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome(
    chrome_options=options, executable_path=r'C:/Users/Buddha/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
driver.get('https://www.youtube.com/')

search = driver.find_element_by_tag_name('search')
search = driver.find_element_by_name('search_query')
search.send_keys("sometext")

click = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
click.click()

back = driver.find_element_by_xpath('//*[@id="endpoint"]/paper-item')
back.click()
