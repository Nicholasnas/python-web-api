from flask import Flask
from blog.config import configure

def create_app():
    app = Flask(__name__)
    # Delega a função de configuração para outro lugar
    configure(app) # nosso app que importa a factory
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
