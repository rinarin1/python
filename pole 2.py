import keyboard as kb
import time
pole=[['О', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
ox=0
oy=0
def obnovlenije():
    global ox,oy
    x=ox
    y=oy
    if ox<0 or ox>9 or oy<0 or oy>9:
        ox=x
        oy=y
        print('Невозможно пройти.')
    pole[oy][ox]='O'
    print('''

''')
    for stroka in pole:
        for kletka in stroka:
            print(kletka,end='')
        print()
def up():
    global ox,oy
    pole[oy][ox]='*'
    oy=oy-1
    obnovlenije()
def down():
    global ox,oy
    pole[oy][ox]='*'
    oy=oy+1
    obnovlenije()
def right():
    global ox,oy
    pole[oy][ox]='*'
    ox=ox+1
    obnovlenije()
def left():
    global ox,oy
    pole[oy][ox]='*'
    ox=ox-1
    obnovlenije()
kb.add_hotkey('up', up)
kb.add_hotkey('down', down)
kb.add_hotkey('right', right)
kb.add_hotkey('left', left)
