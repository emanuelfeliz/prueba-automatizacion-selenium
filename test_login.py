
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
import time

def test_addCart():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://control.pedidoslosfrailes.com/')
    time.sleep(2)

    correo = driver.find_element(By.XPATH,"//input[@type='email']").send_keys('terrero0611@gmail.com')
    time.sleep(10)

    boton = driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(10)


