import os
from dynaconf import FlaskDynaconf

PATH_CURRENT = os.path.dirname(os.path.abspath(__file__))

def configure(app):
    # O app que irá chamar essa função
    # Delega para o dynaconf carregar as configurações do toml settings
    FlaskDynaconf(app, extensions_list="EXTENSIONS", root_path=PATH_CURRENT)
