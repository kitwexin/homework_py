import datetime
may17 = datetime.date(2015, 5, 17)
may18 = datetime.date(2015, 5, 18)
may19 = datetime.date(2015, 5, 19)
may20 = datetime.date(2015, 5, 20)





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
    data_counter(fp, may17.strftime("%d/%B/%Y"))
with open(r'D:\homework_py\18.05\logs.txt', 'r') as fp:
    data_counter(fp, may18.strftime("%d/%B/%Y"))
with open(r'D:\homework_py\18.05\logs.txt', 'r') as fp:
    data_counter(fp, may19.strftime("%d/%B/%Y"))
with open(r'D:\homework_py\18.05\logs.txt', 'r') as fp:
    data_counter(fp, may20.strftime("%d/%B/%Y"))
