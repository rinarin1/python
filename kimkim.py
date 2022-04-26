import random
schetchik=0
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
chislo1=input('Введите 3-ёх значное число:')
for zivra in chislo:
    for ziVra in chislo1:
        if proverka(zivra, ziVra)==True:
            schetchik=schetchik+1
print(schetchik)