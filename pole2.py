import pyautogui as pg
import time
z=input('запрос:').lower() 
while z != 'выход':
    if z == 'браузер':
        v=int(input('кол-во вкладок:'))
        pg.press('ctrl')
        pg.hotkey ('ctrl', 'alt', 'm')
        time.sleep(2)
        for step in range (1, v):
            pg.hotkey('ctrl', 't')
        z=input('запрос:').lower()
    if z == 'блокнот':
        pg.hotkey('alt', 'shift')
        pg.hotkey('win' , 'r')
        pg.write ('notepad')
        pg.press ('enter')
        z=input('запрос:').lower()
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
        z=input('запрос:').lower()
    if z == 'список':
        spisok=[]
        print('''Команды:
    добавить
    удалить
    показать элемент по номеру
    показать весь список''')
        k=input('Введите команду:').lower()
        while k!= 'exit':
            if k == 'добавить':
                p=input('Напишите название нового элемента списка:')
                spisok.append(p)
            if k == 'удалить':
                print('''Выберите способ удаления элемента
    1. индекс
    2. по названию''')
                а=input('Выберите способ удаления элемента:')
                if а =='1':
                    ind=int(input('Введите индекс элемента:'))
                    spisok.pop(ind)
                if а == '2':
                    z2=input('Введите название элемента')
                    spisok.remove(z2)
            if k == 'показать элемент по номеру':
                d=int(input('Введите индекс:'))
                print(spisok[d])
            if k == 'показать весь список':
                for prod in spisok:
                    print(prod)
            k=input('Введите команду:').lower()
    z=input('запрос:').lower()
pg.hotkey('alt', 'f4')