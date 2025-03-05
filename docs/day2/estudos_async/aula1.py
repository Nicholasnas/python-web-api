import asyncio
"""
async def - cria um corrotina
await - pausa a execução da corrotina atual e chama outra corrotina disponivel
asyncio.run() - executa a corrotina principal
"""

async def tarefa(nome, tempo):
    print(f"{nome} iniciando...")
    await asyncio.sleep(tempo)  # Simula I/O
    print(f"{nome} finalizando...")

async def main():
    await asyncio.gather(
        tarefa("Tarefa 1", 2),
        tarefa("Tarefa 2", 1),
        tarefa("Tarefa 3", 3)
    )

asyncio.run(main())  # Executa todas ao mesmo tempo
