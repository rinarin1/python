import random
def pobeda(str1,str2):
    if str1==str2:
        return True
    else:
        return False
def teplo(ch1, ch2):
    result=False
    for zivra in ch1:
        for ziVra in ch2:
            if zivra==ziVra:
             result=True
    return result
def goryacho(ch1, ch2):
    result=False
    p=0
    for step in range(3):
        if ch1[p]==ch2[p]:
            result=True
        else:
            p=p+1
    return result
zivra1=random.randint(0,9)
zivra2=random.randint(0,9)
while zivra1==zivra2:
    zivra2=random.randint(0,9)
zivra3=random.randint(0,9)
while zivra1==zivra3 or zivra2==zivra3:
    zivra3=random.randint(0,9)
chislo=str(zivra1)+str(zivra2)+str(zivra3)
while True:
    chislo1=input('Введите 3-ёх значное число:')
    if pobeda(chislo,chislo1)==True:
        print('Победа')
        break
    elif goryacho(chislo,chislo1)==True:
        print('Горячо')
    elif teplo(chislo,chislo1)==True:
        print('Тепло')
    else:
        print('Холодно')