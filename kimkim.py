import random
schetchik=0
chislo1=random.randint(0,9)
chislo2=random.randint(0,9)
while chislo1==chislo2:
    chislo2=random.randint(0,9)
chislo3=random.randint(0,9)
while chislo1==chislo3 or chislo2==chislo3:
    chislo3=random.randint(0,9)
chislo4=int(input('Введите первую цифру:'))
chislo5=int(input('Введите вторую цифру:'))
chislo6=int(input('Введите третью цифру:'))
if chislo1==chislo4:
    schetchik=schetchik+1
if chislo2==chislo5:
    schetchik=schetchik+1
if chislo3==chislo6:
    schetchik=schetchik+1
