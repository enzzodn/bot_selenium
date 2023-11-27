from selenium import webdriver 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as p

def remove():
    driver = webdriver.Chrome()
    driver.get('https://www.remove.bg/pt-br')
    driver.maximize_window()
    time.sleep(2)

    # ----------- fechar -------------

    WebDriverWait(driver, 10)(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[5]/div/div[1]/div/div/div/div/div/button'))
    )
    fechar = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[1]/div/div/div/div/div/button')
    fechar.click()
    time.sleep(1)

    # ----------------- upload ---------------
    WebDriverWait(driver, 10)(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div[1]/div/div/div/div[2]/div[2]/button'))
    )
    botao = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[1]/div/div/div/div[2]/div[2]/button')
    botao.click()
    time.sleep(1)
    
    nome = 'C:\\Users\\enzzo.nogueira\\Desktop\\bot_selenium\\nome.png'
    p.locateCenterOnScreen(nome)
    while nome != True:
        p.locateCenterOnScreen(nome)
        time.sleep(1)
    p.click()
    p.typewrite("C:/Users/enzzo.nogueira/Desktop/python_logo.png", 0.15)
    p.typewrite('\n')

    # --------- download --------------
    WebDriverWait(driver, 10)(
        EC.presence_of_element_located(By.XPATH, '/html/body/div[1]/main/div/div/div/div/div[2]/div[2]/div[2]/button')
    )
    download = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/div/div[2]/div[2]/div[2]/button')
    download.click()

    # -------------- salvar -----------
    salvar = 'C:\\Users\\enzzo.nogueira\\Desktop\\bot_selenium\\salvar.png'
    p.locateCenterOnScreen(salvar)
    while salvar != True:
        p.locateCenterOnScreen(salvar)
        time.sleep(1)
    p.click(salvar)
    # python_logo-removebg-preview.png => nome do arquivo salvo