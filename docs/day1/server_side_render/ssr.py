
# 1 - carregar os dados
dados = [
    {'nome': 'joao', 'idade': 22},
    {'nome': 'marcos', 'idade': 10},
]
# 2 - Processar 
template = """"\
<html>
    <head>
        <title>Primeira pagina</title>
    </head>
    <body>
        <ul>
            <li>Nome: {dados[nome]} </li>
            <li>Idade: {dados[idade]} </li>
        </ul>
    </body>
</html>
"""
# 3 - renderizar o html
for item in dados:
    print(template.format(dados=item))