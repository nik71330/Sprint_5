# tests/test_login_logout.py 
 
import pytest 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait 
from locators import * 
from conftest import driver 
 
class TestLoginLogout: 
 
    def test_successful_login(self, driver): 
        driver.get("https://qa-desk.stand.praktikum-services.ru/") 
        driver.find_element(*LOGIN_BUTTON).click() 
        WebDriverWait(driver, 25).until( 
            EC.presence_of_element_located(EMAIL_INPUT) 
        ) 
        driver.find_element(*EMAIL_INPUT).send_keys("arahamiya_29@gmail.com") 
        driver.find_element(*PASSWORD_INPUT).send_keys("1994Nika!") 
        driver.find_element(*SIGN_IN).click() 
 
        WebDriverWait(driver, 25).until( 
            EC.presence_of_element_located(USER_PROFILE_BLOCK) 
        ) 
 
        assert driver.find_element(*USER_PROFILE_BLOCK).is_displayed(), "Аватар не отображается" 
        assert "User." in driver.find_element(*USER_PROFILE_BLOCK).text, "Имя User не отображается" 
  
 
    def test_logout(self, driver): 
        # Сначала логинимся 
        driver.get("https://qa-desk.stand.praktikum-services.ru/") 
        driver.find_element(*LOGIN_BUTTON).click() 
        WebDriverWait(driver, 25).until( 
            EC.presence_of_element_located(EMAIL_INPUT) 
        ) 
        driver.find_element(*EMAIL_INPUT).send_keys("arahamiya_29@gmail.com") 
        driver.find_element(*PASSWORD_INPUT).send_keys("1994Nika!") 
        driver.find_element(*SIGN_IN).click() 
        WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located(USER_PROFILE_BLOCK) 
        ) 
        # Выходим 
        driver.find_element(*LOGOUT_BUTTON).click() 
        # Проверяем, что аватар исчез, появилась кнопка "Вход и регистрация" 
        WebDriverWait(driver, 25).until( 
            EC.presence_of_element_located(LOGIN_BUTTON) 
        ) 
        assert driver.find_element(*LOGIN_BUTTON).is_displayed(), "Кнопка входа не отображается" 
        assert not driver.find_elements(*USER_PROFILE_BLOCK), "Аватар всё ещё отображается"