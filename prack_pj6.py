raw_network_data = [
    {"ip": "195.23.87.12", "port": 22},
    {"ip": "84.112.4.90", "port": 993},
    {"ip": "10.0.0.145", "port": 2222},
    {"ip": "185.70.184.2", "port": 23},
    {"ip": "172.16.254.8", "port": 2222},
    {"ip": "93.184.216.34", "port": 22},
    {"ip": "45.134.22.19", "port": 23},
    {"ip": "192.168.1.50", "port": 993},
    {"ip": "77.88.55.88", "port": 22},
    {"ip": "5.255.255.5", "port": 2222},
    {"ip": "109.67.13.52", "port": 23},
    {"ip": "34.221.77.55", "port": 993},
    {"ip": "87.4.233.251", "port": 22},
    {"ip": "142.250.74.46", "port": 2222},
    {"ip": "193.122.101.2", "port": 23}
]


def network_gateway_blackList_port(data: list) -> bool:
    return data['port'] != 22 and data['port'] != 23 


def network_sort_ip(data: list) -> tuple:
    return len(data['ip']),len(str(data['port']))

Parsed_network_data = list(filter(network_gateway_blackList_port,raw_network_data))
Parsed_network_data = sorted(list(Parsed_network_data),key=network_sort_ip)[::-1]
print(Parsed_network_data)
