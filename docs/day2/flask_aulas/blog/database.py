from flask_pymongo import PyMongo


mongo = PyMongo() # instancia do PyMongo - não inicializado

def configure(app):
    mongo.init_app(app) # inicializa o PyMongo com o app
    
    