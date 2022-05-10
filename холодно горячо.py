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
def gen():
    z1=random.randint(0,9)
    z2=random.randint(0,9)
    while z1==z2:
        z2=random.randint(0,9)
    z3=random.randint(0,9)
    while z1==z3 or z2==z3:
        z3=random.randint(0,9)
    return str(z1)+str(z2)+str(z3)
chislo=gen()
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