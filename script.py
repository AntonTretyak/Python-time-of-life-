'''print(then.year) 
print(then.month)
print(then.day)'''

import datetime

y = int(input('Введите год рождения: '))
m = int(input('Введите месяц рождения: '))
d = int(input('Введите день рождения: '))

now = datetime.datetime.now()
then = datetime.datetime(y, m, d)

delta = now - then

months = int(delta.days * 0.0329)
weeks = int((delta.days * 0.0329) * 4)
days = delta.days
hours = delta.days * 24
seconds = hours * 60
years = months // 12

print('Ты прожил',years,'лет,')
print('Или',months,'месяцев,')
print('Или',weeks,'недель,')
print('Или',days,'дней,')
print('Или',hours,'часов,')
print('Или',seconds,'секунд.')
