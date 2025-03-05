#Servidor sincrono
from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    time.sleep(20)
    return {'hello': 'world'}

"""
Fazendo duas requisições com o post man ao mesmo 
tempo levará no total aproximadamente 40 seguntos para processar

O servidor não é assincrono
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=False)