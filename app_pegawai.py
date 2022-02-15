from os import environ
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint
from time import sleep
import operator
from transform_data_pegawai import rows
from datetime import datetime

load_dotenv()

short_waiting_time  = 0.5
medium_waiting_time = 0.7
long_waiting_time   = 1.5

# Read data source
pegawai_list = rows


# For captcha purpose
operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


# Getting credentials
browser             = webdriver.Chrome("./chromedriver/stable/chromedriver")
emispendis_url      = environ.get('emispendis_url')
emispendis_username = environ.get('emispendis_username')
emispendis_password = environ.get('emispendis_password')


# Begin browsing
browser.get(emispendis_url)
browser.set_window_size(1920, 1080)
browser.maximize_window()


# Fill login form
browser.find_element(By.NAME, "username").send_keys(emispendis_username)
browser.find_element(By.NAME, "password").send_keys(emispendis_password)

captcha_problem  = browser.find_element(By.TAG_NAME, "h6").text
captcha_arr      = captcha_problem.split(" ")
number_1         = int(captcha_arr[0])
number_2         = int(captcha_arr[2])
operator         = operators[captcha_arr[1]]
captcha_solution = operator(number_1, number_2)

browser.find_element(By.NAME, "captcha").send_keys(captcha_solution)
browser.find_element(By.TAG_NAME, "button").click()

# Begin fill the form pegawai with data from source

# Open form
browser.implicitly_wait(10)
browser.find_element(By.XPATH, "//span[contains(text(),'Ustad/Ustadzah')]").click()

browser.implicitly_wait(10)
browser.find_element(By.XPATH, "//a[@class='nav-link'][contains(text(), 'Daftar Ustad/Ustadzah')]").click()

browser.implicitly_wait(10)
browser.find_element(By.XPATH, "//i[@class='fas fa-plus']").click()
browser.implicitly_wait(10)
