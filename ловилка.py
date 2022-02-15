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
      ['*', '*', '*', '*', '*', 'О', '*', '*', '*', '*', '*']]
ox=6
oy=10
def proverka():
    global ox,oy
    x=ox
    y=oy
    if ox<0 or ox>10 or oy<0 or oy>10:
        ox=x
        oy=y
        print('Невозможно пройти.')
    pole[oy][ox]='O'
def right():
    global ox,oy
    pole[oy][ox]='*'
    ox=ox+1
    proverka()
def left():
    global ox,oy
    pole[oy][ox]='*'
    ox=ox-1
    proverka()
def bonuS():
    global ox1, oy1, s
    if s==1:
#        pole[oy1][ox1]='¥'
        pole[oy1][ox1]='*'
        pole[oy1+1][ox1]='¥'
        oy1=oy1+1
    if oy1==10:
        pole[oy1][ox1]='*'
        s=2
def timer():
    global t1, t2
    t1=r.randint(2, 10)
    t2=r.randint(2, 10)
    if t1==0:
        s=1
    if t2==0:
        s1=1
kb.add_hotkey('right', right)
kb.add_hotkey('left', left)
k1=r.randint(0, 10)
ox1=k1
oy1=0
s=0
s1=0
timer()
while True:
    print()
    for stroka in pole:
        for kletka in stroka:
            print(kletka,end='')
        print()
    time.sleep(2)
    t1=t1-1
    t2=t2-1
    if s==2:
        s=0
        oy1=0
