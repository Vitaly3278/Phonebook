def read():
    #last_name, first_name, phone, description = data
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        line = file.readlines()
    return line