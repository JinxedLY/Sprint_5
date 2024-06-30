from selenium.webdriver.common.by import By


class MainLocator:
    dash_button = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Личный Кабинет
    login_button = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # Кнопка входа в акк
    sauce_tab = (By.XPATH, ".//span[contains(text(),'Соусы')]")  # Таба с соусами
    fillings_tab = (By.XPATH, ".//span[contains(text(),'Начинки')]")  # Таба с начинками
    buns_tab = (By.XPATH, ".//span[contains(text(),'Булки')]")  # Таба с булками
    post_order = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка оформления заказа
    active_tab = (By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc")  # Активная таба имеет такой класс


class LoginLocator:
    email_field = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email
    pass_field = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода password
    login_button = (By.XPATH, ".//button[text() = 'Войти']")  # Кнопка входа
    reg_redirect = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # Кнопка редира на регу
    recovery_redirect = (By.XPATH, ".//button[text() = 'Восстановить пароль']")  # Кнопка редира на рековер


class RegLocator:
    name_field = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")  # Поле ввода имени
    email_field = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # Поле ввода email
    pass_field = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")  # Поле ввода пароля
    reg_button = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # Кнопка реги
    login_redirect = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка редира на лог
    pass_error = (By.XPATH, ".//p[text() = 'Некорректный пароль']")  # Вывод ошибки на невалидный пасс


class RecoveryLocator:
    email_field = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email
    recovery_button = (By.XPATH, ".//button[text() = 'Восстановить']")  # Кнопка рековера
    login_redirect = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка редира на лог


class DashLocator:
    constructor_button = (By.XPATH, ".//button[text() = 'Конструктор']")  # Кнопка конструктора
    logo_button = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Лого
    logout_button = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка выхода
