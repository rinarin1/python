import pyautogui as pg
z1=input('Введите операцию:')
while z1!='exit':
    if z1=='+':
        slagaemoe1=float(input('Введите первое слагаемое:'))
        slagaemoe2=float(input('Введите второе слагаемое:'))
        summa=slagaemoe1+slagaemoe2
        print(summa)
    if z1=='-':
        umenshaemoe=float(input('Введите уменьшаемое:'))
        vichitaemoe=float(input('Введите вычитаемое:'))
        raznost=umenshaemoe-vichitaemoe
        print(raznost)
    if z1=='*':
        mnozitel1=float(input('Введите первый множитель:'))
        mnozitel2=float(input('Введите второй множитель:'))
        proizvedenie=mnozitel1*mnozitel2
        print(proizvedenie)
    if z1=='/':
        delimoe=float(input('Введите делимое:'))
        delitel=float(input('Введите делитель:'))
        raznost=delimoe/delitel
        print(raznost)
    if z1=='Непейвода Васисуалий':
        print('Его у нас нет. Ищите в другом месте.')
    z1=input('Введите операцию:')
pg.hotkey('alt','f4')