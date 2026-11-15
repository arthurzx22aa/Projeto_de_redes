import socket
import threading
from aplications import calc


HOST = "127.0.0.1"
PORT = 60001


def Service(parts) :
    if len(parts)!= 4:
        return "erro no formato"

    else:
        num1 = float(parts[1])
        num2 = float(parts[3])
        operation = parts[2]
        result = calc(num1, num2, operation)
        return f"RESULT {result}"


def Decode(mensage)  :

    parts= mensage.decode(errors="replace").split()

    if not parts:
        return "erro requisicao vazia"
    
    if parts[0] == "CALC":
        return Service(parts)
    else:
        return "erro comando desconhecido"

def Handle(sock, data, addr):
    sock.sendto((Decode(data) + "\n").encode(), addr)

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print(f"Servidor de serviço UDP em {HOST}:{PORT}")
    while True:
        data, addr = server.recvfrom(1024)
        
        if data:
            threading.Thread(target=Handle, args=(server, data, addr)).start()
        else:
            print("nenhum dado recebido de", addr)

if __name__ == "__main__":
    main()