import pyautogui as gui
import time
import pandas 


gui.PAUSE = 0.5 #temporizar todos os passos
gui.press('win') #aperta a tecla
gui.write("firefox") #escrever
gui.press("enter")
time.sleep(3)
gui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
gui.press("enter")
time.sleep(3)
gui.click(x=560, y=-544) #achar o ponto onde vai clicar

tabela = pandas.read_csv("automacao/produtos.csv")
print(tabela)

for linha in tabela.index:
    pass
    