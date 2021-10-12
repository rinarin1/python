import pyautogui as pg
import time
vkladka=input('введите число от 1 до 8')
pg.click(270,750)
time.sleep(2)
pg.hotkey('ctrl', 'n')
pg.hotkey('ctrl', 't')
pg.hotkey('ctrl', 't')
pg.hotkey('ctrl', 't')
pg.hotkey('ctrl', 't')
pg.hotkey('ctrl', 't')
pg.hotkey('ctrl', 't')
pg.hotkey('ctrl', 't')
pg.hotkey('ctrl', vkladka)
