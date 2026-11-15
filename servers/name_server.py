import socket
import threading


HOST = "127.0.0.1"
PORT = 60000

table = {"calculator_udp":(HOST, 60001), "calculator_tcp":(HOST, 60002)}
lock = threading.Lock()


def Get(mensage) :
    
    if len(mensage)!= 2:
        return "erro no formato"
    
    lock.acquire()
    info= table.get(mensage[1])
    lock.release()

    if info is None:
        return "erro servico nao encontrado"
    return f"FOUND {info[0]} {info[1]}"

def Register(mensage) :
    if len(mensage)!= 4:
        return "erro no formato"

    if not mensage[3].isdigit() or not 1024 <= int(mensage[3]) <= 65535:
        return "erro porta invalida"

    lock.acquire()
    table[mensage[1]] = (mensage[2], int(mensage[3]))
    lock.release()

    return "OK"

def Decode(mensage)  :
    parts= mensage.decode(errors="replace").split()

    if not parts:
        return "erro requisicao vazia"
    
    if parts[0] == "GET":
        return Get(parts)
    elif parts[0] == "REGISTER":
        return Register(parts)
    else:
        return "erro comando desconhecido"

def Handle(sock, data, addr):
    sock.sendto((Decode(data) + "\n").encode(), addr)

def main():

    name_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    name_server.bind((HOST, PORT))
    print(f"Servidor de nomes UDP em {HOST}:{PORT}")

    while True:
        data, addr = name_server.recvfrom(1024)

        if data:
            threading.Thread(target=Handle, args=(name_server, data, addr)).start()
        else:
            print("nenhum dado recebido de", addr)

if __name__ == "__main__":
    main()