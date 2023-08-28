import socket

SERVER = "127.0.0.1"
PORT = 50000

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((SERVER, PORT))

while True:
    print("Exemplo de operação : 4 + 5")

    inp = input()
    if inp == "Sair":
        break

    client.send(inp.encode())
 
    resposta = client.recv(1024)
    print("O resultado é  "+resposta.decode())
    print("Digite Sair para finalizar")
 
client.close()