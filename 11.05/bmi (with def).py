def bmi(height,weight):
    i = weight/height**2
    print('Ваш индекс массы тела - ',round(i))
    print('15' + '='*(round(i)-15) + '|' + '='*(40-round(i)) + '40')
    if i<=16:
        print('У вас выраженный дефицит маасы тела')
    elif i>16 and i<=18.5:
        print('У вас недостаточная масса тела')
    elif i>18.5 and i<=25:
        print('Ваша масса тела в норме')
    elif i>25 and i<=30:
        print('У вас избыточная масса тела (предожирение)')
    elif i>30 and i<=35:
        print('У вас ожирение')
    elif i>35 and i<=40:
        print('У вас резкое ожирение')
    elif i>40:
        print('У вас очень резкое ожирение')
    else:
        print('Проверьте верность введенных данных')

def draw_menu():
    menu = str(input('Меню: \n 1 - Добавить пользователя \n 2 - Просмотреть данные пользователей \n q - Выход из программы '))
    return menu

def data_name():
    name = str(input('Введите ваше ФИО '))
    return name

def data_height():
    height = float(input('Введите ваш рост (м) '))
    return height

def data_weight():
    weight = int(input('Введите ваш вес (кг) '))
    return weight

def data_sex():
    sex = str(input('Выберите ваш пол (М/Ж) '))
    return sex

def data_age():
    age = int(input('Введите ваш возраст '))
    return age

def data_persinfo():
    persinfo = {name:{'Рост':height, 'Вес':weight, 'Пол':sex, 'Возраст':age}}
    print(persinfo)
    return persinfo




allinfo = []
while True:
    menu1 = draw_menu()
    if menu1 == '1':
        name = data_name()
        height = data_height()
        weight = data_weight()
        sex = data_sex()
        age = data_age()
        persinfo = data_persinfo()
        bmi(height,weight)
        allinfo.append(persinfo)
    elif menu1 == '2':
        print(allinfo)
    elif menu1 == 'q':
        break
