# базовое форматирования и методы в принт а также инпут

#print('1','2',sep='|',end=' ')
#print('3','4')
#print(5)

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
