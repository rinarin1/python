import random
chislo1=random.randint(0,9)
chislo2=random.randint(0,9)
while chislo1==chislo2:
    chislo2=random.randint(0,9)
chislo3=random.randint(0,9)
while chislo1==chislo3 or chislo2==chislo3:
    chislo3=random.randint(0,9)
chisla=chislo1, chislo2, chislo3
chislo4=int(input('Введите первую цифру:'))
chislo5=int(input('Введите вторую цифру:'))
chislo6=int(input('Введите третью цифру:'))
chisla1=chislo4, chislo5, chislo6
if chisla==chisla1:
    print('!')
else:
    for chislo in chisla:
        print(chislo)