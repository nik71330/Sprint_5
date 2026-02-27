# conftest.py 
 
import pytest 
from selenium import webdriver 
import random 
import string 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait 
from locators import * 
 
def generate_email(): 
    return f"test_{random.randint(1000, 9999)}@example.com" 
 
@pytest.fixture(scope="function") 
def driver(): 
    driver = webdriver.Chrome()  
    driver.maximize_window() 
    yield driver 
    driver.quit()