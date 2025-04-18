import time
import allure
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver
from selenium import webdriver
from web_locators.locators import AuthLoginLocators
from data.urls import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.user_data import PersonData

# не тестирую на firefox, не работатет action chains, а вместе с ним drag and drop
@allure.step('Открыть браузер')
@pytest.fixture(params=['chrome'])  # ,  'firefox'
def pages(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()

        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1920, 1080)

    elif request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()

        driver = webdriver.Firefox(options=firefox_options)
        driver.set_window_size(1920, 1080)
    driver.get(Urls.url_login)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLoginLocators.EMAIL_FIELD))
    username_field = driver.find_element(*AuthLoginLocators.EMAIL_FIELD)
    username_field.clear()  # Очистка поля перед вводом
    username_field.send_keys(PersonData.user_login)  # Ввод имени пользователя
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLoginLocators.PASSWORD_FIELD))
    password_field = driver.find_element(*AuthLoginLocators.PASSWORD_FIELD)
    password_field.clear()  # Очистка поля перед вводом
    password_field.send_keys(PersonData.user_password)  # Ввод пароля
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthLoginLocators.LOGIN_TEXT_WITH_HREF))
    login_button = driver.find_element(*AuthLoginLocators.LOGIN_TEXT_WITH_HREF)


    driver.execute_script("arguments[0].click();",login_button)  # Клик по кнопке входа
    time.sleep(2)
    driver.get(Urls.url_main)
    yield driver
    driver.quit()
# не тестирую на firefox, не работатет action chains, а вместе с ним drag and drop
@allure.step('Открыть браузер')
@pytest.fixture(params=['chrome']) # , 'firefox'])
def recovery_password(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()

        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1920, 1080)

    elif request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()

        driver = webdriver.Firefox(options=firefox_options)
        driver.set_window_size(1920, 1080)
    driver.get(Urls.url_login)

    yield driver
    driver.quit()
