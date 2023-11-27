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

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[5]/div/div[1]/div/div/div/div/div/button'))
    )
    fechar = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[1]/div/div/div/div/div/button')
    fechar.click()
    time.sleep(1)

    # ----------------- upload ---------------
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div[1]/div/div/div/div[2]/div[2]/button'))
    )
    botao = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[1]/div/div/div/div[2]/div[2]/button')
    botao.click()
    time.sleep(1)
    
    img_nome = 'C:\\Users\\enzzo.nogueira\\Desktop\\bot_selenium\\nome.png'
    nome = p.locateCenterOnScreen(img_nome, confidence=0.9)
    while nome != True:
        nome = p.locateCenterOnScreen(img_nome, confidence=0.9)
        time.sleep(1)
        print('nao')
    p.click()
    p.typewrite("C:\\Users\\enzzo.nogueira\\Desktop\\python_logo.png", 0.15)
    p.typewrite('\n')

    # --------- download --------------
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/div/div/div[2]/div[2]/div[2]/button'))
    )
    download = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/div/div[2]/div[2]/div[2]/button')
    download.click()

    # -------------- salvar -----------
    img_salvar = 'C:\\Users\\enzzo.nogueira\\Desktop\\bot_selenium\\salvar.png'
    salvar = p.locateCenterOnScreen(img_salvar, confidence=0.9)
    while salvar != True:
        salvar = p.locateCenterOnScreen(img_salvar, confidence=0.9)
        time.sleep(1)
    p.click(salvar)
    # python_logo-removebg-preview.png => nome do arquivo salvo