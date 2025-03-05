# callable - function() or obj() or lambda()
# environ, callback(start_response) -> argumentos 
# retornar um iteravel, por baixo ainda esta o cgi

def application(environ, start_response):
    """
    environ: as variaveis do request estará aqui
    Fazer oque quiser com o request
    """
    # print(environ)
    # montar o response
    status = "200 OK"
    headers = [('Content-type', 'text/html')]   
    body = b"<strong> Hello world !!</strong>" # formato de bytes
    start_response(status, headers) # enviando um sinal
    return [body] # para o cgi iterar

if __name__ == "__main__":   
    from wsgiref.simple_server import make_server
    # usar uma factory para instanciar o server
    # qual aplicação será utilizada pelo servidor
    # Criando e iniciando o servidor
    server = make_server('0.0.0.0', 8000, application)
    #mantem o servidor rodando
    server.serve_forever()
    
     



