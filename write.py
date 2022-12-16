
def add_data(data):
    last_name, first_name, phone, description = data
    log = f'{last_name} {first_name} {phone} {description}\n'
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(log)
    return 0