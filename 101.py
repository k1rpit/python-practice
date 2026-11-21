# базовое форматирования и методы в принт а также инпут

#print('1','2',sep='|',end=' ')
#print('3','4')
#print(5)
#print('1234567890!@#$%^&*()_+!"№;%:?*()_+><?~`AЭ')

#user_name = str(input('введите свое имя: '))
#print('user name  --> ',end=' ')
#print(user_name)

#масовые замена числ также метод обознанчения типа тоесть чтобы вывел он

#x = 10
#y = 15
#print(x,y)
#x,y = y,x
#print(x,y)

#print(type(x),'тип')



#user_number = int(input('введите нормер кварриты: '))

#padik = (user_number - 1) // 20 + 1
#itash = ((user_number  - 1) % 20 + 1 ) // 4
#print(f'этаж {itash}, подьезд {padik}')

# булл True и False а также логические операторы и логические операторы в переменные и функция bool()

#a = 0
#b = 1
#print(a==b)
#bool_number = a != 2 and b != 2
#print( not bool_number)
#print(bool(a))

# условия

#year = 2000
#if year % 4 == 0 and year % 100 != 0:
#        print('year is leap')
#elif year % 400 == 0:
#    print('year is leap')
#else:
#    print('year not is leap')


#user_input = int(input('input number type int~$-> '))
#number = user_input % 2 == 0

#if number:
#   print('четное')
#else:
#    print("нечетное")


#user_str = str(input('input class str~#$~> '))
#if user_str:
#    print('1')
#else:
#    print('0')

#user = input('input')
#user_type = type(user)

#if user_type == str:
#    print('str')
#elif user_type == int:
#    print("int")
#elif user_type == bool:
#    print('bool')
#elif user_type == float:
#    print("float")
#else:
#    print('else')

#user_passworld = input('passworld ->')
#user_passw_len = len(user_passworld)

#if user_passw_len < 8:
#    print(f'passworld is not safe len is {user_passw_len}')
#else:
#    print('passworld is real safe and true!')

#user_mail = str(input('input mail '))
#if user_mail and '@' in user_mail and '.'  in user_mail:
#    print('mail valid')
#else:
#    print('error!')    

#my_input = str(input('> '))
#input_str = my_input.isdigit()

#if input_str:
#    print(my_input)
#else:
#    print(f"'{my_input}'не число! ")
    
# работа с текстом
#user_input = str(input('> '))
#print(user_input.upper())
#print(user_input.lower())
#print(user_input.strip())#убирает лишнее пробелы и их
#print('%s раз повртяется \"r\"в\t %s ' % (user_input.count('r'), user_input))




# метод format() а также работа со строками и форматирования через %

#stroka = input('>')
#world = 'привет меня завут {}'.format(stroka)
#print(world)

#world = "айпи {0} был сканирован и был найден опасный порт {1} , а также айпи {0} диномический".format('12.122.122.122',23)
#print(world)

#a = 19
#b = 1
#print('порты по типу {start}-{end_} встречаются редко и скорее всего это хонипот'.format(start=b,end_=a))
#print('тип пакета %s он пришол на порт %i  и на айпи %s'% ('tcp',21,'99.23.87.122'))

#error_tect = 'ivalid email'

#user_mail = str(input('input mail '))
#if user_mail and '@' in user_mail and '.'  in user_mail:
#    print('mail valid %s '% (user_mail)) 
#else:
#   print('error! %s %s' % (user_mail,error_tect))    
#user_part_one = str(input('введите 1 придмет который лучше <>> '))
#user_part_two = str(input('введите 2 придмет который хуже <>> '))
#user_part_final = str(input('введие аргумент <>> '))
#print('%s лучше чем %s так как %s' % (user_part_one,user_part_two,user_part_final))

#user_input_str = input('> ')
#user_input_len = len(user_input_str)
#user_input_data = 'ваш текст соствляет длину %s симболов' % (user_input_len)
#print(user_input_data)

#a = 1024-91+1323215-91-91
#print('%x' % (a))

#message = "\" привет \" написал он,\tно для чего?"\
#          "  это сложно вообразить "
#print(message)

#input_ip_user = input('/>')
#port = 21
#num_log = 424102493

#srt_parts = 'на айпи %s был найден порт %i номер лога\t %X [+]' % (input_ip_user,port,num_log)
#print(
#srt_parts
#)


#big_int = 100 ** 1000
#print(f'количесво нулей у  большого числа ровна {len(str(big_int)) - 1}'
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
# списки list++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++

#list_data = [1,2,3]
#list_user = [1,2,3]
#list_check = list_data == list_user
#list_bool = bool(list_data)
#print(list_check,list_bool)
#print(1 in list_user ,'элемнт 1 есть',sep='|')

#a = 1
#b = 2
#x = 4
#y = 5

#list_number = [a,b,x,y]
#print(list_number)
#print(f"max\t{max(list_number)} min\t{min(list_number)} sum\t{sum(list_number)}")

#list_str = list('qwerty')
#list_int = list(list_data)

#new_list = list_int+list_str
#new_list.append(x)
#new_list.pop(0)
#print(new_list)


#num1 = [10,0,1]
#num2 = [1024,2]
#num1.extend(num2)
#num1.sort(reverse=True)
#print(num1)

#my_str = 'си лучше си++'
#my_list = my_str.split(" ")
#print(my_list)

#no_my_list = " ".join(my_list)
#print(no_my_list)


#input_port = int(input('> '))
#data_list_port = [21,22,23]
#if input_port:
#    data_new = data_list_port.copy()
#    data_new.append(input_port)
#    print("теперь в списке портов {} добаввился обьект види порта {} и теперь список портов выглядит так {} ".format(data_list_port,input_port,data_new))

#data_port = [21,22,4444]
#no_safe_port = 4444
#print(data_port)
#if no_safe_port in data_port:
#    data_port.remove(no_safe_port)
#    print('был найден опасный порт %i и он был удален' % (no_safe_port))
#    print(data_port)

#data_list1 = ['bit','python3']
#data_list = ['TCP','UDP','CPU']
#data_list.pop()
#data_list.extend(data_list1)
#print('список пакетов, а также связоное с другой обласью айти',data_list)
#%%%%%%%%%%%%%
# срезы [0:5]%
#%%%%%%%%%%%%%
#data_list = [1,2,3,4,5]
#print(data_list[0])
#data_list[0] = -1
#print(data_list[-5])

#data_list[2],data_list[4] = data_list[4],data_list[2]
#print(data_list)
#data_list_slise = list(data_list[2:len(data_list)])
#print(data_list_slise[:])


#data = [1,2,3,4,5,6,7,8,9,10]

#print(data[::-1]) # аналог реверс()
#new_data = list(reversed(data))
#data_list = ['1.1.1.1','2.2.2.2','3.3.3.3','4.4.4.4']
#number_stop = len(data_list)
#input_user_one = int(input('введите 1 число слайса>'))
#input_user_two = int(input('введите 2 число слайса>'))

#if input_user_one > number_stop or input_user_two > number_stop:
#    print('надо чтобы числа были меньше %i' % (number_stop))
#else:
#    print(data_list[input_user_one:input_user_two])

#+++++++++++++++++++++++++++++++++++++++++
# *цикл for+++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++
#data_ports = (21,23,455,3389,1038)
#for ports_index in data_ports:
#    print(ports_index)

#count_index = 0
#string = "BIG data"
#for i in string:
#    #print(i)
#    if i == 'a':
#        count_index+= 1
#        print(count_index,'количвво буквы a')

#list_bigData = ['a1','b2','c3','r4','x5','x6']

#for index in list_bigData:
#    print(index)
#    for nuber_bokw in index:
#        print(nuber_bokw)

#num_port = [21,223,48150,55535,1008,65512,122,54201,4444,109]
#Private_port = 49152
#port_stop = 4444

#str_data = 'он что-то сделал '
#indexes = []
#count = 0

