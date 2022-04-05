import random
chislo1=random.randint(0,9)
chislo2=random.randint(0,9)
while chislo1==chislo2:
    chislo2=random.randint(0,9)
chislo3=random.randint(0,9)
while chislo1==chislo3 or chislo2==chislo3:
    chislo3=random.randint(0,9)
print(chislo1, chislo2,chislo3)