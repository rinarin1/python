import random
def proverka(per1, per2):
    if per1==per2:
        return True
    else:
        return False
zivra1=random.randint(0,9)
zivra2=random.randint(0,9)
while zivra1==zivra2:
    zivra2=random.randint(0,9)
zivra3=random.randint(0,9)
while zivra1==zivra3 or zivra2==zivra3:
    zivra3=random.randint(0,9)
chislo=str(zivra1)+str(zivra2)+str(zivra3)
zivra4=input('Введите первую цифру:')
zivra5=input('Введите вторую цифру:')
zivra6=input('Введите третью цифру:')
chislo1=zivra4+zivra5+zivra6
if proverka(chislo, chislo1)==True:
    print('+')
else:
    print('-')
