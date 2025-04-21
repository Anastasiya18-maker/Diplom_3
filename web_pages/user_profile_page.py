import allure
from data.urls import Urls
from web_locators.locators import UserProfileLocators, OrdersPageLocators, MainPageLocators, AuthLoginLocators
from web_pages.base_page import BasePage


class UserProfilePage(BasePage):

    @allure.step('Проверяем переход на страницу профиля')
    def check_switch_on_profile(self):
        self.check_url(Urls.url_profile)
        return self.get_current_url()

    @allure.step('Нажимаем кнопку «История заказов»')
    def click_order_history_button(self):
        self.wait_for_element_to_be_clickable(UserProfileLocators.ORDER_HISTORY_BUTTON)
        self.click_on_element(UserProfileLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Проверяем переход на страницу История заказов')
    def check_switch_on_order_history(self):
        self.wait_until_element_visibility(UserProfileLocators.ENABLED_ORDER_HISTORY_BUTTON)
        return self.get_current_url()

    @allure.step('Нажимаем кнопку «Выход»')
    def click_log_out_button(self):
        self.wait_for_element_to_be_clickable(UserProfileLocators.LOGOUT_BUTTON)
        self.click_on_element(UserProfileLocators.LOGOUT_BUTTON)

    def is_order_id_found_at_history(self):
        self.wait_until_element_visibility(OrdersPageLocators.ALL_ORDERS_AT_HISTORY)
        return self.get_actually_text(OrdersPageLocators.ALL_ORDERS_AT_HISTORY)

    def is_order_id_found_at_feed(self):
        self.wait_until_element_visibility(OrdersPageLocators.ALL_ORDERS_AT_FEED)
        return self.get_actually_text(OrdersPageLocators.ALL_ORDERS_AT_FEED)

    @allure.step('Перейти в "ЛК" по кнопке "Личный кабинет"')
    def click_on_account(self):
        self.move_to_element_and_click(MainPageLocators.PROFILE_BUTTON)


    @allure.step('Проверяем переход на страницу Авторизации')
    def check_switch_on_login_page(self):
        self.wait_until_element_visibility(AuthLoginLocators.LOGIN_TEXT)
        return self.get_current_url()