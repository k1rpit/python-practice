cve_severity: dict[str:float] = {
    "CVE-2017-0144": 8.1,
    "CVE-2014-0160": 7.5,
    "CVE-2021-41773": 7.5,
    "CVE-2021-44228": 10.0,
    "CVE-2015-3306": 10.0,
    "CVE-2024-6387": 8.1,
    "CVE-2026-24061": 9.8,
    "CVE-2020-9272": 5.3,
    "CVE-2015-1419": 5.0,
    "CVE-2023-4863": 8.8,
    "CVE-2022-22965": 9.8,
    "CVE-2018-15473": 5.3,
    "CVE-2016-2183": 5.3,
    "CVE-2019-11043": 9.8,
    "CVE-2011-4109": 3.7,
}


cerver_one: dict[str:str] = {
    'ip':'20.104.0.106',
    'vulnerability':'CVE-2011-4109'
}


cerver_two: dict[str:str] = {
    'ip':'40.14.10.16',
    'vulnerability':'CVE-2021-44228'
}


cerver_three: dict[str:str] = {
    'ip':'3.10.17.0',
    'vulnerability':'CVE-2017-0144'
}

def check_level_danger_CVE(**server):
    cve = server['vulnerability']
    if cve_severity.get(cve,0.0) >= 7.0:
        print(f'внимания на сервере:\t{server["ip"]}\tнайдена узвимость:\t{cve=}\tс отценкой более 7.0')
    else:
         print(f'внимания на сервере:\t{server["ip"]}\tнайдена узвимость:\t{cve=}\tс отценкой менее 7.0')
check_level_danger_CVE(**cerver_one)