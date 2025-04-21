import allure
from selenium.webdriver.support.expected_conditions import none_of
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from conftest import SLEEP


class BasePage:

    """Инициализация класса."""
    def __init__(self, gen):
        self.driver = next(gen())

    def not_in_element(self, element, text):
        WebDriverWait(self.driver,SLEEP).until(none_of(EC.text_to_be_present_in_element(element,text)))


    @allure.step('Открываем ссылку')
    def open_link(self, url):
        return self.driver.get(url)

    @allure.step('Кликаем по элементу {locator}')
    def click_on_element(self, locator):
        self.move_to_element_and_click(locator)


    @allure.step('Вставить текст {text}')
    def set_text_to_element(self, locator, text):
        WebDriverWait(self.driver, SLEEP).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получить текущий текст')
    def get_actually_text(self, locator):
        actually_text = self.driver.find_element(*locator).text
        return actually_text

    @allure.step('Проверить присутствие элемента на странице')
    def check_presense(self, locator):
        WebDriverWait(self.driver, SLEEP).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Проверить невидимость элемента')
    def check_invisibility(self, locator) -> object:
        return WebDriverWait(self.driver, SLEEP).until(EC.invisibility_of_element(locator))

    @allure.step('Дождаться видимости элемента')
    def wait_until_element_visibility(self, locator):
        return WebDriverWait(self.driver, SLEEP).until(EC.visibility_of_element_located(locator))

    @allure.step('Получить текущую ссылку')
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step('Перетащить элемент')
    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = self.driver.find_element(*locator_one)
        droppable = self.driver.find_element(*locator_two)
        assert draggable is not None
        assert droppable is not None
        action_chains = ActionChains(self.driver)

        action_chains.pause(SLEEP/2).drag_and_drop(draggable, droppable).pause(SLEEP/2).perform()

    @allure.step('Переместиться до элемента и кликнуть')
    def move_to_element_and_click(self, locator):
        element = self.wait_until_element_visibility(locator)

        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Дождаться кликабельности элемента')
    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, SLEEP).until(EC.element_to_be_clickable(locator))

    @allure.step('Найти элементы на странице')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Дождаться появления текста в элементе')
    def wait_for_text_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.driver, SLEEP).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step("Нахождение нескольких элементов")
    def find_until_all_elements_located(self, locator):
        return WebDriverWait(self.driver, SLEEP).until(EC.presence_of_all_elements_located(locator))

    @allure.step("Проверка перехода по адресу сайта")
    def check_url(self, url):
        WebDriverWait(self.driver, SLEEP).until(EC.url_to_be(url))
