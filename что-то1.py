factorial=1
n=int(input('Введите натуральное число:'))
for step in range(1, n+1):
    factorial=factorial*step
print(factorial)