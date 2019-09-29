from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators


class Yandex(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://yandex.ru"
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.set_page_load_timeout(10)
        self.driver.maximize_window()
        self.loc = Locators()

    def test_Weather(self):
        driver = self.driver
        driver.get(self.url)
        try:
            self.driver.find_element(By.XPATH, self.loc.search_string).send_keys("погода")
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.select_weather)))
            self.driver.find_element(By.XPATH, self.loc.select_weather).click()
            self.driver.find_element(By.XPATH, self.loc.result_weather)
            print('test of WEATHER is complete')
        except: print('test of WEATHER is NOT working')


    def test_Lipetsk(self):
        driver = self.driver
        driver.get(self.url)
        try:
            self.driver.find_element(By.XPATH, self.loc.search_string).send_keys("Липецк")
            self.driver.find_element(By.XPATH, self.loc.search_button).click()
            self.driver.find_element(By.XPATH, self.loc.result_lipetsk)
            print('test of LIPETSK is complete')
        except: print('test of LIPETSK is NOT working')

    def test_loto(self):
        driver = self.driver
        driver.get(self.url)
        try:
            self.driver.find_element(By.XPATH, self.loc.search_string).send_keys("лото")
            self.driver.find_element(By.XPATH, self.loc.search_button).click()
            self.driver.find_element(By.XPATH, self.loc.result_loto)
            print('test of LOTO is complete')
        except: print('test of LOTO is NOT working')

    def test_Images(self):
        driver = self.driver
        driver.get(self.url)
        try:
            self.driver.find_element(By.XPATH, self.loc.button_img).click()
            self.driver.find_element(By.XPATH, self.loc.result_img_myCollections)
            self.driver.find_element(By.XPATH, self.loc.result_img_myTape)
            print('test of IMAGES is complete')
        except: print('test of IMAGES is NOT working')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()