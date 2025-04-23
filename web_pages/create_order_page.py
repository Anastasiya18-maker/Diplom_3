import allure
from web_locators.locators import OrdersPageLocators, MainPageLocators, UserProfileLocators
from web_pages.base_page import BasePage
from data.urls import Urls

class CreateOrderPage(BasePage):
    @allure.step('Переход в "Конструктор"')
    def click_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_until_element_visibility(MainPageLocators.MAIN_LIST_TITLE)

    @allure.step('Проверяем переход на страницу История заказов')
    def check_switch_on_order_history(self):
        self.wait_until_element_visibility(UserProfileLocators.ENABLED_ORDER_HISTORY_BUTTON)
        return self.get_current_url()

    @allure.step('Нажимаем кнопку «История заказов»')
    def click_order_history_button(self):
        self.wait_for_element_to_be_clickable(UserProfileLocators.ORDER_HISTORY_BUTTON)
        self.click_on_element(UserProfileLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Проверяем переход на страницу профиля')
    def check_switch_on_profile(self):
        self.check_url(Urls.url_profile)
        return self.get_current_url()


    @allure.step('Переход на страницу Лента заказов')
    def click_orders_list_button(self):
        self.move_to_element_and_click(MainPageLocators.ORDERS_LIST_BUTTON)
        self.wait_until_element_visibility(OrdersPageLocators.ORDERS_LIST_TITLE)


    @allure.step('Перейти в "ЛК" по кнопке "Личный кабинет"')
    def click_on_account(self):
        self.move_to_element_and_click(MainPageLocators.PROFILE_BUTTON)


    @allure.step("Закрыть модальное окно после создания заказа")
    def click_close_modal_order(self):
        self.move_to_element_and_click(MainPageLocators.CROSS_BUTTON)


    @allure.step('Проверяем, что заказ оформлен и появился идентификатор заказа')
    def check_show_window_with_order_id(self):
        self.wait_until_element_visibility(MainPageLocators.ORDER_IDENTIFICATE)
        return self.get_actually_text(MainPageLocators.ORDER_IDENTIFICATE)

    @allure.step('Добавить ингридиент в заказ')
    def add_filling_to_order(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BUN_INGREDIENT)
        self.wait_for_element_to_be_clickable(MainPageLocators.ORDER_BASKET)

        self.drag_and_drop_on_element(MainPageLocators.BUN_INGREDIENT, MainPageLocators.ORDER_BASKET)

    @allure.step('Получение ORDER_ID')
    def get_with_order_id(self):
        self.wait_until_element_visibility(MainPageLocators.ORDER_IDENTIFICATE)
        self.not_in_element(MainPageLocators.ORDER_ID, "9999")
        order_id = self.get_actually_text(MainPageLocators.ORDER_ID)

        return f"{order_id}"


    @allure.step('Нажать на кнопку Оформить заказ')
    def click_order_button(self):
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BUTTON)


    @allure.step('Нажимаем на заказ в списке Лента заказов')
    def click_order(self):
        self.click_on_element(OrdersPageLocators.ORDER_LINK)

    @allure.step('Проверка отображения состава')
    def check_order_structure(self):
        return self.check_presense(OrdersPageLocators.ORDER_STRUCTURE).is_displayed()



    @allure.step("Проверка нахождение идентификатора заказа в истории")
    def order_id_found_at_history(self):
        self.wait_until_element_visibility(OrdersPageLocators.ALL_ORDERS_AT_HISTORY)
        return self.get_actually_text(OrdersPageLocators.ALL_ORDERS_AT_HISTORY)

    @allure.step("Проверка нахождение идентификатора заказа в ленте")
    def order_id_found_at_feed(self):
        self.wait_until_element_visibility(OrdersPageLocators.ALL_ORDERS_AT_FEED)
        return self.get_actually_text(OrdersPageLocators.ALL_ORDERS_AT_FEED)

    @allure.step("Получение количества заказов")
    def get_total_order_count_daily(self, locator):
        return self.get_actually_text(locator)

    @allure.step('Получаем номер заказа')
    def get_user_order(self, orders_numbers):
        order_refactor = f'0{orders_numbers}'
        self.wait_for_text_to_be_present_in_element(OrdersPageLocators.NUMBER_IN_PROGRESS, order_refactor)
        return order_refactor

    @allure.step('Получаем номер заказа в работе')
    def get_user_order_in_progress(self):
        return self.get_actually_text(OrdersPageLocators.NUMBER_IN_PROGRESS)
