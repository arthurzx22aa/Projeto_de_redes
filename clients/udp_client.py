import socket
import time

NAME_SERVER = ("127.0.0.1", 60000)
SERVICE = "calculator_udp"


def GetNameServer(service):
    request = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    request.settimeout(2)

    start = time.perf_counter()

    for i in range(3):
        request.sendto(f"GET {service}".encode(), NAME_SERVER)

        try:
            mens= request.recvfrom(1024)[0].decode()
            break
        
        except socket.timeout:
                pass

    end = time.perf_counter()
    time_expend= end - start
    request.close()
    
    return mens, time_expend


def GetUDPServer(ip, port, service):
    request = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    request.settimeout(2)

    start = time.perf_counter()

    for i in range(3):
        request.sendto(f"{service}".encode(), (ip, port))

        try:
            mens= request.recvfrom(1024)[0].decode()
            break
        
        except socket.timeout:
                pass

    end = time.perf_counter()
    time_expend= end - start
    request.close()
    
    return mens, time_expend
     

def main():
    mens, time_name_server = GetNameServer(SERVICE)
    if mens.startswith("FOUND"):

        _, ip, port = mens.split()

        calcular = "CALC 5 * 3"
        mens, time_udp_server = GetUDPServer(ip, int(port), calcular)
        print(f"Resposta do servidor udp: {mens}")

    else:
        print(mens)


    total = time_name_server+ time_udp_server

    print(f"Tempo gasto para servidor de nomes: {time_name_server:.5f}\n")
    print(f"Tempo gasto para servidor de udp: {time_udp_server:.5f}\n")
    print(f"Tempo gasto total: {total:.5f}\n")


if __name__ == "__main__":
    main()