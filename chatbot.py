import pyautogui as pg, time, math, random, keyboard as kb
z=0
schet=0
chislo=0
c=0
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
def gen():
    z1=random.randint(0,3)
    z2=random.randint(0,3)
    z3=random.randint(0,3)
    return str(z1)+str(z2)+str(z3)
def proverka(ch):
    if ch[0]==ch[1] and ch[0]==ch[2]:
        return True
    else:
        return False
def space():
    if c==1:
        global schet, chislo
        if proverka(chislo)==True:
            schet=schet+1
        else:
            schet=schet-1
def right():
    global c
    c=0
kb.add_hotkey('space',space)
kb.add_hotkey('right', right)
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
    if z=='однорукий бандит':
        c=1
        while schet!=10 and c==1:
            chislo=gen()
            print(chislo)
            print("       Score:", schet)
            time.sleep(1)
    if z == 'выход':
        break
