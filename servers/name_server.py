import socket
import threading


HOST = "127.0.0.1"
PORT = 60000

table = {"calculator_udp":(HOST, 60001), "calculator_tcp":(HOST, 60002),"date_udp":(HOST, 60003), "date_tcp": (HOST, 60004)}

def Get(mensage) :
    if len(mensage)!= 2:
        return "erro no formato"
    
    info= table.get(mensage[1])

    if info is None:
        return "erro servico nao encontrado"
    return f"FOUND {info[0]} {info[1]}"

def Decode(mensage)  :
    parts= mensage.decode(errors="replace").split()

    if not parts:
        return "erro requisicao vazia"
    
    if parts[0] == "GET":
        return Get(parts)
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