#for i in range((len(str_data))):
#    if str_data[i] == 'о':
#        count += 1
#        indexes.append(i)
#print(indexes)
#print(count)
#a = 10
#listing = [i*a for i in range(10)]
#print(list(listing))

#for i_one in num_port:
#    if i_one >= Private_port:
#        print('порт\t %i заглушка!' % (i_one))
#for port in num_port:
#    if port >= 49152:
#        continue
#    elif port == port_stop:
#        print('на айпи открыт порт\t {stop} сканирвоания окончено'.format(stop=port_stop))
#        break
    
#    print(port)

#port_old = list(range(20))

#port_system = list(range(20,1024,100))

#for index in range(len(port_system)):
#    port_system[index] += 4
#print(port_system)


#port_system = list(range(20,1024,100))

#port= list(range(25))
#port_old = []
#for i in port:
#    if i <= 19:
#        port_old.append(i)

#print(port_old, 'старые порты',sep='||||')

#ports_min_600= []

#for i in range(len(port_system)):
#    if port_system[i] > 600:
#        ports_min_600.append(i)
#print(ports_min_600,'индексы  портов %s которые %s %i ' % ('port_system',"больше",600))

#port = []
#for i in range(1,100,10):
#   if i <= 20:
#        continue
#    else:
#        port.append(i)

#print(port)



#port_1 = list(range(1024,1050))
#port_2 = []
#print(port_1)
#for i in port_1:
#    if i < 1035:
#        continue
#    else:
        
#        port_2.append(i)
#print(port_2)


#data = ['helloy','as','1','№','з2','E|']
#data_stop = '№'

#for request in data:
#    for i in request:
#        if data_stop in i:
#            print('обнуружены\t\"{}\"\tугроза! т.к не подерживается!'.format(data_stop))
#            break

#central_data = ['155.167.5.232','34.221.77.55','9.0.190.109','87.4.233.251']
#black_list = ['9.0.190.109','untrusted_IP']
#clear_data = []

#for port in central_data:
#        if port == black_list[0]:
#            print('порт\t %s не был добавлен в даные так как он %s' % (black_list[0],black_list[1]))
#            continue
#        clear_data.append(port)
#    
#print(clear_data)

#++++++++++++++++++++++++++++++++++++
# ++++функция def++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++


#data_port = [18,19,20,10,1,293,209]
#data_port_more = [14,19,2,11,14,993,2003]
#data_port_clear = []

#def func_check_ports(list_ports):
#    for port in list_ports:
#        if port <= 19:
#            continue
#        else:
#            data_port_clear.append(port)
#    print(f"очищенный список портов который меньше 19:\t {data_port_clear}")
#    return True

#avarage_check_port = func_check_ports(data_port)
#if avarage_check_port:
#    print('все прошоло успешно функция вернула {}'.format(avarage_check_port))

#def count_ip(string):
#    znak = '.'
#    conunt = 0 
#    for i in string:
#        if i == znak:
#            conunt += 1
#    return conunt

#count_def = count_ip('122.133.05.0')
#print('всего точек  в айпи %i' % (count_def))

#def func_not():
#    pass
#func_not()


#def format_data_ip(*,port: int,string: str) :
#    return print('порт:\t{0} {1} '.format(port,string))

#format_data_ip(port=19,string='устаревший')
#ip_classic = '155.123.70.2'
#def func_scan(*,port: int,ip=ip_classic):
#    return ' на айпи\t %s найден порт\t %i' % (ip,port)
#print(func_scan(port=813))
#print(func_scan(port=23,ip='155.34.2.90'))


# : подсказвает какой тип должен быть = задает базовый аргемнт

#ip = '122.234.11.11'
#def func_ip_check_valid(*,ip:str):
#    if '.' in ip  and 15 >= len(ip):
#        return True

#def func_check_ports(*,ip:str,valid:bool):
#    if valid:
#        print(f'{ip} был просканировал и были найден порт 21')

#valid = func_ip_check_valid(ip=ip)
#print(valid)
#func_check_ports(ip=ip,valid=valid)



#def func_data_lst():
#    list_unstable = [1,2,3,4,5,6,7,8,9,19,23,90,100,1024]
#    list_port_clear = []
#    for port in list_unstable:
#        if port > 19:
#            list_port_clear.append(port)
#    return list_port_clear

#print(func_data_lst())

#data = [122,'12.34.12.4',1092,'56.23.122.0','123.434.134.9',912,23,'71.23.45.0']
#data_ip = []
#data_ports = []

#def func_sort_ip_port(*,list_data:list):
#    for i in list_data:
#        if type(i) == int:
#            data_ports.append(i)
#        else:
#            data_ip.append(i)
#    print(f"""
#    {data_ports} порты,
#    {data_ip} айпи
#    """)
#func_sort_ip_port(list_data=data)

#input_user = int(input('> '))

#def func_generator(*,number:int):
#    list_generat = [i*number for i in range(10)]
#    return list_generat
#func = func_generator(number=input_user)
#list_num = list(func)
#print(list_num)


# ОБЛАСТЬ ВИДИМОСТЬ ПЕРЕМЕННЫХ 

#global_num = 10

#def func_num(): # так лучше не делать
#    global global_num
#    global_num = 20

#print(global_num,'до')
#func_num()
#print(global_num,'после')

#data_port = 20
#port_name = 'FTP'
#port_baner = '220 ProFTPD 1.3.5 Server ready.'


#def func_check_port(*,port:int,name:str,baner:str) -> bool:
#    if 'FTP' in baner and 'FTP' in name and port == 21:
#        port_wrong = False
#    else:
#        port_wrong = True
#    return port_wrong

#if_port = func_check_port(port=data_port,name=port_name,baner=port_baner)
#print(if_port)
#if if_port:
#    data_port += 1
#    print(data_port)

#*********************************************
#**************while**************************
#*********************************************
#цикл вайл 
#port = 2

#while port <20:
#    port += 1

#print(port)

#unnew_ports = [15,18,19]
#while unnew_ports:
#    port_del = unnew_ports.pop()
#    print(port_del)
#print(unnew_ports)

#import random as R
#A = list(range(20))

#def fn_random():
#    return R.choice(A)

#while fn_random() != 7:
#    print(fn_random())



# =В F СТРОКАХ
#data = 99
#print(f"{data=}")

#|||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||кортежи tuple()||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||

#user_ports = (21,8080,22)
#user_ip = '23.55.67.91',

#port1,port2, _ = user_ports
#print(port1)

#def func_tuple(*,data1,data2):
#    data_tuple = (data1,data2)
#    print(data_tuple)
#    print(data_tuple[0])
#    for i in data_tuple:
#        print(i,'из чего состоит кортеж')

#    if '1.1.1.1' in data_tuple:
#        print('в кортежи есть 1.1.1.1')
#        return data_tuple


#dns1,dns2 = func_tuple(data1='1.1.1.1',data2='9.9.9.9')
#print(f'первый днс {dns1} второй днс {dns2}')




    

#|||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||словарь dist()|||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||


#port_data = {
#    'RFC1006':122,
#    'TELNETS':922,
#    'MGE UPS':3397
#}
#port_data['SSH'] = 22


#data_clear_dist = {}
#data_clear_dist['ip'] = '12.34.78.90'
#data_clear_dist['port'] = 778
#data_clear_dist['valid'] = True
#print(data_clear_dist.get('DNS','8.8.8.8'))

#for item in data_clear_dist.items():
#    key,value = item
#    print(f'item:{item}\tkey:{key}\tvalue:{value}')

#for key,value in data_clear_dist.items():
#    print(key,end=' ')
#    print(value)

#for key in data_clear_dist.values():
#    print(key)


#data_ip = {
#    'ip':'45.12.34.1','ports':[21,78,80],'DNS':'9.9.9.9'
#}

#data_ip_other = {
#    'states':'stable','validit':True,'DNS':'1.1.1.1'
#}

#data_ip.update(data_ip_other)
#print(data_ip)

