import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


os.environ['PATH'] = r"C:/SeleniumDrivers"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(30)

def load_page(url):
    driver.get(url)
    print('Loaded Web Successfully')

def click_start_verification_btn():
    time.sleep(10)
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[onclick="document.getElementById(\'landing\').submit();"]')
        )
    ).click()
    print('Clicked  Start Verification')

def click_verification_btn():
    time.sleep(10)
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.ID, "verify_button2")
        )
    ).click()
    print('Clicked Verify to Continue')

def click_continue_btn():
    # time.sleep(10)
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(
            (By.ID, "verify_button")
        )
    ).click()
    print('Clicked Continue Button')

def click_goto_download_btn():
    if WebDriverWait(driver, 20).until(
        lambda driver: driver.find_element(
            By.ID, "two_steps_btn").get_attribute('innerHTML').strip().lower() == 'go to download'):
        driver.find_element(By.ID, "two_steps_btn").click()
        print('Clicked Go To Download')

        driver.switch_to.window(driver.window_handles[1])
        print(f"switched to {driver.current_url}")


def click_direct_download_btns():
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[type="button"')
        )
    )
    driver.execute_script('document.getElementById( "drc" ).click()')
    print('Clicked Direct Download')
    time.sleep(30)
    driver.execute_script('document.querySelector(".btn-success").click()')
    print('Clicked Second Direct Download ')

def click_download_btn():
    driver.switch_to.window(driver.window_handles[-1])
    print(f"switched to {driver.current_url}")
    time.sleep(30)
    driver.execute_script('document.querySelector(".btn-success").click()')
    print('Starting download...')

