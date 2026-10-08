from pathlib import Path

import pytest
from pytest_bdd import given, parsers, scenarios, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOGIN_PAGE = PROJECT_ROOT / "app" / "login.html"
FEATURE_FILE = PROJECT_ROOT / "features" / "login.feature"

scenarios(str(FEATURE_FILE))


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@given("que estoy en la página de inicio de sesión")
def open_login_page(driver):
    driver.get(LOGIN_PAGE.as_uri())


@when(parsers.parse('ingreso el correo "{email}"'))
def enter_email(driver, email):
    driver.find_element(By.ID, "correo").send_keys(email)


@when(parsers.parse('ingreso la contraseña "{password}"'))
def enter_password(driver, password):
    driver.find_element(By.ID, "password").send_keys(password)


@when("dejo el correo vacío")
def leave_email_empty(driver):
    driver.find_element(By.ID, "correo").clear()


@when("dejo la contraseña vacía")
def leave_password_empty(driver):
    driver.find_element(By.ID, "password").clear()


@when(parsers.parse('presiono el botón "{button_text}"'))
def submit_login(driver, button_text):
    button = driver.find_element(By.ID, "login-button")
    assert button.text == button_text
    button.click()


@then(parsers.parse('debería ver el mensaje "{expected_message}"'))
def verify_message(driver, expected_message):
    message_locator = (By.ID, "message")
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(message_locator, expected_message)
    )
    assert driver.find_element(*message_locator).text == expected_message