
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
import time

def test_buy_Amazon():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.amazon.com/ASUS-ZenBook-ultradelgado-Ruise-Cancelation-UX325EA-XH74/dp/B09KLX2T92/ref=sr_1_2_sspa?keywords=mcbooks+2022&qid=1670110957&sprefix=mcbo%2Caps%2C564&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzT1RFU01FRjBJTUcwJmVuY3J5cHRlZElkPUEwNTU5MjE5TlA0VjBaRFlTNTBRJmVuY3J5cHRlZEFkSWQ9QTAyNjg0NTlMQlE1RzJGWko4UUsmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl')
    time.sleep(3)


    searchBox = driver.find_element(By.XPATH, "//input[@id='buy-now-button']")
    time.sleep(3)
    searchBox.click()


    time.sleep(10)

    driver.save_screenshot('./screenshots/image1.png')