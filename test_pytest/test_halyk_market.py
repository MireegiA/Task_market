from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class test_market:
    def __init__(browser):
        chrome_browser = webdriver.Chrome()

    def open(browser, url):
        browser.get(url)
        #chrome_browser.get('https://halykmarket.kz/')

    def get_page_title(browser):
        return browser.title

    def search_product(browser, product_name):
        search_input = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/header/div[2]/div/div[2]/form/label/input')
        search_input.send_keys(product_name)
        search_input.submit()

    def wait_for_search_results(browser):
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-card-title"))
        )

    def get_search_results(browser):
        return browser.find_elements(By.CLASS_NAME, "product-card-title")

    def click_product(browser, product_name):
        products = browser.get_search_results()
        for product in products:
            if product_name in product.text:
                product.click()
                break

    def get_product_title(browser):
        return browser.find_element(By.CLASS_NAME, "product-card-title").text

    def click_favorite_button(browser):
        favorite_button = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div/div/div/div/div[2]/div[1]/div/button") #"icon-text"
        favorite_button.click()

    def wait_for_favorite_confirmation(browser):
        WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "icon-notify"))
        )

    def go_to_favorite_page(browser):
        favorite_link = browser.find_element(By.CLASS_NAME, "icon-wrap")
        favorite_link.click()

  """def get_favorite_product_title(browser):
        return browser.find_element(By.CLASS_NAME, "product-card-title").text

    def get_product_price(browser):
        return browser.find_element(By.CLASS_NAME, "product-price").text """