#data_ip = data_ip | data_ip_other
#print(data_ip)



#input_ip = input('ip>')
#input_port =int(input('port>'))
#input_dns = input('dns>')
#input_valid = int(input('valid(0/1)>')) 

#data = {
#    'ip':input_ip,
#    'port':input_port,
#    'DNS':input_dns,
#    'valid':input_valid
#}

#data_other = {'os':'win32','local_port':56099}

#def func_dist(*,d:dict):
#    print(data)
#    keys_data = []
#    value_data = []
#    if bool(data['valid']):
#        data.update(data_other)
#        for keys,values in d.items():
#            keys_data.append(keys)
#            value_data.append(values)
#    return keys_data,value_data

#tuple_data=func_dist(d=data)
#keys_list,value_list = tuple_data
#print('key',keys_list,'value',value_list)


#json = {
#    'stock_ip': '122.34.56.90',
#    'add_dns' : True,
#    'start_hack':True
#}
#ports = [339,3389]
#dns = '9.9.9.9'
#def generat_log(*,json=json):
#    if json['start_hack']:
#        if json['add_dns']:
#            log = 'на айпи  {} был найдены порты\t {},{}\t днс:\t{}'.format(json['stock_ip'],ports[0],ports[1],dns)
#        else:
#             log = 'на айпи  {} был найдены порты\t {},{}'.format(json['stock_ip'],ports[0],ports[1])
#    return log

#print(generat_log())




#json_scan = {
#   'check_os':True
#}

#input_user_ip = input('input ip>')
#data_ports = {
#    '22/tcp':'SSH',
#    '80/tcp':'http',
#    '9929/tcp':'npling-echo'
#}


#def func_scan_ip(*,ip=input_user_ip,ports=data_ports,json=json_scan):
#    if json_scan['check_os'] and ip:
#        log_scan = f'''
#        ip ({ip}) scan
#        {len(ports)} TCP port open:
#        PORT              SERVIS
#        {'22/tcp'}:{ports['22/tcp']}
#        {'9929/tcp'}:{ports['9929/tcp']}
#        {'80/tcp'}:{ports['80/tcp']}#
#
#        os: 99% linux
#        '''
#    elif ip:
# 
#           log_scan = f'''
#        ip ({ip}) scan
#        {len(ports)} TCP port open:
#        PORT              SERVIS
#        {'22/tcp'}:{ports['22/tcp']}
#        {'9929/tcp'}:{ports['9929/tcp']}
#       {'80/tcp'}:{ports['80/tcp']}
#        '''
        
#    return log_scan

#print(func_scan_ip())


#№№№№№№№№№№№№№№№№№№№№№№№№№№
#№№№№*args|**kwargs№№№№№№№№
#№№№№№№№№№№№№№№№№№№№№№№№№№№

#data_more = {'valid':True}
#def func_def(**kwargs):
#    print(f'''
    
#    вывод:{kwargs}
#    тип:{type(kwargs)}
    
#    ''')
#func_def(ip='12.34.90.1',dns='9.9.9.9',port=[21,25,23,445],**data_more)

#def func_full_data(*args,ip='109.234.90.23',**kwargs):
#    print(args,ip,kwargs)
#func_full_data(120,122,80, **data_more)

#data = {'a1':1,'a4':4,'a5':2}

#def func_modef_dict(dict1=data, **kwargs):
#    for key,value in kwargs.items():
#        is_dict = False
#        if dict1.get(key) != value:
#            is_dict = True
#            dict1[key] = value
#    return dict1, is_dict

#result = func_modef_dict(dict1=data,a1 = 1)
#old_dist,is_true = result

#print(old_dist,is_true)



#input_value1 = input('введите знаичения 1 ключа>')   
#input_value2 = input('введите заначения 2 ключа>') 
#input_value3 = input('введите знаичения 3 ключа>')

#def func_create_dict(**kwargs):
#    return kwargs
#result = func_create_dict(key1=input_value1,key2=input_value2,key3=input_value3)
#print(result)

#input_value1 = input('введите знаичения 1>')   
#input_value2 = input('введите заначения 2>') 
#input_value3 = input('введите знаичения 3>')


#def func_create_list(*args):
#    return list(args)
#result = func_create_list(input_value1,input_value2,input_value3)
#print(result)
#print(type(result))

#data_ip1 = {
#    'ip':'109.67.13.52',
#    'ports':[21,23,45],
#    'valid':True
#}
#data_ip1_more = {
#    'dns':'8.8.8.8',
#    'os':'linux',
#    'level_connect':'low'
#}


#def func_associations_dist(*,dict_data:dict,**kwargs):
#     data_ip = dict_data | kwargs;return data_ip
#print(func_associations_dist(dict_data=data_ip1,**data_ip1_more))



#base_data = {
#    'ip':'192.122.101.2',
#    'ports':(21,22,993),
#    'valid':True
#}
#data_more = {
#    'Subnet_Mask':'255.255.255.0',
#    'DNS':'8.8.8.8',
#    'ports_Private':[60012,49087],
#    'MAC':'00:5A:2B:3C:4D:5A'
#}
    
#def func_dict_data(*,data=base_data,**kwargs):
#    data_clear = data | kwargs
#    data_clear['ports_Private'].append(61027)
#    return data_clear
#print(f'инфомация базовая{base_data=}')
#print(f'доп инфа {data_more=}')
#print('общая информация',func_dict_data(**data_more))
#data_ip = {'ip':'97.12.71.4','ports':[]}
#while 1 != 2:
#    input_ports = (input('введите порт  >>>'))

#    def func_data_use(*args,**kwargs):
#        ports_tuple = tuple(args)
#        kwargs['ports'].append(ports_tuple)
#        return ports_tuple
#    print(func_data_use(input_ports,**data_ip))
#    print(data_ip)

#data_MQ9Reaper = {
#    'weapon_arm_auth':15.0,
#    'gps_coordinates':12.0,
#    'A0-Ks/x/x/z/x':25.0,
#    'radar_scan_area':13.0,
#    '*~-ss/z/x/z/x':25.0
#}

#def func_Reaper_Hz_check(**kwargs):
#    clear_value = []
#    for key,value in kwargs.items():
#        if value != 25.0:
#            clear_value.append(key)
#        else:
#            continue
#    return clear_value
#print(func_Reaper_Hz_check(**data_MQ9Reaper))

#!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!JSON!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!
#import json

#data_ip = {'ip':'98.34.21.9','ports':[21,23,22],'valid':True}
#json_data_dumps = json.dumps(data_ip)
#json_data_loads = json.loads(data_ip)

#!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!IMPORT!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!
#my_port = 21
#import project_1
#print(dir(project_1))
#print(globals().keys())

#import generaor_type

#a=generaor_type.func_generator(type_data=tuple,data='21')#
#print(a)


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$import reguests$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


#import requests
#import time


#url = "https://api.binance.com/api/v3/ticker/price"
#response_url = requests.get(url,params={"symbol":'BTCUSDT'})

#counter = response_url.content
#print(counter)
#print(type(counter))

#price = response_url.json()
#print(price)

#price_int = float(price['price'])
#print(price_int)
#bitcoin_prices = []
#for i in range(20):
 #   response_url = requests.get(url,params={"symbol":'BTCUSDT'})
 #   price = float(response_url.json()['price'])
 #   bitcoin_prices.append(price)
 #   time.sleep(1)

#print('--'*32)
#print(f'цена биткона в течении 20 секунд')
#print(f'максимально:\t{max(bitcoin_prices)}')
#print(f'минимально:\t{min(bitcoin_prices)}')
#print(f'размах:\t{max(bitcoin_prices)-min(bitcoin_prices)}')
#print('--'*32)




#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!set()!!множества!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




#data_ip =['192.168.58.21','192.168.18.3','192.168.48.2','192.168.51.1','192.168.51.1']
#data_ip_more =['192.168.58.21','192.168.98.12','192.168.48.2','192.168.51.1']

