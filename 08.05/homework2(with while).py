a = int(input('Введите число '))
b = int(input('И еще одно число '))
c = int(input('И последнее '))
while a != 0 and b != 0 and c != 0:
    print('Нет нулевых значений')
    break
while a == 0 and b == 0 and c == 0:
    print('Введены все нули')
    break
while c != 0:
    n = c
    break
while b != 0:
    n = b
    break
while a != 0:
    n = a
    break
while a != 0 or b != 0 or c != 0:
    print(n)
    break
while a > (b + c):
    print(a - b - c)
    break
while a < (b+c):
    print(b + c - a)
    break
while a > 50 and (b > a or c > a):
    print('Вася')
    break
while a > 5 or (b == 7 and c == 7):
    print('Петя')
    break