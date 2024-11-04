import pyautogui as gui
import time
gui.PAUSE=1
gui.press("win")
gui.write("bloco de notas")
gui.press("enter")
time.sleep(2)
gui.write("testando, testando testando testando!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
gui.hotkey('alt','f4')
gui.press('tab')
gui.press('enter')

#fazer o pip install pyinstaller e escrever no terminal: pyinstaller --onfile nome do arquivo