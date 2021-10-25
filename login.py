from selenium import webdriver
import time

# O time.sleep(n) espera 'n' segundos para executar o próximo comando

navegador = webdriver.Chrome() # Abre o navegador; requer cuidados - vide README.md
time.sleep(3)

navegador.get("https://nsa.cps.sp.gov.br") # Abre o NSA
time.sleep(2)

navegador.find_element_by_xpath('//*[@id="txtCod"]').send_keys("cod_etec") # Coloca a sua Etec

navegador.find_element_by_xpath('//*[@id="txtlogin"]').send_keys("seu_rm") # Coloca o seu RM

navegador.find_element_by_xpath('//*[@id="txtSenha"]').send_keys("sua_senha") # Coloca a sua senha

navegador.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]').click() # Passa pelo antibot
time.sleep(4)

navegador.find_element_by_xpath('//*[@id="btnEntrar"]').click() # Faz o login