#data_ip_global = data_ip + data_ip_more
#data_ip_set = set(data_ip_global)
#data_ip_global = list(data_ip_set)
#print(data_ip_global)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!сортировка и фильтрация!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#data_id = ['b2','c3','x1','l0','i30','a8','k0','n2']
#data_id = sorted(data_id)[::-1]
#print(data_id)

#data_ip =['192.168.58.221','19.16.18.3','192.168.48.2','192.1.51.1','192.168.51.1']

#def sort_data_ip(data: list) -> int:
    #return len(data)

#data_ip = sorted(data_ip,key=sort_data_ip)

#print(data_ip)
#from statistics import median

#network_traffic_averages = [
#    {"ip": "10.0.0.12", "average_packets": [0, 0, 1, 1, 8, 9, 12, 32, 43]},
#    {"ip": "172.16.254.1", "average_packets": [2, 3, 5, 7, 7, 12, 12, 13]},
#    {"ip": "192.168.1.100", "average_packets":[0, 3, 3, 6, 10, 12, 34]},
#    {"ip": "10.0.0.13", "average_packets": [0, 0, 1, 1, 8, 9, 12, 32, 43]},
#    {"ip": "10.0.0.14", "average_packets": [0, 0, 1, 1, 8, 9, 12, 32, 43]},
#]

#def sort_median(data: dict) -> tuple[int,int]:
#    return (median(data["average_packets"])),len(data['ip'])

#sort_ip = sorted(network_traffic_averages,key=sort_median)
#print(sort_ip[::-1])


#data_ports = [21,22,23,80,8888,22,25,443,20,2222]

#def filtr_ssh(port: int) -> bool:
#    return port != 22 and port != 2222

#filter_ports = filter(filtr_ssh,data_ports)
#print(list(filter_ports))


#raw_traffic = [
#    {"ip": "10.0.0.12", "ports": [22, 80, 443, 22]},
#    {"ip": "192.168.1.100", "ports": [80, 80, 80]},
#    {"ip": "172.16.254.1", "ports": [21, 23, 2222]},
#]

#def del_dupl_data_ip(*,data_traffic: list):
#    for data_ip in data_traffic:
#        data_ip['ports'] = set(data_ip['ports'])
#        data_ip['ports'] = list(data_ip['ports'])
        
#del_dupl_data_ip(data_traffic=raw_traffic)#

#def block_port_SSH(ports: int):
#    return ports != 22 and ports != 2222

#for i in raw_traffic:
#    i['ports']=list(filter(block_port_SSH,i['ports']))
#print(list(raw_traffic))

#data = [
#    {'traffic': [10, 2, 42, 80]},
#    {'traffic': [12, 2, 4, 80]},
#    {'traffic': [1, 3, 4, 8]},
#    {'traffic': [1, 332, 42, 80]},
#    {'traffic': [0, 12, 41, 2]},
#    {'traffic': [0, 32, 42, 8]},
#]
#def sort_data(data: dict):
#    return sum(data['traffic']) / len(data['traffic'])

#data = sorted(data,key=sort_data)[::-1]
#print(data)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!                                                    !!!!!!!!!!!!!
# !!!!!!!!!!!!!               █████    █████   ██████              !!!!!!!!!!!!!
# !!!!!!!!!!!!!              ██   ██  ██   ██  ██   ██             !!!!!!!!!!!!!
# !!!!!!!!!!!!!              ██   ██  ██   ██  ██████              !!!!!!!!!!!!!
# !!!!!!!!!!!!!              ██   ██  ██   ██  ██                  !!!!!!!!!!!!!
# !!!!!!!!!!!!!               █████    █████   ██                  !!!!!!!!!!!!!
# !!!!!!!!!!!!!                                                    !!!!!!!!!!!!!
# !!!!!!!!!!!!!                                                    !!!!!!!!!!!!!
# !!!!!!!!!!!!!                                                    !!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"""
ООП (Объектно-ориентированное программирование) — способ писать код в виде объектов, 
у которых есть свои данные (свойства) и действия (методы).

Основные термины:
- Класс (class) — чертеж или шаблон (например, "Машина").
- Объект (экземпляр) — конкретная вещь, созданная по чертежу (например, "красная BMW").
- Атрибуты — переменные внутри объекта, его характеристики (цвет, скорость).
- Методы — функции внутри объекта, его действия (ехать, тормозить).
- __init__ — конструктор, который задает начальные атрибуты при создании объекта.
- self — ссылка на сам конкретный объект, с которым сейчас идет работа.

4 принципа ООП:
1. Инкапсуляция — скрытие внутренней начинки и защита данных от прямого изменения.
2. Наследование — создание нового класса на основе старого с перенятием его свойств.
3. Полиморфизм — разное поведение одного и того же метода у разных классов.
4. Абстракция — выделение только главных характеристик объекта и отбрасывание лишнего.
"""


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!    ОПИСАНИЯ КЛАССОВ И СОЗДАНИЯ ОБЪЕКТОВ    !!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# ------------------- [сзнакомсто с классами и обьектами] -------------------

"""
class OneA():
    pass

class Oneb():
    pass
a = OneA()
b = Oneb()
print('обьект А:\t',a)
print('обьект Б:\t',b)

class CD ():
    pass
C = CD()
D = CD()
print(f'class C:\t{C};',end=" ")
print(f'class D:\t{D}')

is_cd_bool = C == D
print(f'C==D?:\t\t{is_cd_bool}')

print(f'класс обьекта C:\t{type(C).__name__}')
print(f'класс обьекта D:\t{type(D).__name__}')
"""

# ------------------- [ ПОЛЯ И МЕТОДЫ ] -------------------

"""
class CveClass:
    def set_cve(self,cve):
        self.cve_ftp = cve
    def chow_cve(self):
        print(f'CVE FTP:\t\t{self.cve_ftp}')
        
cve_ftp_2015 = CveClass()
cve_ftp_2020 = CveClass()

cve_ftp_2015.set_cve('CVE-2015-3306')
cve_ftp_2020.set_cve('CVE-2020-9273')


cve_ftp_2015.chow_cve()
cve_ftp_2020.chow_cve()

cve_ftp_2015.set_cve('CVE-2015-1419')
cve_ftp_2020.set_cve('CVE-2020-9272')


cve_ftp_2015.chow_cve()
cve_ftp_2020.chow_cve()
"""

CVE = 'CVE-2021-41773'
'''
class CheckDateCve:
    def check_date(self,cve: str) -> None:
        self.date_cve =  cve.split('-')[1]
        print('USER CVE:\t{}'.format(cve))
        
    def show_date_cve(self) -> None:
        print(f'DATE CVE:\t{self.date_cve}')
        
obj_check_date_cve = CheckDateCve()

obj_check_date_cve.check_date(CVE)
obj_check_date_cve.show_date_cve()
'''

# ------------------- [ КОНСТРУКТОРЫ И ДЕСТРУКТОРЫ ] -------------------
"""
class PrintCveUser:
    def __init__(self,cve='CVE-2000-0124'):
        self.name_cve = cve
        print(f'create obj "cve":\n{self.name_cve}')
    
    def __del__(self):
        print(f'del obj "cve":\n{self.name_cve}')
        
def creat_obj_cve(cve):
    obj_cve = PrintCveUser(cve)
    
    
cve_one =  PrintCveUser('CVE-2006-2369')
cve_two =  PrintCveUser('CVE-2026-24061')
cve_three =  PrintCveUser('VE-2019-0708')
cve_three.name_cve = 'CVE-2017-0144'


del cve_one;del cve_two;del cve_three
"""
'''
class SequenceNumberCve:
 def __init__(self,cve='CVE-1999-0004') -> None:
     self.sequence_number = cve.split('-')[-1]
 def chow_sequence_number(self) -> None:
     print(f' A Sequence Number CVE:\t\t{self.sequence_number}')


obj_cve_sn = SequenceNumberCve()
obj_cve_sn.chow_sequence_number()

'''
# ------------------- [ ОБЪЕКТЫ: РЕАЛИЗАЦИЯ КЛАССОВ ] -------------------
"""
class Unix:
    pass

