summa=float(input('Введите любое число больше 0'))
if summa<0:
    print('Говорили же, такие не принимаем')
if summa>1000:
    summa1= summa*0.3
    summa2= summa-summa1
    print(summa2)
if 0<summa<1001:
    print(summa)
