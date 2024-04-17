import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_check_logout(browser):
    browser.get(browser.url + "/administration")
    browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("user")  # Поле логина + ввод
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("bitnami")  # Поле пароля + ввод
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()  # Логин
    # Проверка, что поля ввода логина и пароля пропали из dom
    WebDriverWait(browser, 1).until_not(EC.all_of(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input-username")),
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input-password"))
    ))
    # Проверка, что кнопка выхода из админки появилась в dom
    WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#nav-logout")))
    browser.find_element(By.CSS_SELECTOR, "#nav-logout").click()  # Поиск кнопки выхода + выход
    # Проверка, что поля ввода логина и пароля снова появились в dom
    WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#input-username")))
    WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#input-password")))


def test_add_to_cart(browser):
    browser.get(browser.url)
    # Проверка, что корзина пуста
    browser.find_element(By.XPATH, '//*[@class="btn btn-lg btn-inverse btn-block dropdown-toggle"]').click()
    browser.find_element(By.XPATH, '//*[@class="text-center p-4"]')
    browser.find_element(By.XPATH, '//*[@class="btn btn-lg btn-inverse btn-block dropdown-toggle show"]').click()
    # Добавление первого товара в корзину
    add_to_hover_over = browser.find_element(By.XPATH, '//div[@id="content"]/div[2]/div[2]/div/div[2]/form/div/button')
    hover = ActionChains(browser).move_to_element(add_to_hover_over)
    hover.perform()
    add_to_hover_over.click()
    time.sleep(1)
    # Ожидание закрытия алерта
    WebDriverWait(browser, 7).until_not(EC.presence_of_element_located(
             (By.XPATH, '//*[@class="alert alert-success alert-dismissible"]')))
    # Открытие корзины
    cart_to_hover_over = browser.find_element(
        By.XPATH, '//*[@class="btn btn-lg btn-inverse btn-block dropdown-toggle"]')
    hover = ActionChains(browser).move_to_element(cart_to_hover_over)
    hover.perform()
    cart_to_hover_over.click()
    # Поиск элементов, существующих в окне корзины только при наличии добавленного товара
    WebDriverWait(browser, 1).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@class="table table-striped mb-2"]')))
    WebDriverWait(browser, 1).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@class="table table-sm table-bordered mb-2"]')))
    WebDriverWait(browser, 1).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@class="btn btn-danger"]')))


def test_price_on_main_page(browser):
    browser.get(browser.url + "/en-gb?route=common/home")
    p_new1 = browser.find_element(By.CSS_SELECTOR, "span.price-new")  # Получение текущих значений сумм первой позиции
    browser.find_element(By.XPATH, '//*[@class="dropdown-toggle"]').click()
    browser.find_element(By.XPATH, '//*[@href="EUR"]').click()
    p: str = p_new1
    time.sleep(1)
    p_new2 = browser.find_element(By.CSS_SELECTOR, "span.price-new")  # Получение новых значений сумм первой позиции
    assert p != p_new2.text


def test_price_on_catalog_page(browser):
    browser.get(browser.url)
    browser.find_element(By.XPATH, '//*[@class="nav-link dropdown-toggle"]').click()
    browser.find_element(By.XPATH, '//*[@class="see-all"]').click()
    time.sleep(1)
    p_new1 = browser.find_element(By.CSS_SELECTOR, "span.price-new")  # Получение текущих значений сумм первой позиции
    browser.find_element(By.XPATH, '//*[@class="dropdown-toggle"]').click()
    browser.find_element(By.XPATH, '//*[@href="EUR"]').click()
    p: str = p_new1
    time.sleep(1)
    p_new2 = browser.find_element(By.CSS_SELECTOR, "span.price-new")  # Получение новых значений сумм первой позиции
    assert p != p_new2.text
