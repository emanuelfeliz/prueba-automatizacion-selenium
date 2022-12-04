from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
import time

def test_ebay():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.ebay.com/')
    time.sleep(3)


    searchBox = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
    searchBox.send_keys('Microphone')
    time.sleep(3)
    searchBox.send_keys(Keys.ENTER)



    time.sleep(10)

    driver.save_screenshot('./screenshots/image1.png')