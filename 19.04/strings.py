text = 'Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!'
print('Исходная строка -',text)
print('Количество символов в строке -',len(text))
print('Инверсная строка -',text[::-1])
print('Та же строка, с каждым словом с большой буквы -',text.title())
print('Та же строка прописными буквами -',text.lower())
print('Число вхождений "нд" =',text.count('нд'),', число вхождений "ам" =',text.count('ам'),', число вхождений "о" =',text.count('о'))
print('Данная строка заглавными буквами -',text.upper())
print('Данная строка без пробелов -',text.replace(' ',''))
if text.count('нд') > text.count('ор'):
    print(True)