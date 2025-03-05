import asyncio

async def say_hello(name, time):
    print(f"{name} iniciando...")
    await asyncio.sleep(time)
    print(f"{name} finalizando...")

async def main():
    await say_hello('task 3' , 3) # Atuacao sincrona
    # espera a primeira corrotina ser concluida para passar para a proxima
    # Corrotinas sendo chamadas de forma concorrente
    await asyncio.gather( # Atuacao assincrona
        say_hello("Tarefa 1", 2),
        say_hello("Tarefa 2", 1),
    )

asyncio.run(main())  # Executa todas ao mesmo tempo