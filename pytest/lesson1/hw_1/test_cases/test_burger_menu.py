from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome = webdriver.Chrome()

def test_system_exit():
    chrome.get("https://www.saucedemo.com/")

    username_field = chrome.find_element(By.XPATH, '//*[@id="user-name"]')
    username_field.send_keys("standard_user")

    password_field = chrome.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("secret_sauce")

    login_button = chrome.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

    burger_button = chrome.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']")
    burger_button.click()

    logout_button = chrome.find_element(By.XPATH, "//*[@id='logout_sidebar_link']")
    logout_button.click()

    assert chrome.current_url == 'https://www.saucedemo.com/'

def test_about():
    chrome.get("https://www.saucedemo.com/")

    username_field = chrome.find_element(By.XPATH, '//*[@id="user-name"]')
    username_field.send_keys("standard_user")

    password_field = chrome.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("secret_sauce")

    login_button = chrome.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

    burger_button = chrome.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']")
    burger_button.click()

    about_button = chrome.find_element(By.XPATH, "//*[@id='about_sidebar_link']")
    about_button.click()

    assert chrome.current_url == 'https://saucelabs.com/'

def test_reset_app_state():
    chrome.get("https://www.saucedemo.com/")

    username_field = chrome.find_element(By.XPATH, '//*[@id="user-name"]')
    username_field.send_keys("standard_user")

    password_field = chrome.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("secret_sauce")

    login_button = chrome.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

    item_image = chrome.find_element(By.XPATH, '//*[@alt="Sauce Labs Backpack"]')
    item_image.click()

    add_button = chrome.find_element(By.XPATH, "//*[@data-test='add-to-cart-sauce-labs-backpack']")
    add_button.click()

    burger_button = chrome.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']")
    burger_button.click()

    reset_button = chrome.find_element(By.XPATH, "//*[@id='reset_sidebar_link']")
    reset_button.click()

    cart_button = chrome.find_element(By.XPATH, "//*[@class='shopping_cart_link']")
    cart_button.click()

    try:
        removed_item = chrome.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
    except NoSuchElementException:
        pass

    chrome.quit()
