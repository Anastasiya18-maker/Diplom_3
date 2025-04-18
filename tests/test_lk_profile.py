import allure
import pytest
from web_pages.main_page import MainPage
from web_pages.user_profile_page import UserProfilePage
from web_pages.auth_user_page import AuthUserPage
from data.urls import Urls


class TestLKProfile:
    @allure.title('Переход в ЛК по клику на кнопку «Личный кабинет»')
    @allure.description('При нажатии на кнопку ЛК, происходит переход на страницу ЛК профиля ')
    def test_go_to_account_from_header(self, pages):
        main_page = MainPage(pages)
        user_profile_page = UserProfilePage(pages)
        main_page.click_on_account()
        current_url = user_profile_page.check_switch_on_profile()
        assert current_url == Urls.url_profile

    @allure.title('Переход в ЛК в раздел История заказов по кнопке "История заказов"')
    @allure.description('При нажатиии на кнопку "История заказов" в ЛК профиля, происходит переход к истории заказов юзера')
    def test_go_to_order_history(self, pages):
        main_page = MainPage(pages)
        user_profile_page = UserProfilePage(pages)
        main_page.click_on_account()
        user_profile_page.click_order_history_button()
        current_url = user_profile_page.check_switch_on_order_history()
        assert current_url == Urls.url_profile_order_history

    @allure.title('Переход на старницу авторизации при нажатии в ЛК кнопки "Выход"')
    @allure.description('При нажатии в ЛК профиля кнопки "Выход" происходит разлогин пользователя на сайте и редирект на страницу авторизации')
    def test_logout(self, pages):
        main_page = MainPage(pages)
        user_profile_page = UserProfilePage(pages)
        auth_user_page = AuthUserPage(pages)
        main_page.click_on_account()
        user_profile_page.click_log_out_button()
        current_url = auth_user_page.check_switch_on_login_page()
        assert current_url == Urls.url_login
