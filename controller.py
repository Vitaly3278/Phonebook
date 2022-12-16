from console import console
from add import add
from read import read

run = console()
if run == 1:
    data = add()
    last_name, first_name, phone, description = data
    print ('*'*20 + '  Данные заполнены  ' + '*'*20)
    print (f'Фамилия: {last_name}')
    print(f'Имя: {first_name}')
    print(f'Номер телефона: {phone}')
    print(f'Описание: {description}')
    print('*' * 20 + '  Данные успешно добавлены  ' + '*' * 20)
    console()
if run == 2:
    data = read()
if run == 3:
    data = read()
    print('*' * 20 + '  Данные для выгрузки в файл  ' + '*' * 20)
    for line in data:
        print(line.strip())

    #last_name, first_name, phone, description = data

