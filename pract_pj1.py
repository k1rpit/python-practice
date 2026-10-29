access_rights = {
    "ufw":664,
    "fail2ban":755,
    "wireguard":755,
    "firefox": 700,
    'uklown':777,
    'dovecot':600,
    'ls':755,
    'q$j+1=~':777
}


def func_check_ccess_rights(**kwargs):
    dangerous_list = []
    is_there_any_danger = False
    for key,value in access_rights.items():
        if value == 777:
            dangerous_list.append(key)
            access_rights[key] = 000
            is_there_any_danger = True
    return dangerous_list,is_there_any_danger
unclear_list,is_there_any_danger =   func_check_ccess_rights(**access_rights)

def func_log_output(*,bool_danger: bool,list_danger: list):
    if bool_danger:
        return f'в правах процессов были найдены уязвимоати\t{list_danger} они были отпрвелены на карантин'
    else:
        return f'все чисто'
print(func_log_output(bool_danger=is_there_any_danger,list_danger=unclear_list))