class Darwin:
    pass

class Linux:
    pass

class BSD:
    pass

apple_os  = Darwin

hp_ux = Unix()
debian = Linux()

iOS = apple_os()
iPadOS = apple_os()
macOS = apple_os()


apple_os = iOS.__class__
watchOS = apple_os()

print(f'ОБЬЕКТ:\t"iOS" ПОД КЛАССОМ:\t{type(iOS).__name__}')
print(f'ОБЬЕКТ:\t"iPadOS" ПОД КЛАССОМ:\t{type(iPadOS).__name__}')
print(f'ОБЬЕКТ:\t"macOS" ПОД КЛАССОМ:\t{type(macOS).__name__}')
print(f'ОБЬЕКТ:\t"watchOS" ПОД КЛАССОМ:\t{type(watchOS).__name__}')

apple_os.__name__ = "darwin"
iOS.__name__ = "mac_os"

print(f'ОБЬЕКТ:\t"iOS" ПОД КЛАССОМ:\t{type(iOS).__name__}')
print(f'ОБЬЕКТ:\t"iPadOS" ПОД КЛАССОМ:\t{type(iPadOS).__name__}')
print(f'ОБЬЕКТ:\t"macOS" ПОД КЛАССОМ:\t{type(macOS).__name__}')
print(f'ОБЬЕКТ:\t"watchOS" ПОД КЛАССОМ:\t{type(watchOS).__name__}')
"""

'''
class GNU:
    pass
class Linux:
    pass
linux = Linux
gnu  = GNU

debian = linux()
red_heat = gnu()

linux.__name__ = 'GNU/LINUX'
gnu.__name__ = 'GNU/LINUX'

print('debian\n',type(debian).__name__)

print('red heat\n',type(red_heat).__name__)
'''
'''
class OpenSSH:
    cve = ['CVE-2024-6387']
    def set(self,cve_user: str):
        OpenSSH.cve.append(cve_user)
        
    def show():
        print(f'{OpenSSH.cve=}')
        


OpenSSH.cve = ['CVE-2018-15473']
OpenSSH.show()

High_Critical_vce_open_ssh = OpenSSH()



High_Critical_vce_open_ssh.set('CVE-2023-38408 ')
High_Critical_vce_open_ssh.set('CVE-2024-6387 ')


print(f'{High_Critical_vce_open_ssh.cve=}')
'''

"""
class Unix:
    os = 'BSD'
    
    def set(os_user):
        Unix.os = os_user
        
    def chow():
        print(f'{Unix.os=}')
Unix.chow()
Unix.set('SunOS')
Unix.chow() 

Unix.os = 'HP-UX'
print(f'{Unix.os=}')

Unix.set('BSD')

obj_BSD = Unix()
obj_mac_os = Unix()

print('-'*64)
print(f'класс:\t{Unix.os=}')
print(f'обьект №1:\t{obj_BSD.os=}')
print(f'обьект №2:\t{obj_mac_os.os=}')
print('-'*64)

obj_BSD.os = 'NetBSD'

print('-'*64)
print(f'класс:\t{Unix.os=}')
print(f'обьект №1:\t{obj_BSD.os=}')
print(f'обьект №2:\t{obj_mac_os.os=}')
print('-'*64)

obj_mac_os.os = 'Darwin'

print('-'*64)
print(f'класс:\t{Unix.os=}')
print(f'обьект №1:\t{obj_BSD.os=}')
print(f'обьект №2:\t{obj_mac_os.os=}')
print('-'*64)

del obj_BSD.os

print('-'*64)
print(f'класс:\t{Unix.os=}')
print(f'обьект №1:\t{obj_BSD.os=}')
print(f'обьект №2:\t{obj_mac_os.os=}')
print('-'*64)
"""
"""
class WinXPVM:
    def __init__(self):
        self.port = 445
        print('ПОРТ ОТКРЫВАЕТСЯ:\t{port}'.format(port=self.port))
        
    def __del__(self):
        print('ПОРТ ЗАКРЫВАЕТСЯ:\t{port}'.format(port=self.port))
        
    def set_port(self,p: int):
        self.port = p
        
    def chow_port(self):
        print('ПОЛЕ ОБЬЕКТА(ПОРТ):\t{port}'.format(port=self.port))
        
target_vm_xp = WinXPVM()

target_vm_xp.set_port(139)
target_vm_xp.chow_port() 

WinXPVM.chow_port(target_vm_xp)
WinXPVM.set_port(target_vm_xp,135)
"""
'''
class DebianOldVM:
     def __init__(self):
        self.ports = [22]
        print('ПОРТ ОТКРЫВАЕТСЯ:\t{port}'.format(port=self.ports))
        
     def __del__(self):
        print('ПОРТ ЗАКРЫВАЕТСЯ:\t{port}'.format(port=self.ports))
        
     def set_port(self,p: int):
        self.ports.append(p)
        
     def chow_port(self):
        print('ПОЛЕ ОБЬЕКТА(ПОРТ):\t{port}'.format(port=self.ports))
        
obj_save_port_debian_old_vm = DebianOldVM()
obj_save_port_debian_old_vm.set_port(23)
obj_save_port_debian_old_vm.set_port(21)
obj_save_port_debian_old_vm.chow_port()
        
obj_not_save_port_debian_old_vm = DebianOldVM()
obj_not_save_port_debian_old_vm.set_port(993)
obj_not_save_port_debian_old_vm.set_port(443)
obj_not_save_port_debian_old_vm.chow_port()
'''

'''
class scan:
    def __init__(self,*,port: int,ip: str) -> None:
        self.port = port
        self.ip = ip
    def chow_result_scan(self):
        print('=='*32)
        print(' SCAN IP\t[%s]\tIP:\t[%i]' % (self.ip,self.port))
        print('=='*32)
        
obj_scan_port_445 = scan(port=445,ip='40.23.90.2')
obj_scan_port_22 = scan(port=22,ip='20.35.90.102')

def show_obj_scan():
    obj_scan_port_22.chow_result_scan()
    obj_scan_port_445.chow_result_scan()
    
show_obj_scan()
'''

'''
class ExploitBuilder:
        def __init__(self,*,vce: str,ip: str) -> None:
            self.target_ip = ip
            self.vce = vce
            
            if self.vce == 'CVE-2014-0160':
                self.timeout = 2.0
                self.payload = '0/0/0/0/0/n/r/n'
            elif self.vce == 'CVE-2017-5638':
                self.timeout = 0.2
                self.payload = 'x/x/0/t/0/n/r/n'
            elif self.vce == 'CVE-2021-44228':
                self.timeout = 6.2
                self.payload = '0/n/r/n'
            else:
                self.timeout = 0.0
                self.payload = 'r/n'
                self.vce = 'invalid'
                
                
        def chow_parameters_exploi_builder(self):
            print('~~'*32)
            print(f'target:\t{self.target_ip=}')
            print(f'VCE:\t{self.vce=}')
            print(f'payload:\t{self.payload=}')
            print(f'timeout:\t{self.timeout=}')
            print('~~'*32)
        
                
obj_exploit_open_sll = ExploitBuilder(vce='CVE-2021-44228',ip='192.168.158')
obj_exploit_open_sll.chow_parameters_exploi_builder()
'''

'''
class SearchPortServis:
    def __init__(self,*,port: int):
        port_servis_dict: dict[int,list[str]] = {22:['SSH','SCP','SFTP '],23:['Telnet'],445:['SMB','CIFS','Microsoft-DS']}
        self.port = port
        
        result_search_port_servis = port_servis_dict.get(port,False)
        if result_search_port_servis:
            print(f'на порте:\t{self.port}\t\tсервисы:\t{result_search_port_servis}')
        else:
            print('порта нету в базе данных')

search_port = SearchPortServis

obj_result_search = search_port(port=23)    
'''   
'''  
from secrets import choice as random   
class ScanIpPort:
    def __init__(self,*,ip:str) :
        self.ports = [22,80,13]
        self.ip = ip
        self.open_port = random(self.ports)

    def return_ip_port(self)-> tuple[str,int]:
         return self.ip,self.open_port

class BanerGrabbing:
    def __init__(self,*,ip: str,port: int) -> None:
        self.baner_port = {22:"SSH-2.0-OpenSSH_8.9p1",80:"HTTP/1.1 200 OK",13:"15 NOV 2026 19:08:00 MSK"}
        self.ip = ip
        self.port = port
        
        result_baner = self.baner_port.get(port,False)
        if result_baner:
            print(result_baner)
        else:
            print('банер не нашолся')

scan = ScanIpPort
baner = BanerGrabbing

obj_scan = scan(ip='192.168.0.1')
ip,port = obj_scan.return_ip_port()
obj_baner = BanerGrabbing(ip=ip,port=port)
'''

        
# ==================== { ОПЕРАЦИИ С АТРИБУТАМИ КЛАССОВ И ОБЪЕКТОВ } ====================
# класс это словарь
"""
class ip_one:
    pass

