def zaglavnie(stroka):
    result=False
    for symbol in stroka:
        if symbol>='A' and symbol<='Z':
            result=True
    return result
def malenkie(stroka):
    result=False
    for symbol in stroka:
        if symbol>='a' and symbol<='z':
            result=True
    return result
def spetzsymbol(stroka):
    result=False
    for symbol in stroka:
        if symbol in ['-','*','/','+','!','&','?','#',',', '`','<','>','.','=','"',"'",'@','%','$','№',':',';','^','(',')']:
            result=True
    return result
parol=input('Введите пароль:')
result1=zaglavnie(parol)
result2=malenkie(parol)
result3=spetzsymbol(parol)
if result1==True and result2==True and result3==True:
    print('＼(＾▽＾)／')
if result1==False:
    print('Нет заглавных букв')
if result2==False:
    print('Нет строчных букв')
if result3==False:
    print('Нет спецсимволов')