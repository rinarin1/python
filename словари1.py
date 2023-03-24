pers = {}

while True:
    command = input('Введите команду:').lower()
    if command == 'изменить параметр' or command == 'добавить параметр':
        p = input('Введите параметр:')
        z = input('Введите значение параметра:')
        pers[p] = z
    elif command == 'вывести информацию о персонаже':
        for key in pers:
            print(key + ": ", pers[key])
    elif command == 'выход':
        break