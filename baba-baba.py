import random
import time
import keyboard as kb
schet=0
chislo=0
def gen():
    z1=random.randint(0,9)
    z2=random.randint(0,9)
    z3=random.randint(0,9)
    return str(z1)+str(z2)+str(z3)

def proverka(ch):
    if ch[0]==ch[1] and ch[0]==ch[2]:
        return True
    else:
        return False
def space():
    chislo=gen()
    if proverka(chislo)==True:
        

kb.add_hotkey('space',space)
while schet!=50:
    print()
    time.sleep(1)
    