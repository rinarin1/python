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
kb.add_hotkey('right', right)
kb.add_hotkey('left', left)
while True:
    print()
    for stroka in pole:
        for kletka in stroka:
            print(kletka,end='')
        print()
    n1=r.randint(2, 10)
    time.sleep(n1)
    k1=r.randint(0, 11)
    ox1=k1
    oy1=0    
    s=0
    time.sleep(3)
    s=1
    bonuS()


   
def bonuS():
    global ox1, oy1, s
    pole[oy1][ox1]='¥'
    if s==1:
        pole[oy1][ox1]='*'
        pole[oy1+1][ox1]='¥'
        oy1=oy1+1