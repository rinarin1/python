import random
zivra1=random.randint(0,9)
zivra2=random.randint(0,9)
while zivra1==zivra2:
    zivra2=random.randint(0,9)
zivra3=random.randint(0,9)
while zivra1==zivra3 or zivra2==zivra3:
    zivra3=random.randint(0,9)
chislo=str(zivra1)+str(zivra2)+str(zivra3)
print(chislo)
