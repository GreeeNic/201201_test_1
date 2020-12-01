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
elif gh == 'float':
    print('Это замечательно!')
elif gh == 'str':
    print('Это хорошо!')
elif gh == 'bool':
    print('Это интересно!')
else:
    print('Error! 404')
    print('Boot problem А671Е54')
print(gh, dir(gh))
print('Это все Шутка!')
print('Это все Шутка!'.upper())
print('Это все Шутка!'.lower())
