allinfo = []
while True:
    menu = str(input('Меню: \n 1 - Добавить пользователя \n 2 - Просмотреть данные пользователей \n q - Выход из программы '))
    if menu == '1':
        name = str(input('Введите ваше ФИО '))
        height = float(input('Введите ваш рост (м) '))
        weight = int(input('Введите ваш вес (кг) '))
        sex = str(input('Выберите ваш пол (М/Ж) '))
        age = int(input('Введите ваш возраст '))
        persinfo = {name:{'Рост':height, 'Вес':weight, 'Пол':sex, 'Возраст':age}}
        print(persinfo)
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
        allinfo.append(persinfo)
    elif menu == '2':
        print(allinfo)
    elif menu == 'q':
        break