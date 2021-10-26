import random as r
chislo=int(input('угадайте загаданное число от 0 до 10'))
chislo1=r.randint(0,10)
while (chislo==chislo1):
    print('попробуй ещё раз')
    chislo=int(input())
print('угадал')
