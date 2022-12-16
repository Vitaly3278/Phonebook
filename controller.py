# Обработка введенных данных

from console import console
from add import add
from read import read
import csv


def main():
    run = console()
    if run == 1:
        one()
    if run == 2:
        two()
    if run == 3:
        three()
    else:
        print('Неправильный ввод!!!')
        input('Чтобы продолжить, нажмите Enter')
    main()


def one():
    data = add()
    last_name, first_name, phone, description = data
    print('*' * 20 + '  Данные заполнены  ' + '*' * 20)
    print(f'Фамилия: {last_name}')
    print(f'Имя: {first_name}')
    print(f'Номер телефона: {phone}')
    print(f'Описание: {description}')
    print('*' * 20 + '  Данные успешно добавлены  ' + '*' * 20)
    input('Чтобы продолжить, нажмите Enter')
    main()


def two():
    data = read()
    print('*' * 20 + '  Поиск абонента  ' + '*' * 20)
    search = (input('Введите ключевой текст: ').title())

    for line in data:
        if search in line:
            print(f'Найдена запись:  {line}')
    input('Чтобы продолжить, нажмите Enter')
    main()


def three():
    data = read()
    form = int(input('Выберите формат файла данных (1. txt, 2. csv)'))
    if form == 1:
        print('*' * 20 + '  Данные для выгрузки в файл  ' + '*' * 20)
        for line in data:
            log = line.strip()
            print(log)
            with open('data_out.txt', 'a', encoding='UTF-8') as file:
                file.write(log + '\n')

    if form == 2:
        print('*' * 20 + '  Данные для выгрузки в файл  ' + '*' * 20)
        for line in data:
            log = line.strip()
            print(log)
        with open('data_out.csv', 'w', newline='', encoding='UTF-8') as file:
            writer = csv.writer(file)
            writer.writerows([data])

    print('*' * 20 + '  Выгрузка успешно завершена в файл data_out.txt  ' + '*' * 20)
    input('Чтобы продолжить, нажмите Enter')
    main()
