
import socket
 

LOCALHOST = "127.0.0.1"
PORT = 50000

server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print('Aguardando Conexão cliente')

conexaocliente, clienteendereco = server.accept()

print("Conexão estabelecida em :", clienteendereco)
msg = ''

while True:
    dados = conexaocliente.recv(1024)
    msg = dados.decode()
    if msg == 'vazia':
        print("Conexão finalizada")
        break
 
    print("Operação Recebida com Sucesso")
    result = 0
    fluxo_operacoes = msg.split()
    oprnd1 = fluxo_operacoes[0]
    operation = fluxo_operacoes[1]
    oprnd2 = fluxo_operacoes [2]
 
    num1 = int(oprnd1)
    num2 = int(oprnd2)
   
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
 
        result = num1 - num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "*":
        result = num1 * num2
 
    print("Realizar Envio do resultado para o cliente")
    
    output = str(result)
    conexaocliente.send(output.encode())
conexaocliente.close()