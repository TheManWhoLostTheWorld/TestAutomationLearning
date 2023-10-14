from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

chrome = webdriver.Chrome()
fake = Faker()

def test_order_with_correct_data():
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

    checkout_button = chrome.find_element(By.XPATH, '//*[@data-test="checkout"]')
    checkout_button.click()

    firstname_field = chrome.find_element(By.XPATH, '//*[@data-test="firstName"]')
    firstname_field.send_keys(fake.first_name())

    surname_field = chrome.find_element(By.XPATH, '//*[@data-test="lastName"]')
    surname_field.send_keys(fake.last_name())

    postcode_field = chrome.find_element(By.XPATH, '//*[@data-test="postalCode"]')
    postcode_field.send_keys(fake.postcode())

    continue_button = chrome.find_element(By.XPATH, '//*[@data-test="continue"]')
    continue_button.click()

    finish_button = chrome.find_element(By.XPATH, '//*[@data-test="finish"]')
    finish_button.click()

    if chrome.find_element(By.XPATH, "//h2[text()='Thank you for your order!']"):
        pass
