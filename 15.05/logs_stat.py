with open(r'D:\homework_py\15.05\logs.txt', 'r') as fp:
    print('Общее количество строк -',len(fp.readlines()))
ip = []
with open(r'D:\homework_py\15.05\logs.txt', 'r') as fp:
    for line in fp:
        lines = (str(line)).split()
        ip.append(lines[0])
print('Количество уникальных ip адресов -',len(set(ip)))
browsers = []
with open(r'D:\homework_py\15.05\logs.txt', 'r') as fp:
    for line in fp:
        x = ((str(line)).split())
        browsers.append(x[-1])
firefox_counter = 0
safari_counter = 0
for browser_name in browsers:
    if 'Safari' in str(browser_name):
        safari_counter += 1
    elif 'Firefox' in str(browser_name):
        firefox_counter += 1
print('Входов с браузера Safari -',safari_counter)
print('Входов с браузера Firefox -',firefox_counter)
with open(r'D:\homework_py\15.05\unique_ip.txt', 'w') as fp:
    fp.write(str(set(ip)))
print('Все уникальные ip адреса записаны в файл unique_ip.txt')
