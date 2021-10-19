login=input('Введите логин:')
parol=input('Введите пароль:')
while(login != 'овца75' or parol != 'Непейвода_Васисуалий_75'):
    if login != 'овца75':
        print('Неверный логин')
        login=input('Введите логин:')
        parol=input('Введите пароль:')
    if parol != 'Непейвода_Васисуалий_75':
        print('Неверный пароль')
        login=input('Введите логин:')
        parol=input('Введите пароль:')
print('Вход выполнен')
