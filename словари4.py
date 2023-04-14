r = {}
r2 = {}
a = 0
while True:
    if a == 'добавить запись':
        r2 = {}
        b = input('имя:')
        c = int(input('рекорд:'))
        r[b] = c
        r2 = dict(r2 = sorted(r.items(), key = lambda x: x[1], reverse=True))

        print(r2)
        a = 0
        
    elif a == 'выход':
        break
    else:
        a = input('команда:').lower()