# tests/test_registration.py

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import *
from conftest import generate_email


def wait_for_error_class(driver, input_locator, timeout=15):
    """Ждёт появления error-класса у родительского div"""
    WebDriverWait(driver, timeout).until(
        lambda d: "input_inputError__" in
        d.find_element(*input_locator)
        .find_element(By.XPATH, "./..")
        .get_attribute("class")
    )


def wait_for_error_and_red_fields(driver):
    """Ждёт текст ошибки и покраску всех полей"""
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(EMAIL_ERROR_TEXT)
    )

    for locator in (EMAIL_INPUT, PASSWORD_INPUT, CONFIRM_PASSWORD):
        wait_for_error_class(driver, locator)


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(REGISTER_LINK)
        )

        driver.find_element(*REGISTER_LINK).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(EMAIL_INPUT)
        )

        email = generate_email()
        driver.find_element(*EMAIL_INPUT).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys("Password123!")
        driver.find_element(*CONFIRM_PASSWORD).send_keys("Password123!")

        driver.find_element(*CREATE_ACCOUNT).click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(USER_PROFILE_BLOCK)
        )

        assert driver.find_element(*USER_PROFILE_BLOCK).is_displayed()
        assert "User." in driver.find_element(*USER_PROFILE_BLOCK).text


    def test_invalid_email_format(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable(REGISTER_LINK))
        driver.find_element(*REGISTER_LINK).click()

        driver.find_element(*EMAIL_INPUT).send_keys("invalid-email")
        driver.find_element(*CREATE_ACCOUNT).click()

        wait_for_error_and_red_fields(driver)

        error_element = driver.find_element(*EMAIL_ERROR_TEXT)
        assert error_element.is_displayed()
        assert "Ошибка" in error_element.text

        # Проверяем, что у родительского div есть error-класс
        for locator in (EMAIL_INPUT, PASSWORD_INPUT, CONFIRM_PASSWORD):
            parent_div = driver.find_element(*locator).find_element(By.XPATH, "./..")
            assert "input_inputError__" in parent_div.get_attribute("class")


    def test_existing_user_registration(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable(REGISTER_LINK))
        driver.find_element(*REGISTER_LINK).click()

        driver.find_element(*EMAIL_INPUT).send_keys("arahamiya_29@gmail.com")
        driver.find_element(*PASSWORD_INPUT).send_keys("1994Nika!")
        driver.find_element(*CONFIRM_PASSWORD).send_keys("1994Nika!")

        driver.find_element(*CREATE_ACCOUNT).click()

        wait_for_error_and_red_fields(driver)

        error_element = driver.find_element(*EMAIL_ERROR_TEXT)
        assert error_element.is_displayed()
        assert "Ошибка" in error_element.text

        for locator in (EMAIL_INPUT, PASSWORD_INPUT, CONFIRM_PASSWORD):
            parent_div = driver.find_element(*locator).find_element(By.XPATH, "./..")
            assert "input_inputError__" in parent_div.get_attribute("class")