stop = str(input('Введите stop, если хотите остановить калькулятор, любой символ, если хотите продолжить '))
while stop != 'stop':
    name = str(input('Введите ваше ФИО '))
    height = float(input('Введите ваш рост (в метрах) '))
    weight = int(input('Введите ваш вес '))
    age = int(input('Введите ваш возраст '))
    persinfo = {name:{'Рост':height, 'Вес':weight, 'Возраст':age}}
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