# Импорт необходимых для выполнения тестового задания библиотек
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import webbrowser
from selenium.webdriver.common.action_chains import ActionChains
from tkinter import Tk
from Locators import Locators

# Создание класса юнит-тестов
class Drop_box(unittest.TestCase):

# Предусловия
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.dropbox.com"
        self.wait = WebDriverWait(self.driver, 30)
        self.driver.set_page_load_timeout(10)
        self.driver.maximize_window()
        self.loc = Locators()

# Авторизация на сайте (п.а тестового задания)
    def test_sign_in(self, user_email="miixmax@ya.ru", user_password="QwertY11321311!"):
        driver = self.driver
        driver.implicitly_wait(20)
        try:
            driver.get(self.url)
            self.driver.find_element(By.XPATH, self.loc.button_sign_in).click()
            self.driver.find_element(By.XPATH, self.loc.line_email).send_keys(user_email)
            self.driver.find_element(By.XPATH, self.loc.line_password).send_keys(user_password)
            self.driver.find_element(By.XPATH, self.loc.button_sign_come_in).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.login_successful)))
            self.driver.save_screenshot("a. Login successful.png")
        except:
            print("a. Login failed")

# Настройка профиля (выполнение п.b и подпунктов i, ii, iii тестового задания)
    def test_settings_profile(self):
        self.test_sign_in()
# Загрузка фото в профиль (подпункт i тестового задания)
        try:
            self.driver.find_element(By.XPATH, self.loc.button_foto_akk).click()
            self.driver.find_element(By.XPATH, self.loc.button_settings_akk).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.personal_akk)))
            self.driver.find_element(By.XPATH, self.loc.button_change_foto).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.add_foto_akk)))
            self.driver.find_element(By.XPATH, self.loc.download_foto).send_keys(os.getcwd() + '/ava.png')
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.looks_great)))
            self.driver.find_element(By.XPATH, self.loc.button_gotovo).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.avatar_ok)))
            self.driver.save_screenshot("i. Foto is downloaded.png")
        except:
            print("i. Foto not downloaded")
# Изменение имени и фамилии в профиле (подпункт ii тестового задания)
        try:
            self.driver.find_element(By.XPATH, self.loc.button_change_name).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.button_change_name)))
            self.driver.find_element(By.XPATH, self.loc.line_fname).clear()
            self.driver.find_element(By.XPATH, self.loc.line_fname).send_keys("Test")
            self.driver.find_element(By.XPATH, self.loc.line_lname).clear()
            self.driver.find_element(By.XPATH, self.loc.line_lname).send_keys("Task")
            self.driver.find_element(By.XPATH, self.loc.button_change_title).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.name_ok)))
            self.driver.save_screenshot("ii. Name is changed.png")
        except:
            print("ii. Name is not changed")
# Изменение формата даты в профиле (подпункт iii тестового задания)
        try:
            self.driver.find_element(By.XPATH, self.loc.selector_data).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.line_format_data_MM_DD_YYYY)))
            self.driver.find_element(By.XPATH, self.loc.line_format_data_MM_DD_YYYY).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.data_ok)))
            self.driver.save_screenshot("iii. Data format changed.png")
        except:
            print("iii. Data format not changed")

# Работа с файлами (п.b (еще один); пп.с; d; e; f)
    def test_section_my_files(self):
        self.test_settings_profile()
# Переход в раздел "Мои файлы" (п.b (еще один) тестового задания)
        try:
            self.driver.find_element(By.XPATH, self.loc.button_my_files).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.button_create_folder)))
            self.driver.save_screenshot("b. Section My_Files.png")
        except:
            print("b. go to section not completed")
# Создание папки (п.c тестового задания)
        try:
            self.driver.find_element(By.XPATH, self.loc.button_create_folder).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.window_create_folder)))
            self.driver.find_element(By.XPATH, self.loc.line_name_folder).send_keys("New folder")
            self.driver.find_element(By.XPATH, self.loc.button_create).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.folder_created_ok)))
            self.driver.save_screenshot("c. Folder created.png")
        except:
            print("c. Folder not created")
# Загрузка файла формата .docx (п.d тестового задания)
        try:
            self.driver.find_element(By.XPATH, self.loc.file_download).send_keys(os.getcwd() + '/Task for testing.docx')
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.file_is_downloaded)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.loc.button_close_1))).click() # Закрытие всплывающего уведомления о загрузке файла
            self.driver.save_screenshot("d. File is downloaded.png")
        except:
            print("b. File not downloaded")
# Проверка наличия загруженного файла, проверка наличия читаемости содержимого файла в режиме "превью" (п.e тестового задания)
        try:
            self.driver.find_element(By.XPATH, self.loc.file_is_downloaded).click()
            self.driver.find_element(By.XPATH, self.loc.file_is_downloaded).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.view_content)))
            self.driver.save_screenshot("e. Content is view and has writen.png")
        except:
            print("e. Content not view")
# Переименование файла (п.f тестового задания)
        try:
            self.driver.find_element(By.XPATH, self.loc.button_back_preview).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.folder_created_ok)))
            self.driver.find_element(By.XPATH, self.loc.button_over_actions_for_file).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.button_rename_file)))
            self.driver.find_element(By.XPATH, self.loc.button_rename_file).click()
            action = ActionChains(self.driver)
            action.send_keys("OS33_test")
            action.send_keys(Keys.ENTER)
            action.perform()
            self.driver.save_screenshot("f. rename file is complete.png")
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.loc.button_close_1))).click()
        except:
            print("f. rename file not complete")

# Отправка файла, формирование и копирование ссылки (п.g тестового задания)
    def test_send_file(self):
        self.test_section_my_files()
# Отправка файла
        self.driver.find_element_by_xpath("//span[text()='OS33_test.docx']").click()
        self.driver.find_element(By.XPATH, self.loc.button_over_actions_for_file).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.button_share)))
        self.driver.find_element(By.XPATH, self.loc.button_share).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.button_create_link))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.loc.button_close_1))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.button_copy_link))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.loc.button_close_1))).click()
        self.driver.find_element(By.XPATH, self.loc.line_send_email).send_keys('miixmax@ya.ru')
        self.driver.find_element(By.XPATH, self.loc.button_share_to_email).click()
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.loc.message_message_send_is_complete)))
            self.driver.save_screenshot("g. File is send.png")
        except:
            print("g. is not complete")

# Открытие ссылки в режиме инкогнито (п.h тестового задания)
    def test_browser_incognito(self):
        self.test_send_file()
        c = Tk()
        link = c.clipboard_get()
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
        webbrowser.get(chrome_path).open_new(link)

# Постусловия
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()