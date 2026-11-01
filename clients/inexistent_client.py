import socket
import time

NAME_SERVER = ("127.0.0.1", 60000)
SERVICE = "time"


def Get(service):
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


def main():
    mens, time_name_server = Get(SERVICE)

    if mens.startswith("FOUND"):
        _, ip, port = mens.split()
        #não existe serviço nesse caso.
    else:
        print(mens)

    print(f"Tempo gasto para servidor de nomes: {time_name_server:.5f}\n")

if __name__ == "__main__":
    main()