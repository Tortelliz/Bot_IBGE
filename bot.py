#Olá, este código tem como finalidade executar os seguintes processos:



# 1 - Acessar o site do IBGE ("https://cidades.ibge.gov.br/")

# 2 - Extrair de cada estado, as seguintes informações: ("Gentílico"|"Capital"|"Governador"|"População Estimada"|"IDH")

# 3 - Gerar um arquivo ".xlsx" destes dados, para serem visualizados atráves do MS Excel

# 4 - Enviar um email automático contendo este arquivo em anexo



# Importando as bibliotecas necessárias para a aplicação
import botcity
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders
import os

# Configurando o chromedriver
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

# Abre o site do IBGE
url = "https://cidades.ibge.gov.br/"
driver.get(url)

# Processo de extração
data = []
for i in range(1, 28):
    # Clica no link para a busca dos estados
    link = driver.find_element_by_xpath(f"//tr[{i}]//a")
    link.click()
    time.sleep(5)
    
    # Declarando as variáveis contendo as informações
    gentilico = driver.find_element_by_xpath("//dt[contains(text(), 'Gentílico')]/following-sibling::dd").text.strip()
    capital = driver.find_element_by_xpath("//dt[contains(text(), 'Capital')]/following-sibling::dd").text.strip()
    governador = driver.find_element_by_xpath("//dt[contains(text(), 'Governador')]/following-sibling::dd").text.strip()
    idh = driver.find_element_by_xpath("//dt[contains(text(), 'IDH')]/following-sibling::dd").text.strip()
    populacao = driver.find_element_by_xpath("//dt[contains(text(), 'População')]/following-sibling::dd").text.strip()
    
    # Listando as variáveis
    data.append({
        "Gentílico": gentilico,
        "Capital": capital,
        "Governador": governador,
        "IDH": idh,
        "População Estimada": populacao
    })
    
    
    driver.execute_script("window.history.go(-1)")

    time.sleep(5)

# Criando um DataFrame com os dados
df = pd.DataFrame(data)

# Salvando o arquivo em "xlsx"
df.to_excel("estados.xlsx", index=False)

# Termina a extração
driver.quit()

# Fim do processo de extração dos dados e criação do arquivo "xlsx"
# Início do processo de envio do email com o arquivo "xlsx" em anexo
# Neste caso, coloquei meus 2 emails pessoais para exemplo

# Define as informações do email
de = "rayan.tortelli@gmail.com" # Remetente
para = "tortelli.rayan@gmail.com" # Destinatário
senha = "***" #Local onde seria inserida minha senha pessoal do e-mail remetente (rayan.tortelli@gmail.com)
assunto = "Informações - IBGE"
corpo = "Segue em anexo o arquivo com as informações extraídas de cada estado, coforme solicitado, diretamente do site do IBGE"

# Anexa o arquivo gerado ao email
arquivo = "estados.xlsx"
if not os.path.isfile(arquivo):
    print(f"Arquivo {arquivo} não encontrado")
    quit()
parte = MIMEBase('application', "octet-stream")
parte.set_payload(open(arquivo, "rb").read())
encoders.encode_base64(parte)
parte.add_header('Content-Disposition', 'attachment', filename=arquivo)

# Montando o email
msg = MIMEMultipart()
msg['From'] = de
msg['To'] = COMMASPACE.join([para])
msg['Subject'] = assunto
msg.attach(MIMEText(corpo))
msg.attach(parte)

# Envia o email
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login(de, senha) # Autenticação
smtp.sendmail(de, para, msg.as_string())
smtp.quit()

print("Email enviado com sucesso!")