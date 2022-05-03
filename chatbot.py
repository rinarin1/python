import pyautogui as pg
import time
import math
z=0
def brauzer():
    v=int(input('кол-во вкладок:'))
    pg.hotkey ('ctrl', 'alt', 'm')
    time.sleep(5)
    for step in range (1, v):
        pg.hotkey('ctrl', 't')
def notepad():
    pg.hotkey('win' , 'r')
    time.sleep(1)
    pg.hotkey('shift', 'ctrl')
    pg.write ('notepad')
    pg.press ('enter')
def plus():
    slagaemoe1=float(input('Введите первое слагаемое:'))
    slagaemoe2=float(input('Введите второе слагаемое:'))
    summa=slagaemoe1+slagaemoe2
    print(summa)
def minus():
    umenshaemoe=float(input('Введите уменьшаемое:'))
    vichitaemoe=float(input('Введите вычитаемое:'))
    raznost=umenshaemoe-vichitaemoe
    print(raznost)
def zvezdochka():
    mnozitel1=float(input('Введите первый множитель:'))
    mnozitel2=float(input('Введите второй множитель:'))
    proizvedenie=mnozitel1*mnozitel2
    print(proizvedenie)
def delenie():
    delimoe=float(input('Введите делимое:'))
    delitel=float(input('Введите делитель:'))
    raznost=delimoe/delitel
    print(raznost)
def stepen():
    osnovanie=float(input('Введите основание степени:'))
    pokazatel=float(input('Введите показатель степени:'))
    stepen=osnovanie**pokazatel
    print(stepen)
def koren():
    pocazatel=float(input('Введите основание корня:'))
    koren=math.sqrt(pocazatel)
    print(koren)
while z!='выход':
    z=input('запрос:').lower()
    if z == 'браузер':
        brauzer()
    if z == 'блокнот':
        notepad()
    if z == 'калькулятор':
        d=input('операция:')
        if d == '+':
            plus()
        if d == '-':
            minus()
        if d =='*':
            zvezdochka()
        if d =='/':
            delenie()
        if d == '**':
            stepen()
        if d == '^':
            koren()
    if z == 'выход':
        break
