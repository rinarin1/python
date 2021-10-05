import pyautogui as pg
import keyboard
surname=input('введите свою фамилию')
name=input('введите своё имя')
pg.alert(text=' Ваша фамилия:' + surname + '\n' + ' Ваша имя:' + name , title='фамилия и имя', button='OK')
