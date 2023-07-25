import pytest
from selenium import webdriver
from test_halyk_market import test_market


@pytest.fixture
def browser():
 """   driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
    yield driver
    driver.quit() """
    chrome_browser = webdriver.Chrome()
    chrome_browser.maximize_window()
    chrome_browser.implicitly_wait(10)
    return chrome_browser

def test_search_and_favorite(browser):
    # Создаем объект страницы
    page = test_market(browser)

    # Открываем сайт HalykMarket
    page.open("https://www.halykmarket.kz/")

    # Проверяем заголовок страницы
    #assert "Halyk Market - Выгодные покупки в рассрочку" in page.get_page_title()
    assert "Halyk Market" in page.get_page_title()

    # Ищем и выбираем продукт
    product_name = "iPhone 14 Pro 128Gb Deep Purple"
    page.search_product(product_name)
    page.wait_for_search_results()
    page.click_product(product_name)

    # Проверяем, что название продукта на странице продукта совпадает с ожидаемым
    assert page.get_product_title() == product_name

    # Добавляем продукт в избранное
    page.click_favorite_button()
    page.wait_for_favorite_confirmation()

    # Переходим на страницу избранного
    page.go_to_favorite_page()

    # Проверяем, что продукт в избранном совпадает с ожидаемым
    assert page.get_favorite_product_title() == product_name
"""
    # Получаем цену продукта на странице карточки товара
    product_price = page.get_product_price()

    # Переходим на страницу карточки товара
    page.open("https://www.halykmarket.kz/product/12345")  # Замените "12345" на актуальный идентификатор продукта

    # Проверяем, что название товара в избранном совпадает с названием товара на странице карточки товара
    assert page.get_product_title() == product_name

    # Проверяем, что цена товара в поиске, избранном, и карточке товара одинакова
    assert page.get_product_price() == product_price
"""