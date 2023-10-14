from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome = webdriver.Chrome()

def test_click_on_image():
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

    assert chrome.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"

def test_click_on_name():
    chrome.get('https://www.saucedemo.com')

    username_field = chrome.find_element(By.XPATH, '//*[@id="user-name"]')
    username_field.send_keys("standard_user")

    password_field = chrome.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("secret_sauce")

    login_button = chrome.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

    time.sleep(1)

    name_button = chrome.find_element(By.XPATH, '//div[text()="Sauce Labs Backpack"]')
    name_button.click()

    assert chrome.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
