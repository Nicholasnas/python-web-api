from jinja2 import Environment, FileSystemLoader

# Nao aceita templates pronto apenas string
# Ambiente- pode pegar um texto e renderizar
env = Environment(
    loader=FileSystemLoader('.') # De onde carregar os templates
) 
# criar um filtro para o template

def addhearts(text):
    return f"💓 {text} 💓"

# Adicionando ao jinja
env.filters['addhearts'] = addhearts

template = env.get_template("email.template.txt")

data = {
    "name": "Bruno",
    "products": [
        {"name": "iphone", "price": 13000.320},
        {"name": "ferrari", "price": 900000.430},
    ],
    "special_customer": True
}
print(template.render(**data)) # desempacotar passar os elementos separados



