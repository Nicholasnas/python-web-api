import asyncio
import httpx 


async def fetch_get(client:any, pokemon_name:str):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    # Estou esperando a resposta da requisição - I/O 
    response = await client.get(url)
    data = response.json()
    name = data['name']
    hability = data['moves'][0]['move']
    print(f'mais um pokemon: {name} com a habilidade: {hability}')
    print('-------------------')


async def main():
    async with httpx.AsyncClient() as client:
        await asyncio.gather(
            fetch_get(client, 'pikachu'),
            fetch_get(client, 'charmander'),
            fetch_get(client, 'bulbasaur'),
        )
        await fetch_get(client, 'ditto')


asyncio.run(main())