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
    if command == "пр" and x < len(pole[0]) - 1:
        pole[y][x] = "O"
        x = x + 1
        pole[y][x] = "*"
    elif command == "лв" and x > 0:
        pole[y][x] = "O"
        x = x - 1
        pole[y][x] = "*"
    elif command == "вх" and y > 0 :
        pole[y][x] = "O"
        y = y - 1
        pole[y][x] = "*"
    elif command == "нз" and y < len(pole) - 1:
        pole[y][x] = "O"
        y = y + 1
        pole[y][x] = "*"
    else:
        print("Не понял...")
    for stroka in pole:
        for kvadr in stroka:
            print(kvadr, end = ' ')
        print()
    command = input("Введи команду: ")