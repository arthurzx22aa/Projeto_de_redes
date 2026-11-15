import socket
import threading
from aplications import calc


HOST = "127.0.0.1"
PORT = 60002


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

def Handle(sock, addr):

    data = sock.recv(1024)

    if data:
        sock.sendall((Decode(data) + "\n").encode())
    else:
        print("nenhum dado recebido de", addr)
    sock.close()

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    
    print(f"Servidor de serviço TCP em {HOST}:{PORT}")

    while True:
        
        socket_client, addr = server.accept()
        threading.Thread(target=Handle, args=(socket_client, addr)).start()


if __name__ == "__main__":
    main()