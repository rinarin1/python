import pyautogui as pg
import time
pg.hotkey('win' , 'r')
pg.write ('notepad')
pg.press ('enter')
time.sleep (3)
pg.write ('Zubnoj v 8:00')
pg.hotkey ('ctrl' , 's')
time.sleep (3)
pg.click (710, 582)
pg.write ('notepad')
time.sleep (1)
pg.press ('enter')
