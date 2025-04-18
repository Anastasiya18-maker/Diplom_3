from selenium.webdriver.common.by import By


class MainPageLocators:
    PROFILE_BUTTON = By.XPATH, ".//p[text()='Личный Кабинет']"
    LOGIN_PROFILE_BUTTON = By.XPATH, "button[text()='Войти в аккаунт']"
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]/parent::a'
    MAIN_LIST_TITLE = By.XPATH, "//h1[text()='Соберите бургер']"
    ORDERS_LIST_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'
    BUN_INGREDIENT = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')  # Ингредиент "Флюоресцентная булка R2-D3"
    INGREDIENT_DETAILS_POPUP = (By.XPATH, "//h2[text()='Детали ингредиента']")  # Детали ингредиента
    CROSS_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]")  # закрытие всплывающего окна
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')  # Счетчик
    ORDER_BASKET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (низ)']")
    CREATE_ORDER_BUTTON = ( By.XPATH, "//button[text()='Оформить заказ']")  # кнопка "Оформить заказ"
    ORDER_IDENTIFICATE = (By.XPATH, '//p[text()="идентификатор заказа"]')  # Идентификатор заказа
    ORDER_ID = (By.XPATH, '//*[@id="root"]/div/section/div[1]/div/h2')
    LOADING_CHECK_BOX = (By.XPATH, ".//img[@alt='tick animation']")
    ORDER_STATUS_TEXT = By.XPATH, "//p[text()='Ваш заказ начали готовить']"  # Ваш заказ начали готовить попап
    ORDER_WAITING_TEXT = By.XPATH, "//p[text()='Дождитесь готовности на орбитальной станции']"

    MAIN_ORDER_H1 = By.XPATH, ".//h1[text()='Соберите бургер']"


class AuthLoginLocators:
    # /login
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    LOGIN_BUTTON_ANY_FORMS = (By.XPATH, ".//button[text()='Войти']")
    FORGOT_PASSWORD = (By.XPATH, '//a[contains(@href, "/forgot-password")]')    # ссылка "Восстановить пароль"
    LOGIN_TEXT = (By.XPATH, ".//h2[text()='Вход']")
    LOGIN_TEXT_WITH_HREF = (By.XPATH, "(//button[text()='Войти'])[1]")  # Надпись Войти и ссылка
    LOGIN_BUTTON = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj')]")



class AuthRegistreLocators:
    AR_NAME_FIELD = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")
    AR_EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    AR_PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    AR_REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    AR_ERROR_MESSAGE = (By.XPATH, ".//p[contains(@class, 'input__error')]")
    AR_ERROR_MESSAGE_2 = (
    By.XPATH, ".//div[@class='Auth_login__3hAey']/p[@class='input__error text_type_main-default']")


class AuthForgotPasswordlocators:
    # /forgot-password
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'  # поле ввода почты
    RESET_BUTTON = By.XPATH, '//button[text()="Восстановить"]'  # кнопка "Восстановить"

    # /reset-password
    INPUT_ACTIVE = By.CSS_SELECTOR, '.input.input_status_active'  # поле пароль активно
    SHOW_PASSWORD_BUTTON = By.XPATH, '//div[contains(@class,"icon-action")]'  # кнопка "Показать пароль"
    SAVE_BUTTON = By.XPATH, '//button[text()="Сохранить"]'  # кнопка "Сохранить"


class UserProfileLocators:
    PROFILE_BUTTON = By.XPATH, "//a[text()='Профиль']" # Кнопка "Профиль"
    ORDER_HISTORY_BUTTON = By.XPATH, "//a[text()='История заказов']"  # Кнопка "История заказов"
    ENABLED_ORDER_HISTORY_BUTTON = (By.XPATH, '//ul/li[2]/a[contains(@class, "Account_link_active")]')  # Включенная кнопка "История заказов"
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    LK_INFO_MESSAGE = (By.XPATH, ".//p[contains(text(),'изменить свои персональные данные')]")


class OrdersPageLocators:
    ORDERS_LIST_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]') # Заголовок "Лента заказов"
    ORDER_STRUCTURE = By.XPATH, "//p[text()='Cостав']"  # Состав
    ORDER_LINK = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'  # ссылка на заказ в Ленте заказов
    ALL_ORDERS_AT_HISTORY = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul/li[last()]/a/div[1]/p[1]')
    ALL_ORDERS_AT_FEED = (By.XPATH, '//*[@id="root"]/div/main/div/div/ul/li[1]/a/div[1]/p[1]')

    TOTAL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    NUMBER_IN_PROGRESS_2 = (By.XPATH, "//li[text()='Все текущие заказы готовы!']")  # Номер в разделе "В работе"
    NUMBER_IN_PROGRESS = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[contains(@class, 'text_type_digits-default')])[1]")

class UIWorkerLocators:
     ORDER_HISTORY = By.XPATH, "//a[text()='История заказов']"
     USERNAME_FIELD = (By.ID, 'username')
     PASSWORD_FIELD = (By.ID, 'password')
     LOGIN_BUTTON = (By.ID, 'login-button')
     ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"
     CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]")


