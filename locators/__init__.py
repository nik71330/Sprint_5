from selenium.webdriver.common.by import By 
 
# Регистрация нового пользователя 
LOGIN_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")                 # кнопка "Вход и регистрация" 
REGISTER_LINK = (By.XPATH, "//button[text()='Нет аккаунта']")    # кнопка "Нет аккаунта" 
CREATE_ACCOUNT = (By.XPATH, "//button[text()='Создать аккаунт']")   # кнопка "Создать аккаунт" 
USER_PROFILE_BLOCK = (By.XPATH, "//div[contains(@class, 'columnSmall')]")           # аватарка после регистрации + имя 
EMAIL_INPUT = (By.XPATH, "//input[@name='email']")                #поле email 
PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")           #поле пароль 
CONFIRM_PASSWORD = (By.XPATH, "//input[@name='submitPassword']")  #поле подтвердждения пароля 
POST_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']") #кнопка "Разместить объявление" 
AUTH_REQUIRED_TITLE = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']") #форма при попытке разместить объявление без регистрации 
 
# Вход зарегистрированного пользователя 
SIGN_IN = (By.XPATH, "//button[text()='Войти']") 
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']") 
 
# Размещение объявления 
TITLE_INPUT = (By.XPATH, "//input[@placeholder='Название']") #поле "Название" 
DESCRIPTION_INPUT = (By.XPATH, "//textarea[@placeholder='Описание товара']") #поле "Описание товара" 
PRICE_INPUT = (By.XPATH, "//input[@placeholder='Стоимость']") #поле "Стоимость" 
CITY_DROPDOWN = (By.XPATH, "//form//div[3]//button[contains(@class, 'dropDownMenu_arrowDown')]")           #выпадашка Город 
CATEGORY_DROPDOWN = (By.XPATH, "//form//div[2]/div[2]//button[contains(@class, 'dropDownMenu_arrowDown')]")         #выпадашка Авто 
CONDITION_NEW = (By.XPATH, "//form//fieldset//div[1]/div")    #радиокнопка состояния Новый 
CONDITION_USED = (By.XPATH, "//form//fieldset//div[2]/div")    #радиокнопка состояния Б/У 
PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']") #кнопка "Опубликовать"  
 
 
# Локаторы для ошибок  
EMAIL_ERROR_TEXT = (By.XPATH, "//span[@class='input_span__yWPqB' and text()='Ошибка']")  # сообщение об ошибке под полем Email 
# Локатор для кнопки профиля  
PROFILE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/button/svg") # Кнопка с аватаркой 
 
# Локатор для блока "Мои объявления"  
MY_ADS_BLOCK = (By.XPATH, "//h1[text()='Мои объявления']")
avatar = (By.CSS_SELECTOR, ".circleSmall, .avatar, [class*='avatar'], [class*='profile']")
URL = ("https://qa-desk.stand.praktikum-services.ru/") 
URL_PROFILE = ("https://qa-desk.stand.praktikum-services.ru/profile")