import socket
from time import sleep as sl
from datetime import datetime
from random import randrange
import sys

def main() -> None:
    IP = '45.33.32.156'
    
    top_ports_simple: dict[int, str] = {
    80: "HTTP",
    443: "HTTPS",
    22: "SSH",
    3389: "RDP",
    445: "SMB",
    21: "FTP",
    53: "DNS",
    23: "Telnet",
    3306: "MySQL",
    8080: "HTTP-Proxy / Alt Web"
}

    
    
    
    top_25_ports: dict[int, str] = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    111: "RPCBIND",
    135: "MSRPC",
    139: "NetBIOS-SSN",
    143: "IMAP",
    443: "HTTPS",
    445: "Microsoft-DS (SMB)",
    993: "IMAPS",
    995: "POP3S",
    1025: "NFS-or-IIS",
    1723: "PPTP",
    3306: "MySQL",
    3389: "RDP",
    5900: "VNC",
    8000: "HTTP-Alt (Django/Dev)",
    8080: "HTTP-Proxy / Apache Tomcat",
    8443: "HTTPS-Alt",
    8888: "HTTP-Alt (Jupyter/Dev)",
    9000: "PHP-FPM / SonarQube"
}

    vulnerable_ports_clean: dict[int, str] = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    69: "TFTP",
    135: "MSRPC",
    139: "NetBIOS",
    445: "SMB",
    1433: "MSSQL",
    3306: "MySQL",
    3389: "RDP",
    4444: "Metasploit Default Shell",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    9200: "Elasticsearch",
    27017: "MongoDB"
}

    remote_screen_ports: dict[int, str] = {
    5900: "VNC Default (Display :0)",
    5901: "VNC Display :1 (User 1)",
    5902: "VNC Display :2 (User 2)",
    5500: "VNC Reverse Connection (Listen Mode)",
    5631: "PCAnywhere (Old Remote Desktop)",
    6000: "X11 (Linux Graphical Display :0)",
    6001: "X11 (Linux Graphical Display :1)"
}

    def connect(*,ports: dict[int,str]) -> list[int]:
        open_ports = []
        print(f'scan IP:{IP} -- date:\t{datetime.now()}')
        for port,servis in ports.items():
            s: socket.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(0.5)
            sl(randrange(3))
            connect_attempt=s.connect_ex((IP,port))
            s.close()
            
            if connect_attempt == 0:
                    print('--'*32)
                    print(f'port\t[{port}]:OPEN;\tSERVIS:\t"{servis}"')
                    print('--'*32)
                    open_ports.append(port)
            elif connect_attempt == 110:
                    print('--'*32)
                    print(f'port\t[{port}]:Connection timed out')
                    print('--'*32)
            elif connect_attempt== 111:
                    print('--'*32)
                    print(f'port\t[{port}]:Connection refused')
                    print('--'*32)
            elif connect_attempt == 113:
                    print('--'*32)
                    print(f'port\t[{port}]:No route to host')
                    print('--'*32)
            else:
                    print('--'*32)
                    print(f'port\t[{port}]:CLOSE')
                    print('--'*32)
        print(f' end scan IP:{IP} -- {sorted(open_ports)=} ')
        return open_ports
            
            
    def banner_grabbing(*,ports: list[int]) -> None:
              for port in ports:
        
                s: socket.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.settimeout(3.0)


                result_data: int = s.connect_ex((IP,port))
                

                if result_data == 0:
                    try:
                        s.sendall(b"\r\nHELP\r\nEHLO\r\n")
                        data_baner = s.recv(1024)
                        print(f'baner port\t{port}:\f{str(data_baner.rstrip()).rstrip()}')
                    except ConnectionResetError as error:
                        print(f'PORT:{port}:\t{error}')
                    except socket.timeout as error:
                        print(f'PORT:{port}:\t{error}')
                    except Exception as error:
                        print(f'PORT:{port}:\t{error}')
                    finally:
                        s.close()
                        
                        
    result_conn=connect(ports=top_ports_simple)
    banner_grabbing(ports=result_conn)




if __name__ == "__main__":
    if sys.platform == 'linux':
        pass
    else:
        print('Warning:\tYour OS is not supported.\nThis program was not designed or tested on other operating systems.\nExecution halted.')
    main()
