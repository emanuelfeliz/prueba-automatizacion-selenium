
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
import time

def test_addCart():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.amazon.com/-/es/John-F-MacArthur/dp/1602559392/ref=sr_1_1?keywords=biblia+de+estudio+macarthur&qid=1670109980&sprefix=biblia+de+estudio+mc%2Caps%2C706&sr=8-1')
    time.sleep(3)


    searchBox = driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']")
    time.sleep(3)
    searchBox.click()


    time.sleep(10)

    driver.save_screenshot('./screenshots/image1.png')