import unittest
from unittest.main import main
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        print("seting up")
        self.driver = webdriver.Chrome(
            'F:/selenium/chromedriver_win32/chromedriver.exe')
        self.driver.get("http://www.python.org")

    def test_example1(self):
        main_page = page.MainPage(self.driver)
        main_page.is_title_matches()
        print("success 1")
        

    def test_example2(self):
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        print("success 2")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
