# passo a passo para automação
# entrar no sistema
# logar no sistema
# importar a base de dados
# cadastrar um produto
# repetir esse processo

# Pyautogui.press – Serve para pressionar uma tecla 
# Pyautogui.write – Serve para escrever 
# Pyautogui.click – Serve para clicar (precisa da posição x, y)
# 


import pyautogui
import time

# entrar no sistema
# passo 1

pyautogui.PAUSE = 0.5

# entrar no sistema
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.write(link)
pyautogui.press('enter')

time.sleep(2)

# login
pyautogui.click(x=659, y=359)
pyautogui.write('luizcorporation@gmail.com')
pyautogui.press('tab')
pyautogui.write('gustavob23.')
pyautogui.press('tab')
pyautogui.press('enter')

# cadastrar produto
import pandas

tabela = pandas.read_csv('produtos.csv')
for linha in tabela.index:
    pyautogui.click(655, y=237)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    if not pandas.isna(tabela.loc[linha, 'obs']):
        pyautogui.write(str(tabela.loc[linha, 'obs']))

    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)