class ip_two:
    ip = '192.168.0.104'
    def chow_ip():
        print(f'поле класса{ip_two=}:\t\t{ip_two.ip=}')
        
    def chow_ports(self):
        print(f'ПОРТЫ {ip_two.ip=}:\t\t{self.ports=} ')
        
    def __init__(self):
        self.ports = [20,445,21,80,8080,137,5900,135]
        
port = [139,2222]

print('='*128)
for p in ip_one.__dict__:
    print(f'{ip_one.__dict__[p]=}')        

print('='*128)

for p in ip_two.__dict__:
    print(f'{ip_two.__dict__[p]=}')   
print('='*128)
    
ip1 = ip_one()
ip2 = ip_two()

print(f'{ip1.__dict__=}')
print(f'{ip2.__dict__=}')
"""
# >>>>>>>>>>>>>>>>>>>> ( КОПИРОВАНИЕ ОБЪЕКТОВ ) <<<<<<<<<<<<<<<<<<<<
"""
from copy import *

class DataIp:
    pass
2
obj_data_ip = DataIp()

obj_data_ip.ip = '192.168.0.109'
obj_data_ip.ports = [5900,8080,5901]

obj_data_ip_safe = obj_data_ip

obj_data_ip_copy = copy(obj_data_ip)
obj_data_ip_deepcopy = deepcopy(obj_data_ip)

obj_data_ip_copy.ports.append(22)
obj_data_ip_deepcopy.ip = '10.56.0.8'

print("<>"*64)
print(f'{obj_data_ip.ip=}\t{obj_data_ip.ports=}')
print(f'{obj_data_ip_safe.ip=}\t{obj_data_ip_safe.ports=}')
print(f'{obj_data_ip_copy.ip=}\t{obj_data_ip_copy.ports=}')
print(f'{obj_data_ip_deepcopy.ip=}\t{obj_data_ip_deepcopy.ports=}')
print("<>"*64)
"""

'''
from copy import deepcopy as dcopy


class VMWinXp:
    pass

VMWinXp.ip = '10.12.0.3'
VMWinXp.ports = [137,135,139,5000]

vm_xp = VMWinXp()
vm_xp.ports = VMWinXp.ports

vm_xp_rdr = dcopy(vm_xp)
vm_xp_samba = dcopy(vm_xp_rdr)

vm_xp_rdr.ports.append(3389)
vm_xp_samba.ports.append(445)

print('>>'*32)
print(f'{vm_xp_rdr.ports=}')
print(f'{vm_xp_samba.ports=}')
print('<<'*32)
'''



# ========================================================================
# root#~ ./ДОКУМЕНТАЦИЯ_И_ДЕКОРАТОРЫ

'''
class GNU:
    """GNU NOT UNIX"""
    pass

class MacOs:
    """DARWIN"""
    pass


print(f'ДОКУМЕНТАЦИЯ класса GNU:\t\t{GNU.__doc__}')
print(f'ДОКУМЕНТАЦИЯ класса MacOs:\t\t{MacOs.__doc__}')


obj_linux = GNU()
obj_IOS = MacOs()

obj_linux.__doc__ = 'класс линукс'
obj_IOS.__class__.__doc__ = "класс айос"

print(obj_linux.__doc__)
print(obj_IOS.__doc__)
'''

'''
class filterData:
    """фильтарция всего кроме '9.3.1.0' """
    def filter_data(data: str) -> bool:
        return not data != '9.3.1.0'
    
data_raw: list[str] = ['1.3.4.0','10.3.6.8','1.0.0.1','9.3.1.0','94.3.23.1','100.4.5.1','1.7.8.9']
data_clear = list(filter(filterData.filter_data,data_raw))
print(data_clear)
print(filterData.__doc__)
'''


#_______________________________________________________________________________

"""
def set_data(Data):
    class SetData:
        value = Data()
    SetData.__name__='мой'+Data.__name__
    return SetData
@set_data
class UniversalClass:
    def __init__(self):
        self.number = 923
        
    def show(self):
        print(f'поля UniversalClass:\t{self.number=}')
        
#univ_obj =set_data(UniversalClass)()
univ_obj = UniversalClass()

