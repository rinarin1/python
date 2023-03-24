d = {'ФИО':'Непейвода Васисуалий Акакиевич'}

while True:
    command = input('Введите команду:').lower()
    if command == 'добавить запись' or command == 'изменить запись':
        p = input('Введите предмет:')
        z = input('Введите оценку:')
        d[p] = z
    elif command == 'удалить запись':
        p = input('Введите предмет:')
        d.pop(p)
    elif command == 'выход':
        break
    elif command == 'вывести все об ученике':
        for key in d:
            print(key + ": ", d[key])
