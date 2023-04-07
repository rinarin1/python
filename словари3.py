a = {}

while True:
    d = input('Выберите действие:').lower()
    if d == 'регистрация':
        login = input('Логин:')
        if login in a:
            print('Данный логин уже существует.')
        else:
            password = input('Пароль:')
            password1 = input('Проверка пароля:')
            if password != password1:
                print('Пароли не совпадают.')
            else:
                a[login] = password
                print('Регистрация прошла успешно.')
    elif d == 'вход':
        login = input('Логин:')
        password = input('Пароль:')
        if a.get(login) == password:
            print('Вход выполнен.')
        else:
            print('Логин или пароль введены не верно.')
    print(a)
    if d == 'выход':
        break
