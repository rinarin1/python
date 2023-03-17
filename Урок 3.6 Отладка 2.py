'''
Это программа Эргуария. Он решил сделать бродилку,
в которой звёздочка может путешествовать по полю.
Только почему-то она странно себя ведёт, если
попытаться пройти сквозь стену.

Звёздочка должна просто оставаться на месте,
ходить сквозь стены она не может,
но она то телепортируется вообще в другое место поля,
то выдаёт ошибку. 

'''


pole = [['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', '*', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'], ]

x = 3
y = 4

for stroka in pole:
    for kvadr in stroka:
        print(kvadr, end = ' ')
    print()
command = input("Введи команду: ")
while command != "стоп":
    if command == "пр":
        pole[y][x] = "O"
        x = x + 1
        if x > 6 :
            x = x - 1
        pole[y][x] = "*"
    elif command == "лв":
        pole[y][x] = "O"
        x = x - 1
        if x < 0 :
            x = x + 1
        pole[y][x] = "*"
    elif command == "вх":
        pole[y][x] = "O"
        y = y - 1
        if y <0 :
            y = y + 1
        pole[y][x] = "*"
    elif command == "нз":
        pole[y][x] = "O"
        y = y + 1
        if y > 7 :
            y = y - 1
        pole[y][x] = "*"
    else:
        print("Не понял...")
    for stroka in pole:
        for kvadr in stroka:
            print(kvadr, end = ' ')
        print()
    command = input("Введи команду: ")