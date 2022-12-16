# Добавление абонента

def add():
    print('*' * 20 + '  Добавление абонента  ' + '*' * 20)
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    description = input('Описание (если нет, поставьте "-"): ')
    data = last_name.title(), first_name.title(), phone, description.title()
    return (last_name.title(), first_name.title(), phone, description.title())
