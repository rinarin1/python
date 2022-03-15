import keyboard as kb
import time
import random as r
pole=[['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', 'O', '*', '*', '*', '*', '*']]
ox1 = 0
oy1 = 0
ox2=-2
oy2=-2
ox=5
oy=10
schet=0
def proverka(coord_x):
    if int(coord_x) < 0:
        return 0
    elif int(coord_x) > 10:
        return 10
    else:
        return coord_x
def right():
    global ox,oy
    pole[oy][ox]='*'
    ox=ox+1
    ox = proverka(ox)
    pole[oy][ox]='O'
def left():
    global ox,oy
    pole[oy][ox]='*'
    ox=ox-1
    ox = proverka(ox)
    pole[oy][ox]='O'
def bonuS():
    global ox1, oy1, s, t1, oy, ox 
    if oy1==10:
        pole[oy1][ox1]='*'
        s=2
        t1=r.randint(2, 10)
        if oy1-1==oy and ox1==ox:
            pole[oy][ox]='O'
        oy1=-1
    else:
        pole[oy1][ox1]='*'
        pole[oy1+1][ox1]='¥'
        oy1=oy1+1
def bonus():
    global ox1, oy1, s
    ox1=r.randint(0, 10)
    oy1=0
    pole[oy1][ox1]='¥'
    s=3
def bomba():
    global ox2, oy2, s1
    ox2=r.randint(0, 10)
    oy2=0
    pole[oy2][ox2]='💣'
    s1=3
def bomBa():
    global ox2, oy2, s1, t2, oy, ox  
    if oy2==10:
        pole[oy2][ox2]='*'
        s1=2
        t2=r.randint(2, 10)
        oy2=-1
    else:
        pole[oy2][ox2]='*'
        pole[oy2+1][ox2]='💣'
        oy2=oy2+1
    if oy2==oy and ox2==ox:
        pole[oy][ox]='O'
def timer():
    global t1, t2, s, s1
    if t1==0:
        s=1
    if t2==0:
        s1=1
kb.add_hotkey('right', right)
kb.add_hotkey('left', left)
s=0
s1=0
t1=r.randint(2, 10)
t2=r.randint(2, 10)
t1=t1+1
t2=t2+1
while True:
    print()
    for i in range(0, 11):
        for kletka in pole[i]:
            print(kletka,end='')
        if i == 5:
            print("       Score:", schet)
            continue
        print()
    time.sleep(1.5)
    timer()
    t1=t1-1
    t2=t2-1
    if s==1:
        bonus()
    elif s==3:
        bonuS()
    if ox1==ox and oy1==oy:
        pole[oy][ox]='О'
        schet=schet+1
        ox1=0
    if ox2==ox and oy2==oy:
        pole[oy][ox]='О'
        schet=schet-1
        ox2=0
    if s1==1:
        bomba()
    elif s1==3:
        bomBa()
    if ox2==ox1 and oy2==oy1:
        pole[oy1][ox1]='¥'
        ox2=r.randint(0, 10)
        pole[oy2][ox2]='💣'
