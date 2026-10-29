import platform
import json

data_you_pc_and_os = {}
json_bool = bool(1)

def func_data_you_pc_and_os_full(*,json_ :bool,**kwargs):
    system = platform.system()
    if 'Linux' in system:
        data_os = platform.freedesktop_os_release()
    elif 'Windows' in system:
        data_os = platform.win32_ver()
    elif 'Darwin' in system:
        data_os = platform.mac_ver()
    
    data_temp = {
        'architecture':platform.architecture(),'type_machine':platform.machine(),
        'name_pc_in_network':platform.node(),'platform':platform.platform(),
        'name_processor':platform.processor(),'system_release':platform.release(),
        'system':system, 'os_data':data_os
    }
    if json_ == True:
        json_f=json.dumps(data_temp,indent=4, ensure_ascii=False)
        with open('data_os_pc.json','w') as f:
            f.write(json_f)

    return data_temp | kwargs
print(func_data_you_pc_and_os_full(json_=json_bool,**data_you_pc_and_os))


