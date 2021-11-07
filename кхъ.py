import pyautogui as pg
vkl=int(input('Введите число вкладок:'))
pg.hotkey('ctrl', 'alt', 'm')
for step in range(vkl-1):
    pg.hotkey('ctrl', 'n')