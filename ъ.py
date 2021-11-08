import pyautogui as pg
import time as t
k=int(input('Введите число:'))
for step in range(1, k+1):
    pg.hotkey('win', 'r')
    pg.write('notepad')
    pg.press('enter')
    t.sleep(1)
    pg.hotkey('ctrl', 's')
    t.sleep(2)
    pg.click(322, 432)
    pg.write(str(step))
    pg.press('enter')
