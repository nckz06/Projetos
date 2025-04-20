# Escrever PASSO A PASSO para resolver o "problema"
# Link do site: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Código da aula 1: python2024

import pyautogui
# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# atalho -> pyautogui.hotkey
# rolar -> pyautogui.scroll 
    # positivo -> cima  negativo -> baixo
import time

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "pythonimpressionador@gmail.com"
senha = "minha senha"
produtos = "C:/Users/User/Documents/Nicolas/PROJETOS/Hashtag/produtos.csv"

# PASSO 1 - Entrar no sistema da empresa
pyautogui.PAUSE = 1

pyautogui.hotkey("win", "r")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=1052, y=497)
pyautogui.hotkey("ctrl", "t")
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

# PASSO 2 - Fazer login
pyautogui.click(x=1006, y=469)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# PASSO 3 - Importar base de dados
import pandas

tabela = pandas.read_csv(produtos)

# PASSO 4 - Cadastro de todos os produtos da base de dados
for linha in tabela.index:

    codigo = str(tabela.loc[linha, "codigo"])        
    marca = str(tabela.loc[linha, "marca"])
    tipo = str(tabela.loc[linha, "tipo"])
    categoria = str(tabela.loc[linha, "categoria"])
    preco = str(tabela.loc[linha, "preco_unitario"])
    custo = str(tabela.loc[linha, "custo"])
    obs = tabela.loc[linha, "obs"]
    
    pyautogui.click(x=824, y=327)
    
    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    pyautogui.write(categoria)
    pyautogui.press("tab")
    
    pyautogui.write(preco)
    pyautogui.press("tab")
    
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    if not pandas.isna(obs):
        pyautogui.write(obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)