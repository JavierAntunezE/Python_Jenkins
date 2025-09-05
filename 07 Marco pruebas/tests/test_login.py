# archivo: test_login.py
import time
import unittest
from selenium import webdriver

from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.db_helper import Database

class TestLogin(unittest.TestCase):

    def setUp(self): #Se ejecuta antes de cada función
        self.config_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.db = Database(
            server="localhost",
            database="TestLoginDB",
            username="userPythonDB",
            password="Abc.123"
        )

    def config_options(self):
        self.options = webdriver.ChromeOptions()
        prefs = {
             "profile.password_manager_leak_detection": False
        }
        self.options.add_experimental_option("prefs", prefs)
        self.options.add_argument('--headless')

    def test_login_valido(self): #Test de login exitoso
        user = self.db.get_user("standard_user")  # Devuelve ("admin", "admin123")
        username, password = user

        self.login_page.wait_until_loaded()
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login()

        # Espera explícita a que cargue la página de inventario
        WebDriverWait(self.driver, 5).until(
            EC.url_contains("inventory.html"))

    def tearDown(self): #Se ejecuta después de cada función
        time.sleep(0.5)
        self.db.close()
        self.driver.quit()

if __name__ == "__main__": #Solo se ejecuta si el archivo se corre directamente
    unittest.main() #Ejecuta automáticamente todas las funciones que comienzan con test_