from web_pages.create_order_page import CreateOrderPage
import allure
import pytest
from data.urls import Urls
from web_locators.locators import OrdersPageLocators

from conftest import pages


class TestCreateOrder:
    @pytest.fixture
    def main_page(self):
        main_page = CreateOrderPage(pages)
        yield main_page
        main_page.driver.quit()

    @allure.title('Проверка всплывающего окна с деталями заказа при клике')
    @allure.description('Клик на заказ и проверка появления всплывающего окна с деталями заказа')
    def test_get_order_popup(self, main_page):

        main_page.click_order_button()

        order_number = main_page.get_with_order_id()
        assert order_number == "9999"


    @allure.title('При создании заказ отображается в истории заказов в ЛК профиля и в "Ленте заказов"')
    @allure.description('Создание заказа и проверка в ЛК в Истории заказов и в "Ленте заказов"')
    def test_find_order_in_list(self, main_page):

        main_page.add_filling_to_order()
        main_page.click_order_button()
        main_page.check_show_window_with_order_id()
        order_number = main_page.get_with_order_id()
        main_page.click_close_modal_order()
        main_page.click_on_account()

        assert main_page.check_switch_on_profile() == Urls.url_profile

        main_page.click_order_history_button()
        assert main_page.check_switch_on_order_history() == Urls.url_history

        is_order_id_found_at_history = main_page.order_id_found_at_history()
        assert is_order_id_found_at_history[2:] == order_number
        main_page.click_orders_list_button()
        is_order_id_found_at_feed = main_page.order_id_found_at_feed()
        assert is_order_id_found_at_feed[2:] == order_number
        assert is_order_id_found_at_history and is_order_id_found_at_feed, "Заказы в истории и в ленте не совпадают"

    @allure.title('При создании заказа, увеличевается значение счетчиков заказов "Выполнено за все время"/"Выполнено за сегодня"')
    @allure.description('Сверка счетчика заказов "Выполнено за все время" / "Выполнено за сегодня" до создания заказа и после создания заказа '
                        'Счетчик должен увеличиться')

    @pytest.mark.parametrize('counter', [OrdersPageLocators.TOTAL_ORDER_COUNT,OrdersPageLocators.DAILY_ORDER_COUNT])
    def test_today_orders_counter(self, main_page,counter):


        main_page.click_orders_list_button()
        prev_counter_value = main_page.get_total_order_count_daily(counter)
        main_page.click_constructor_button()
        main_page.add_filling_to_order()
        main_page.click_order_button()
        main_page.click_close_modal_order()
        main_page.click_orders_list_button()
        current_counter_value = main_page.get_total_order_count_daily(counter)
        assert current_counter_value > prev_counter_value, "Заказ не создался, counter не сработал"

    @allure.title('Проверка отображения номера заказа в разделе "В работе')
    @allure.description('Получаем номер нового заказа, и проверяем, что номер заказа появился в разделе "В работе"')
    def test_new_order_appears_in_work_list(self, main_page):

        main_page.add_filling_to_order()
        main_page.click_order_button()
        order_number = main_page.get_with_order_id()
        main_page.click_close_modal_order()
        main_page.click_orders_list_button()
        order_number_refactor = main_page.get_user_order(order_number)
        order_in_progress = main_page.get_user_order_in_progress()
        assert order_number_refactor == order_in_progress
