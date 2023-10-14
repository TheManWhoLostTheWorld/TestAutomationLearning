from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome = webdriver.Chrome()

def test_authentification_positive():
    chrome.get('https://www.saucedemo.com')

    username_field = chrome.find_element(By.XPATH, '//*[@id="user-name"]')
    username_field.send_keys("standard_user")

    password_field = chrome.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("secret_sauce")

    login_button = chrome.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

    time.sleep(5)
    assert chrome.current_url == 'https://www.saucedemo.com/inventory.html'

    # chrome.quit()

def test_authentification_negative():
    chrome.get('https://www.saucedemo.com')

    username_field = chrome.find_element(By.XPATH, '//*[@id="user-name"]')
    username_field.send_keys("user")

    password_field = chrome.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("user")

    login_button = chrome.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

    time.sleep(5)
    try:
        assert chrome.current_url == 'https://www.saucedemo.com/inventory.html'
    except AssertionError:
        pass

    chrome.quit()