univ_obj.value.show()
print(f'класс обьекта:\t{univ_obj.__class__.__name__=}')
print(f'класс поля обьекта "value":\t{univ_obj.value.__class__.__name__=}')
"""


# ==============================================================================
# ================    ИСПОЛЬЗОВАНИЕ КЛАССОВ И ОБЪЕКТОВ    =====================
'''
import random
from time import sleep
class Bank:
    def __init__(self) -> None:
        self.value = 0
        self.balance_activity = True
    def show_value(self) -> None:
        if self.value < 0:
            self.balance_activity = False
            print('ВАШ БАЛАННС УШОЛ В МИНУС')
        else:
            print(f'ваш баланс:\t{self.value}')
    def earn(self)-> None:
        if self.value < 0:
            self.balance_activity = False
            print('ВАШ БАЛАННС УШОЛ В МИНУС')
        else:
            self.value += random.randint(1,10)
    def spend(self) -> None:
        if self.value < 0:
            self.balance_activity = False
            print('ВАШ БАЛАННС УШОЛ В МИНУС')
        else:
             self.value -= random.randint(1,10)   
             
bank_user = Bank()

def user_actions(*,obj=bank_user) -> None:
    while obj.balance_activity:
        sleep(random.randint(1,2))
        obj.earn()
        obj.show_value()
        sleep(random.randint(1,2))
        obj.spend()
        obj.show_value()
        
user_actions()
'''
'''
from secrets import choice as randomList
random_data_ports: list[list[int]] = [[22,21,445],[20,21],[23,21,22],[80],[80,22],[445],[19,22],[23],[2000,22],[564]]

data_port_baner: dict[int,str] = {
    19:' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefg',
    20:None,
    21:'220/t(vsFTPd 3.0.5)/n/n',
    22:'SSH-2.0-OpenSSH_for_Windows_7.7',
    23: 'FreeBSD/amd64 (amnesiac) (pts/0)/n',
    80:'Server: OpenBSD httpd',
    445:'Windows Server 2008 R2 Standard 7601 Service Pack 1',
    564: '9P2000',
    2000: '/nMikroTik bandwidth-test server/n/r/n'
}


class ScanIpPorts:
   def __init__(self) -> None :
       self.ports =  random_data_ports
       self.open_ports = randomList(self.ports)
       
   def return_ports(self) -> list[int] :
       return self.open_ports


class BanerScan:
    def __init__(self,*,open_ports: list[list[int]],data_baner:dict[int,str]) -> None:
        self.ports = open_ports
        self.baners = data_baner
        self.baners_list = []
    def get_banner(self) -> list[str]:
        for i in self.ports:
            result_search_baner = self.baners.get(i,None)
            if result_search_baner:
                self.baners_list.append(result_search_baner)
        return self.baners_list

class ShowDataPortsBanner:
    def __init__(self,*,baners: list[str],ip:str) -> None:
        self.baners = baners
        self.ip= ip
    def show_baners(self):
        print('='*64)
        print(f'IP:\t{self.ip=}\nБАНЕРА:\t{self.baners=}')
        print('='*64)


def scan(*,ip: str) -> None:
   obj_scan = ScanIpPorts()
   obj_baner =BanerScan(open_ports=obj_scan.return_ports(),data_baner=data_port_baner)
   obj_show = ShowDataPortsBanner(baners=obj_baner.get_banner(),ip=ip)
   obj_show.show_baners()

scan(ip='192.168.0.105')
'''
'''
import random
cve_data_base: dict[str, float] = {
    "CVE-2021-44228": 10.0,
    "CVE-2017-0144": 8.8,
    "CVE-2014-0160": 7.5,
    "CVE-2024-3094": 10.0,
    "CVE-2023-44487": 7.5,
    "CVE-2020-0601": 8.1,
    "CVE-2019-11043": 9.8,
    "CVE-2021-34527": 8.8,
    "CVE-2018-11776": 9.8,
    "CVE-2022-22965": 9.8,
    "CVE-2025-21520": 1.8,
    "CVE-2023-21928": 1.8,
    "CVE-2026-60913": 1.9,
}

cve_list: list[str] = [
    "CVE-2021-44228",
    "CVE-2017-0144",
    "CVE-2014-0160",
    "CVE-2024-3094",
    "CVE-2023-44487",
    "CVE-2020-0601",
    "CVE-2019-11043",
    "CVE-2021-34527",
    "CVE-2018-11776",
    "CVE-2022-22965",
    "CVE-2025-21520",
    "CVE-2023-21928",
    "CVE-2026-60913",
]


ips: list[str] = [
    "45.83.192.14",
    "185.220.101.34",
    "91.108.56.130",
    "81.19.70.3",
    "104.21.48.190",
    "77.88.55.242",
    "89.208.103.21",
    "176.59.44.118",
    "62.112.113.5",
    "142.250.185.78",
]


class GeneratorLog:
    def __init__(self,*,ips:list[str],data_cve: list[str] ) -> None :
        self.ip = random.choice(ips)
        self.data_cve = random.choice(data_cve)
        
    def show_log(self) -> None :
        print(f'target IP:\t"{self.ip}" Vulnerability:\t"{self.data_cve}"')
        
    def return_data_log(self) -> tuple[str,str] :
        return self.ip,self.data_cve

class CveScore:
    def score(self,*,ip: str,cve: str,data=cve_data_base) -> None:
        result_search_cve = data.get(cve,None)
        if result_search_cve:
            print(f'cve:\t"{cve}" Severity:\t"{result_search_cve}" IP:\t"{ip}"')



gen_log = GeneratorLog(ips=ips,data_cve=cve_list)
gen_log.show_log()
ip_log,cve_log = gen_log.return_data_log()

score_cve = CveScore()
score_cve.score(ip=ip_log,cve=cve_log)
'''
'''
sys_core_pross = {
    'init_process':10,
    'network_service':5,
    'filesystem_services':9,
    'security_services':9
}

user_processes = {
    'shell': 8,
    'window_manager': 7,
    'background_apps': 4,
    'user_apps': 3
}

drivers = [
    "storage_driver",
    "network_driver",
    "gpu_driver",
    "input_driver",
    "audio_driver",
]



class Core:
    def __init__(self,*,pros: dict[str,int]) -> None:
        self.processes = pros
        self.distributed_processes = None
    
    def control_prosses(self):
        def process_priorities(pros: tuple[str,int]):
            return pros[1]
        
        self.distributed_processes = sorted(self.processes.items(),key=process_priorities)[::-1]
    
    def show_prosses(self):
        print(f"""
│{self.distributed_processes=}│
              """)
    
    
    
class System:
    def __init__(self,*,drivers: list[str]):
        self.drivers =  drivers
        self.prepared_drivers = []
        
    def load_drivers(self):
        for d in self.drivers:
            self.prepared_drivers.append(d)
            
    def init_system(self):
        pross_sys = Core(pros=sys_core_pross)
        pross_user = Core(pros=user_processes) 

        pross_sys.control_prosses()
        pross_sys.show_prosses()

        pross_user.control_prosses()
        pross_user.show_prosses()
        
    
sys = System(drivers=drivers)
sys.load_drivers()
sys.init_system()
'''





# ░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒
# █▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓
# ░▒▓█░▒▓█░▒▓█░         НАСЛЕДОВАНИЕ И СПЕЦИАЛЬНЫЕ МЕТОДЫ        ░█▓▒░█▓▒░█▓▒░█▓
# █▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓▒░█▓
# ░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒▓█░▒

# ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ [ ЗНАКОМСТВО С НАСЛЕДОВАНИЕМ ] ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀

"""
class ServirTelnet:
    def __init__(self) -> None:
        self.set_servis(23)
        print(f'{self.servis=}')
        
    def set_servis(self,s: str) -> None:
        self.servis = s
        
    def show_servis(self):
        print(f"{self.__class__.__name__ =}  {self.servis=}")
        
        
class ServirTelnetAlt(ServirTelnet):
    def __init__(self):
        self.set_servis(933)
        print(f"{self.__class__.__name__ =}  {self.servis=}")
        

servir_telnet = ServirTelnet()
servir_telnet.set_servis(23)
servir_telnet.show_servis()
print('/\\'*64)
servir_telnet_alt = ServirTelnetAlt()
servir_telnet_alt.set_servis(933)
servir_telnet_alt.show_servis()
"""


'''
class BaseScan:
    def __init__(self):
        self.ports = [445,139,3389,137,135]
        self.ip = '93.184.206.32'
        
    def show_self(self):
        print(self.ip)
        print(self.ports)
        
class Fullscan(BaseScan):
    pass

        
scan_base = BaseScan()
scan_base.show_self()

scan_full = Fullscan()
scan_full.show_self()
'''

# ╳◈╳◈╳◈╳◈╳◈╳◈╳◈╳◈╳◈╳ [ МНОГОКРАТНОЕ НАСЛЕДОВАНИЕ ] ╳◈╳◈╳◈╳◈╳◈╳◈╳◈╳◈╳◈╳◈╳◈╳◈╳◈
"""
class ServirOne:
    port = (80,)
    def show_port(self):
        print(f'ServirOne:\t[{self.port}]')
        
class ServirTwo(ServirOne):
    def show_port(self):
        print(f'ServirTwo:\t[{self.port}]')
        
class ServirThree(ServirTwo):
    def show_port(self):
        print(f'ServirThree:\t[{self.port}]')
        
        
server_1 = ServirOne()
server_2 = ServirTwo()
server_3 = ServirThree()

server_1.show_port()
server_2.show_port()
server_3.show_port()
"""

'''
class WindowsXp:
    api = 'Win32'
    def show(self):
        print(f'windows XP:\t{self.api}')
        
class Windows7(WindowsXp):
     api = 'Win64'
     def show(self):
        print(f'Windows7:\t{self.api}')
        
class Windows10(Windows7):
     def show(self):
        print(f'Windows10:\t{self.api}')
        
win_xp = WindowsXp()
win_7 = Windows7()
win_10 = Windows10()

win_xp.show(); win_7.show(); win_10.show()



'''

'''
class BasedScan:
    def based_scan(self):
        print('IP:"93.209.135.43"\tport:23\ttelnet')
        
class DeepScan(BasedScan):
    def deep_scan(self):
        print('os:"LINUX"\tCVE:None')
        
        
scan = DeepScan()
scan.based_scan()
scan.deep_scan()
''' 

# ╠═╬═╬═╬═╬═╬═╬═╬═╬═╣ [ МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ ] ╠╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╣
    
""" 
class Darwin:
    def show_kernel(self) -> None:
        print('kernel:\t\tDarwin')
        
