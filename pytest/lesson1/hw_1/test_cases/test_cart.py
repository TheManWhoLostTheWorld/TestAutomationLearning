from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

chrome = webdriver.Chrome()

def test_add_to_cart_from_catalog():
    chrome.get('https://www.saucedemo.com')

    username_field = chrome.find_element(By.XPATH, '//*[@id="user-name"]')
    username_field.send_keys("standard_user")

    password_field = chrome.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("secret_sauce")

    login_button = chrome.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

    time.sleep(1)

    add_button = chrome.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']")
    add_button.click()

    cart_button = chrome.find_element(By.XPATH, "//*[@class='shopping_cart_link']")
    cart_button.click()

    if chrome.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']"):
        pass

    chrome.quit()

def test_remove_item_from_cart_through_cart():
    chrome.get('https://www.saucedemo.com')

    username_field = chrome.find_element(By.XPATH, '//*[@id="user-name"]')
    username_field.send_keys("standard_user")

    password_field = chrome.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("secret_sauce")

    login_button = chrome.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

    time.sleep(1)

    add_button = chrome.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']")
    add_button.click()

    cart_button = chrome.find_element(By.XPATH, "//*[@class='shopping_cart_link']")
    cart_button.click()

    remove_button = chrome.find_element(By.XPATH, "//*[@data-test='remove-sauce-labs-backpack']")
    remove_button.click()

    if chrome.find_element(By.XPATH, "//*[@class='removed_cart_item']"):
        pass

def test_item_to_cart_from_description():
    chrome.get('https://www.saucedemo.com')

    username_field = chrome.find_element(By.XPATH, '//*[@id="user-name"]')
    username_field.send_keys("standard_user")

    password_field = chrome.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("secret_sauce")

    login_button = chrome.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

    time.sleep(1)

    item_image = chrome.find_element(By.XPATH, '//*[@alt="Sauce Labs Backpack"]')
    item_image.click()

    add_button = chrome.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']")
    add_button.click()

    cart_button = chrome.find_element(By.XPATH, "//*[@class='shopping_cart_link']")
    cart_button.click()

    time.sleep(1)

    if chrome.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']"):
        pass

    chrome.quit()

def test_remove_item_from_cart_through_description():
    chrome.get('https://www.saucedemo.com')

    username_field = chrome.find_element(By.XPATH, '//*[@id="user-name"]')
    username_field.send_keys("standard_user")

    password_field = chrome.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("secret_sauce")

    login_button = chrome.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

    add_button = chrome.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']")
    add_button.click()

    cart_button = chrome.find_element(By.XPATH, "//*[@class='shopping_cart_link']")
    cart_button.click()

    item_description = chrome.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
    item_description.click()

    remove_button = chrome.find_element(By.XPATH, "//*[@data-test='remove-sauce-labs-backpack']")
    remove_button.click()

    cart_button1 = chrome.find_element(By.XPATH, "//*[@class='shopping_cart_link']")
    cart_button1.click()

    time.sleep(1)

    try:
        removed_item = chrome.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
    except NoSuchElementException:
        pass







