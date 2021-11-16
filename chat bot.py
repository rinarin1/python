import pyautogui as pg
import time
z=input('запрос:').lower()
if z == 'браузер':
    v=int(input('кол-во вкладок:'))
    pg.hotkey ('ctrl', 'alt', 'm')
    for step in range (1, v):
        pg.hotkey('ctrl', 't')
if z == 'блокнот':
    pg.hotkey('win' , 'r')
    pg.write ('notepad')
    pg.press ('enter')
if z == 'калькулятор':
    d=input('операция:')
    while d!='+' and d!='-' and d!='*' and d!='/':
        d=input('действие:')
    if d == '+':
        slagaemoe1=float(input('Введите первое слагаемое:'))
        slagaemoe2=float(input('Введите второе слагаемое:'))
        summa=slagaemoe1+slagaemoe2
        print(summa)
    if d == '-':
        umenshaemoe=float(input('Введите уменьшаемое:'))
        vichitaemoe=float(input('Введите вычитаемое:'))
        raznost=umenshaemoe-vichitaemoe
        print(raznost)
    if d =='*':
        mnozitel1=float(input('Введите первый множитель:'))
        mnozitel2=float(input('Введите второй множитель:'))
        proizvedenie=mnozitel1*mnozitel2
        print(proizvedenie)
    if d =='/':
        delimoe=float(input('Введите делимое:'))
        delitel=float(input('Введите делитель:'))
        raznost=delimoe/delitel
        print(raznost)
if z == 'выход':
    pg.hotkey('alt', 'f4')