class FreeBSD:
    def show_userland(self) -> None:
        print('userland:\tFreeBSD')
        
class Unix:
    def show_architecture(self) -> None:
        print('architecture:\tUnix')
        

class MacOS(Unix,Darwin,FreeBSD) :
    pass


mak_os = MacOS()
mak_os.show_kernel()
mak_os.show_architecture()
mak_os.show_userland()
"""


'''
class Gnu:
    def show_tools(self):
        print('tools:\tGNU')
        
class Linux:
    def show_core(self):
        print('core:\tLINUX')
        
class Debian:
    def show_base(self):
        print('base:\tDebian')
        

class Gnome:
     def show_desktop_environment(self):
        print('desktop_environment:\tGNOME')
    
    
class Ubuntu(Linux,Gnu,Debian,Gnome):
    def chow_distro(self):
        print('distro:\tUbuntu')


ubuntu = Ubuntu()
ubuntu.chow_distro()
ubuntu.show_base()
ubuntu.show_tools()
ubuntu.show_core()
'''
   
    
'''
class BasedScan:
    def based_scan(self):
        print('IP:"93.209.135.43"\tport:23\ttelnet')
        
class DeepScan():
    def deep_scan(self):
        print('os:"LINUX"\tCVE:None')
        
class BanerScan():
    def baner_scan(self):
        print('Authorized access only!')
        
class FullScan(BasedScan,DeepScan,BanerScan):
    pass
        
        
scan = FullScan()
scan.based_scan()
scan.deep_scan()
scan.baner_scan()

'''

# █▌▐█▌▐█▌▐█▌▐█ [ ПЕРЕОПРЕДЕЛЕНИЕ МЕТОДОВ ПРИ НАСЛЕДОВАНИИ ] ▐█▌▐█▌▐█▌▐█▌▐█▌▐█▌▐█

"""
class BSD:
    os = 'BSD'
    def __init__(self,*,char: str):
        print('Конструктор\t№1:\t"BSD"')
        self.character_os = char
        print('характер\tсоздан')
        self.show()
        
    def show(self):
        print(f'Метод\t№1')
        print(f'Класс:\t{self.__class__.__name__=}')
        print(f'Ос класса:\t{self.__class__.os=}')
        print(f'Поле характера:\t{self.character_os=}')
        
        
class FreeBSD(BSD):
    os = 'FreeBSD'
    
    
class GhostBSD(FreeBSD):
    def __init__(self,*,char,txt):
        print('Конструктор\t№2:\t"GhostBSD"')
        self.character_os = char
        self.name = txt
        print('Новый\tобьект')
        self.show()
        
    def show(self):
        print(f'Метод\t№2')
        print(f'Класс:\t{self.__class__.__name__=}')
        print(f'Ос класса:\t{self.__class__.os=}')
        print(f'Поле характера:\t{self.character_os=}')
        
        
        
        


class NomadBSD(GhostBSD):
    os = 'NomadBSD'
    
bsd = BSD(char='raw')
bsd.os = 'bsd'
bsd.show()

freebsd = FreeBSD(char='network')
ghostbsd = GhostBSD(char='gui',txt=1)
nomadbsd = NomadBSD(char='gui',txt=2)
"""

'''
class Windows2000Server:
    max_ram = '4gb'
    def __init__(self,*,norm_ver: str):
        print(f'{self.__class__.__name__}')  
        self.client_system = norm_ver
        
    def show(self):
        print(f'максиально видимое озу:\t{self.__class__.max_ram=}')
        print(f'обычная версия:\t{self.client_system=}')

class WindowsServer2003R2(Windows2000Server):
    max_ram = '32gb'
    
    
class WindowsServer2008(WindowsServer2003R2):
    max_ram = '2TB' 
    def __init__(self,*,norm_ver: str,arch: int):
        print('Windows Server 2008')  
        self.client_system = norm_ver
        self.architecture = arch
        
    def show(self):
        print(f'максиально видимое озу:\t{self.__class__.max_ram=}')
        print(f'обычная версия:\t{self.client_system=}')
        print(f'архитектура:\t{self.architecture=}')
        
class WindowsComputeClusterServer2003(WindowsServer2003R2):
    pass
def main() -> None:
    print('=='*42)
    
    win_2000 = Windows2000Server(norm_ver='xp')
    win_2000.show()

    print('=='*42)

    win_2003_r2 = WindowsServer2003R2(norm_ver='Windows XP Professional x64 Edition')
    win_2003_r2.show()

    print('=='*42)

    win_2008 = WindowsServer2008(norm_ver='Windows Vista',arch=64)
    win_2008.show()

    print('=='*42)

    win_2008_super_pc = WindowsComputeClusterServer2003(norm_ver='Windows XP Professional x64 Edition')
    win_2008_super_pc.show()
    

'''
        
# [~~~~~~~~~~~~~~~~~~ [ ВИРТУАЛЬНОСТЬ МЕТОДОВ ] ~~~~~~~~~~~~~~~~~~~~~~~~~]
"""
class LogOpenSSH:
    def display_log(self):
        print(f'Метод из  LogOpenSSH')
        print(f'Поля os:\t{self.os}')
        
    def show(self):
        self.display_log()
        
class LogTelnet(LogOpenSSH):
    def display_log(self):
        print(f'Метод из LogTelnet')
        print(f'Поля port:\t{self.port}')
    
log_openssg = LogOpenSSH()
log_openssg.os = 'OpenSSH'

log_telnet = LogTelnet()
log_telnet.port = 23

log_openssg.show()
log_telnet.show()
"""

'''
class Win64:
    def display_api(self):
        print('WIN64')
        print('системы которые полностю перешли на WIN64:\t{}'.format(self.os_64))
        
    def show(self):
        self.display_api()
        
class Win128(Win64):
     def display_api(self):
        print(f'Win128')
        print(f'системы которые полностю перешли на WIN128:\t{self.os_128}')
        
win_64 = Win64()
win_64.os_64 = ['Windows 11','Windows XP Professional x64 Edition']
win_64.show()

win_128 = Win128()
win_128.os_128 = [None]
win_128.show()
''' 

#:::::::::::::::::'super()'::::::::::::::::

'''
class BSD:
    def __init__(self):
        self.arch = 'Unix'
        self.char = 'Raw'
    def start_show(self):
        self.show()
    def show(self):
        print(f'{self.char=}')
        
class OpenBSD(BSD):
    def __init__(self):
        super().__init__()
        self.name = 'OpenBSD'
        self.char = 'safe'
        
    def show(self):
        super().show()
        print(f'{self.name=}')
bsd_raw = BSD()
open_bsd = OpenBSD()
bsd_raw.start_show()   
open_bsd.start_show()  
'''
'''
class Server_10_main:
    def __init__(self,*,os: str):
        self.ip = '192.168.1.104'
        self.os = os


    def show(self):
        print(f'os:\t{self.os}\nip:\t{self.ip}')

class Server_10_alt(Server_10_main):
    def __init__(self,*,os):
        super().__init__(os=os)
        self.ip = '192.168.1.108'

        

serv = Server_10_main(os='win')
serv_alt = Server_10_alt(os='darwin')
serv.show()
serv_alt.show()
'''

class Scan:
    def __init__(self,*,ip: str):
        self.ip = ip
        self.port = 22
    def display_scan(self):
        print(f'ip:\t{self.ip}')
        print(f'port:\t{self.port}')
        self.show_result()
    def show_result(self):
        print(f'PORT:{self.port}\tOPEN\tSERVICE:SSH')

class OsScan(Scan):
    def __init__(self,*,ip):
        super().__init__(ip=ip)
        self.os = 'Gnu/Linux'

    def show_result(self):
        super().show_result()
        print(f'OS:{self.os}')

os_scan = OsScan(ip='23.56.90.13')
os_scan.display_scan()