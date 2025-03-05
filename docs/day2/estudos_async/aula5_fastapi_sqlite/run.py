from sqlalchemy import MetaData, Table, Column, Integer, String
import databases
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

#Criar a conexao
DATABASE_URL = 'sqlite:///schema.db'
database = databases.Database(DATABASE_URL)

# Descrevendo tabelas - inicializando as tabelas
metadata = MetaData()
pessoa = Table(
    'people', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String)
)

# buscando as pessoas adicionadas
async def get_all_people():
    query = pessoa.select()
    result = await database.fetch_all(query)
    return result


app = FastAPI()

@app.get('/')
async def read_data():
    await database.connect() # espera conectar ao banco de dados
    pessoas = await get_all_people()
    print(pessoas)
    formatted_people = []
    for pessoa in pessoas:
        formatted_people.append(pessoa.name)
    return JSONResponse(
        content={'pessoas': formatted_people},
                 status_code=200
    )

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)

