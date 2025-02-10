import socket

"receber pacotes de dados e enviar respostas"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 8080)) # servidor http porta 8080 -servidor local

# Quantidade de conexoes que serão enfileiradas pelo protolo TCP até que o servidor realize outro passo
server.listen() # numero de conexoes - escutar conexoes

# pegar a conexao do cliente
try:
    while True:
        # Aceita a conexao do cliente, return endereco do cliente 
        # e file descriptor(usado para receber e enviar dados para o cliente)  
        client, address = server.accept()
        # Sempre realizar o oposto do cliente - recv e send ou send e recv
        #Pegando um request
        data = client.recv(5000).decode() # receber dados do cliente
        print(f'{data=}')
        # Response - enviar uma resposta para o cliente 
        # Começando pelo cabeçalho
        with open('/home/nkk/Área de trabalho/projetos/python-web-api/docs/day1/first_page/index.html') as file:
            response = file.read()
        client.sendall(
        f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{response}".encode()
        )
        client.shutdown(socket.SHUT_WR) # fechar a conexao com o cliente
        
except Exception as e:
    print(f'Error: {e}')
    raise server.close() # fechar a conexao com o servidor - liberar a porta

