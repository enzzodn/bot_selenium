from selenium import webdriver 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyautogui as p
import time

def wiki():
    driver = webdriver.Chrome()
    driver.get('https://pt.wikipedia.org/wiki/')
    driver.maximize_window()

    # ----------------- pesquisa ---------------

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div[2]/div/div/div/form/div/div/input"))
    )
    pesquisar = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/form/div/div/input')
    pesquisar.send_keys('python' + Keys.ENTER)

    # ---------------------- inicio ---------------------

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[1]"))
    )
    paragrafo = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[1]')
    texto1 = paragrafo.text
    time.sleep(1)

    # --------------------- historia -------------------------

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[5]"))
    )
    paragrafo = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[5]')
    texto2 = paragrafo.text
    time.sleep(1)

    # -------------- logo do python ----------------------

    imagem = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]/tbody/tr[2]/th/small/span/a/img')
    imagem.screenshot('C:\\Users\\enzzo.nogueira\\Desktop\\python_logo.png')

    return texto1, texto2