gh = 5
print(gh, type(gh))
gh = '5'
print(gh, type(gh))
gh = 5.0
print(gh, type(gh))
gh = True
print(gh, type(gh))
gh = input('Что больше нравится?')
if gh == 'int':
    print('Это круто!')
if gh == 'Int':
    print('Это круто!')
elif gh == 'float':
    print('Это замечательно!')
elif gh == 'Float':
    print('Это замечательно!')
elif gh == 'str':
    print('Это хорошо!')
elif gh == 'Str':
    print('Это хорошо!')
elif gh == 'bool':
    print('Это интересно!')
elif gh == 'Bool':
    print('Это интересно!')
else:
    print('Error! 404')
    print('Boot problem А671Е54')
print(gh, dir(gh))
print('ЭтО ВсЕ ШуТкА!')
print('Это все Шутка!'.upper())
print('Это все Шутка!'.lower())

pupil_1 = 'Коля'
pupil_2 = 'Соня'
pupil_3 = 'Миша'
print('Группа 28:', pupil_1, pupil_2, pupil_3)
bor = ['Коля', 'Соня', 'Миша']
print('Группа 28:', bor)
print(type(bor), dir(bor))
