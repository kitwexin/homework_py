a = int(input('Введите число '))
b = int(input('И еще одно число '))
c = int(input('И последнее '))
if a != 0:
    n = a
elif b != 0:
    n = b
elif c != 0:
    n = c
if a != 0 and b != 0 and c != 0:
    print('Нет нулевых значений')
if a == 0 and b == 0 and c == 0:
    print('Введены все нули!')
elif a != 0 or b != 0 or c != 0:
    print(n)
if a > (b + c):
    print(a - b - c)
elif a < (b+c):
    print(b + c - a)
if a > 50 and (b > a or c > a):
    print('Вася')
if a > 5 or (b == 7 and c == 7):
    print('Петя')