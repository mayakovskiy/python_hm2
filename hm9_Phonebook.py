def start_menu(file):
    while True:
        text = "Уточните Ваши действия!"
        width = 130
        fillchar = "-"
        centered_text = text.center(width, fillchar)
        print(centered_text)

        user_choice = input('1 - Просмотреть все контакты\n2 - Найти контакт\n3 - Добавить контакт\n\
4 - Изменить контакт\n5 - Удалить контакт\n0 - Выйти из приложения\n')
        print()
        if user_choice == '1':
            show_contacts(file)
        elif user_choice == '2':
            find_item(file)
        elif user_choice == '3':
            add_new_contact(file)
        elif user_choice == '4':
            change_contact(file)
        elif user_choice == '5':
            delete_contact(file)
        elif user_choice == '0':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue
       

def show_contacts(file):
    with open(file, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            print(line.strip())

def find_item(file):
    item = input('Что ищем: ')
    item_type = int(input('Введите номер (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    with open(file, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            line = line.split(', ')
            if item.lower() in line[item_type].lower():
                print(*line)

def add_new_contact(file):
    str_new1 = input('Фамилия: ')
    str_new2 = input('Имя: ')
    str_new3 = input('Отчество: ')
    str_new4 = input('Телефон: ')
    str_new = '\n' + str_new1 + ', ' + str_new2+ ', ' + str_new3+ ', ' + str_new4
    with open(file, 'a', encoding='utf8') as txt_file:
        txt_file.write(str_new)

def change_contact(file):
    query = ((input('Для изменения контакта введите его фамилию: ')))
    objects = []
    with open(file, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            if query.lower() in line.lower():
                line = line.split(", ")
                objects.append(line)
                print('Какое поле вы хотите изменить?')
                field = input('1 - Фамилия\n2 - Имя\n3 - Отчетво\n4 - Номер телефона\n')
                if field == '1':
                    objects[0][0] = input('Введите фамилию: ')
                elif field == '2':
                    objects[0][1] = input('Введите имя: ')
                elif field == '3':
                    objects[0][2] = input('Введите отчество: ')   
                elif field == '4':
                    objects[0][3] = input('Введите номер телефона: ')
    contact_to_change = []
    with open(file, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            if query.lower() in line.lower():
                line = line.split(", ")
                contact_to_change.append(line)
    lst = []
    with open(file, 'r+', encoding='utf8') as txt_file:
        for line in txt_file:
            line = line.split(", ")
            lst.append(line)
        
        print("Подтвердите замену: ")
        user_choice = input("1 - Да\n2 - Нет\n")
        print()
        if user_choice == '1':
            for i, sublist in enumerate(lst):
                if sublist == contact_to_change[0]:
                    lst[i] = objects[0]
            print ("Изменения сохранены")
        elif user_choice == '2':
            print("Изменения не сохранены")
           
    with open(file, 'w', encoding='utf8') as txt_file:
        for item in lst:
            line = ', '.join(item)
            txt_file.write(line.strip() + '\n') 

def delete_contact(file):
    query = ((input('Для удаления контакта введите его фамилию: ')))
    objects = []
    with open(file, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            if query.lower() in line.lower():
                line = line.split(", ")
                objects.append(line)
                print(*objects)
    
    lst = []
    with open(file, 'r+', encoding='utf8') as txt_file:
        for line in txt_file:
            line = line.split(", ")
            lst.append(line)
            
        print("Вы действительно хотите удалить контакт: ")
        user_choice = input("1 - Да\n2 - Нет\n")
        print()
        if user_choice == '1':
            for sublist in lst:
                if sublist == objects[0]:
                    lst.remove(sublist)
            print ("Контакт удален")
        elif user_choice == '2':
                print("Изменения не сохранены")
            
    with open(file, 'w', encoding='utf8') as txt_file:
        for item in lst:
            line = ', '.join(item)
            txt_file.write(line.strip() + '\n')


if __name__ == '__main__':
    file = 'data.txt'
    start_menu(file)