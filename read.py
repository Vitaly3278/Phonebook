# Чтение из файла базы
def read():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        line = file.readlines()
    return line
