import time
from selenium.webdriver.common.by import By


def test_find_elements_on_main_page(browser):
    browser.get(browser.url)
    browser.find_element(By.XPATH, '//*[title="Your Store"]')  # Логотип
    browser.find_element(By.CSS_SELECTOR, '[name="search"]')  # Поле поиска
    browser.find_element(By.XPATH, '//*[@class="btn btn-lg btn-inverse btn-block dropdown-toggle"]').click()  # Корзина + Нажатие
    browser.find_element(By.XPATH, '//*[@class="text-center p-4"]')  #Your shopping cart is empty!
    browser.find_element(By.CSS_SELECTOR, "#carousel-banner-1")  # Карусель баннеров
    browser.find_element(By.XPATH, '//*[@class ="container"]')  # Футер


def test_find_elements_on_catalog_page(browser):
    browser.get(browser.url)
    browser.find_element(By.XPATH, '//*[@class="nav-link dropdown-toggle"]').click()
    browser.find_element(By.XPATH, '//*[@class="see-all"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[text()="Desktops"]')  # Название раздела
    pr = browser.find_elements(By.XPATH, '//*[@class="product-thumb"]')  # Блоки товаров
    price = browser.find_elements(By.XPATH, '//div[@class="price"]')  # Блок цены в каждом блоке товаров
    assert len(pr) == len(price)  # Сравнение количеств блоков
    browser.find_element(By.XPATH, '//label[@for="input-sort"]')  # Сортировка товаров
    browser.find_element(By.CSS_SELECTOR, "#input-sort")  # Ввод параметра сортировки
    browser.find_element(By.XPATH, '//label[@for="input-limit"]')  # Лимит на странице
    browser.find_element(By.CSS_SELECTOR, "#input-limit")  # Ввод лимита
    browser.find_element(By.XPATH, '//div[@class="col-sm-6 text-end"]')  # Инфо о страницах и количестве товаров


def test_find_elements_on_product_page(browser):
    browser.get(browser.url + "/en-gb/product/desktops/canon-eos-5d")  # Переход в карточку
    browser.find_element(By.XPATH, '//*[text()="Canon EOS 5D"]')  # Название товара
    browser.find_element(By.XPATH, '//*[@class="list-unstyled"]')  # Характеристики
    browser.find_element(By.XPATH, '//*[@class="price-old"]')  # Цена без скидок
    browser.find_element(By.XPATH, '//*[@class="price-new"]')  # Актуальная цена
    browser.find_element(By.XPATH, '//*[@class="fa-solid fa-heart"]')  #Лайк
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")  # Кнопка Add to Card
    browser.find_element(By.XPATH, '//*[text()="Description"]')  # Description
    browser.find_element(By.XPATH, '//*[text()="Reviews (0)"]')  # Reviews


def test_find_elements_on_login_page(browser):
    browser.get(browser.url + "/administration")
    browser.find_element(By.XPATH, '//*[text()=" Please enter your login details."]')  # Заголовок
    browser.find_element(By.CSS_SELECTOR, "#input-username")  # Поле ввода логина
    browser.find_element(By.CSS_SELECTOR, "#input-password")  # Поле ввода пароля
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")  # Кнопка Login
    browser.find_element(By.XPATH, '//*[text()=" © 2009-2024 All Rights Reserved."]')  # Футер


def test_find_elements_on_registration_page(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    browser.find_element(By.XPATH, '//*[text()="Register Account"]')  # Заголовок
    browser.find_element(By.CSS_SELECTOR, "#input-firstname")  # firstname
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')  # lastname
    browser.find_element(By.CSS_SELECTOR, "#input-email")  # email
    browser.find_element(By.CSS_SELECTOR, '[name="password"]')  # password
    browser.find_element(By.CSS_SELECTOR, '[name="newsletter"]')  # checkbox newsletter
    browser.find_element(By.CSS_SELECTOR, '[name="agree"]')  # checkbox agree
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")  # Кнопка Continue