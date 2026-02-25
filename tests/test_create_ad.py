# tests/test_create_ad.py 
 
import pytest 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait 
from locators import * 
from conftest import driver 
 
class TestCreateAd: 
 
    def test_create_ad_unauthorized(self, driver): 
        driver.get("https://qa-desk.stand.praktikum-services.ru/") 
        driver.find_element(*POST_AD_BUTTON).click() 
        # Ждём появления модального окна 
        WebDriverWait(driver, 15).until( 
            EC.presence_of_element_located(AUTH_REQUIRED_TITLE) 
        ) 
        modal_title = driver.find_element(*AUTH_REQUIRED_TITLE) 
        assert modal_title.is_displayed(), "Модальное окно не отображается" 
 
         
     
    def test_create_ad_authorized(self, driver): 
        # Логинимся 
        driver.get("https://qa-desk.stand.praktikum-services.ru/") 
        driver.find_element(*LOGIN_BUTTON).click() 
        WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located(EMAIL_INPUT) 
        ) 
        driver.find_element(*EMAIL_INPUT).send_keys("arahamiya_29@gmail.com") 
        driver.find_element(*PASSWORD_INPUT).send_keys("1994Nika!") 
        driver.find_element(*SIGN_IN).click() 
        WebDriverWait(driver, 15).until( 
            EC.presence_of_element_located(USER_PROFILE_BLOCK) 
        ) 
         
        # Переходим к созданию объявления 
        driver.find_element(*POST_AD_BUTTON).click() 
         
        # Заполняем поля 
        title = "Тестовое объявление" 
        driver.find_element(*TITLE_INPUT).send_keys(title) 
        driver.find_element(*DESCRIPTION_INPUT).send_keys("Описание тестового объявления") 
        driver.find_element(*PRICE_INPUT).send_keys("1000") 
         
        # Выбираем категорию и город 
        driver.find_element(*CATEGORY_DROPDOWN).click() 
 
        driver.find_element(*CITY_DROPDOWN).click() 
 
         
        # Выбираем состояние 
        driver.find_element(*CONDITION_USED).click() 
         
        # Публикуем 
        driver.find_element(*PUBLISH_BUTTON).click() 
         
        # Ждем загрузки страницы после публикации 
        WebDriverWait(driver, 15).until( 
            EC.presence_of_element_located(USER_PROFILE_BLOCK) 
        ) 
         
         
        # ВАРИАНТ 1: Пробуем перейти в профиль по прямому URL 
        driver.get("https://qa-desk.stand.praktikum-services.ru/profile") 
 
         
        # Проверяем, что мы в профиле 
        try: 
            WebDriverWait(driver, 10).until( 
                EC.presence_of_element_located(MY_ADS_BLOCK) 
            ) 
        except: 
            # ВАРИАНТ 2: Если не сработало, пробуем через навигационное меню 
            driver.get("https://qa-desk.stand.praktikum-services.ru/") 
 
             
            # Ищем кнопку профиля на главной 
            try: 
                profile_btn = WebDriverWait(driver, 10).until( 
                    EC.element_to_be_clickable(PROFILE_BUTTON) 
                ) 
                profile_btn.click() 
            except: 
                # ВАРИАНТ 3: Пробуем найти аватарку пользователя 
                try: 
                    avatar = driver.find_element(By.CSS_SELECTOR, ".circleSmall, .avatar, [class*='avatar'], [class*='profile']") 
                    avatar.click() 
                except: 
                    # ВАРИАНТ 4: Пробуем через меню пользователя 
                    driver.find_element(By.CSS_SELECTOR, "[data-testid='user-menu'], .user-menu, .profile-menu").click() 
 
                    driver.find_element(By.XPATH, "//*[text()='Профиль' or text()='Мои объявления']").click() 
         
        # Ждем появления блока "Мои объявления" 
        WebDriverWait(driver, 15).until( 
            EC.presence_of_element_located(MY_ADS_BLOCK) 
        ) 
         
        # Проверяем наличие созданного объявления 
        ad_locator = (By.XPATH, f"//h2[text()='{title}'] | //*[contains(text(), '{title}')]") 
        WebDriverWait(driver, 15).until( 
            EC.presence_of_element_located(ad_locator) 
        )
        assert driver.find_element(*ad_locator).is_displayed(), "Созданное объявление не отображается в профиле"