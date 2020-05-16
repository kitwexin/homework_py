def data_counter(fp, date):
    ip = []
    safari = []
    firefox = []
    for line in fp:
        lines = (str(line)).split()
        if date in lines[3]:
            ip.append(lines[0])
            if 'Safari' in str(lines[-1]):
                safari.append(lines[-1])
            elif 'Firefox' in str(lines[-1]):
                firefox.append(lines[-1])
    print(str(date)+': total = '+str(len(ip))+', unique = '+str(len(set(ip)))+', safari = '+str(len(safari))+', firefox = '+str(len(firefox)))


with open(r'D:\homework_py\18.05\logs.txt', 'r') as fp:
    data_counter(fp, '17/May/2015')
with open(r'D:\homework_py\18.05\logs.txt', 'r') as fp:
    data_counter(fp, '18/May/2015')
with open(r'D:\homework_py\18.05\logs.txt', 'r') as fp:
    data_counter(fp, '19/May/2015')
with open(r'D:\homework_py\18.05\logs.txt', 'r') as fp:
    data_counter(fp, '20/May/2015')
