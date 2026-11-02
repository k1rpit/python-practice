import requests
import json

ip_data = {}

ip = input('введие айпи/input ip>')
def check_valid_ip(*,ip: str) -> bool:
    is_bool_valid_ip = True
    if ip and '.' in ip and 8 <=len(ip) <= 15 :
        list_ip_int = ip.rsplit('.')
        for i in list_ip_int :
            if int(i) > 255:
                is_bool_valid_ip = False
                break
    else:
        is_bool_valid_ip = False
    return is_bool_valid_ip
def main(*,bool_ip=check_valid_ip(ip=ip),data=ip_data):
    if bool_ip:
        url = f'http://ip-api.com/json/{ip}'
        response_url = requests.get(url,params={'fields':'status,message,country,city',},timeout=3)
        raw_data_ip = response_url.json()

        data = ip_data | raw_data_ip
        ip_data_json = json.dumps(data)
        with open('data-ip.json','w') as f:
            f.write(ip_data_json)
    else:
        print('invalid ip!')

if __name__ == '__main__':
    main()
