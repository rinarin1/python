a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))

    
def ryd1(a, b):
    if a == b:
        return a
    else:
        print(a)
        return ryd1(a +1, b)

def ryd2(a, b):
    if a == b:
        return a
    else:
        print(a)
        return ryd2(a -1, b)

if a < b:
    print(ryd1(a, b))
else:
    print(ryd2(a, b))