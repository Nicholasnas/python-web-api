"""
Por baixo do framework HTTP está o protocolo TCP/IP
Servidor esta em uma rede e o cliente esta em outra rede
o socket estará aberto para escutar as requisicoes
trocar mensagens em conexoes TCP 
Consumir um site atraves do python
"""""

import socket

# Criando um socket - formato de  e tipo de socket que será aberto(stream de texto)
# AF_INET - formato de endereço de IP
# SOCK_STREAM - tipo de socket que será aberto- protocolo tcp na camada de transporte
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(('localhost', 8080)) # cliente hhtp porta 80 - tcp 22

# Enviar uma mensagem para o servidor - GET é um comando para pegar um arquivo e versao do http
cmd = "GET http://localhost/index.html HTTP/1.0 \r\n\r\n".encode()
cliente.send(cmd) # enviar a mensagem para o servidor

while True:
    data = cliente.recv(512) # receber a resposta do servidor 512 bytes
    if len(data) < 1:
        break
    print(data.decode(), end='') # imprimir a resposta do servidor em utf-8 
cliente.close() # fechar uma conexão com o servidor
 
