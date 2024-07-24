import asyncio
import random

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования. Сила атлета: {power}.')
    for i in range(1, 6):
        await asyncio.sleep(5 / power)
        print(f'Силач {name} поднял {i}-й шар.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    names = ['Joe', 'Chandler', 'Ross']
    tasks = []
    for name in names:
        tasks.append(asyncio.create_task(start_strongman(name, random.choice([1,2,3,4,5]))))
    for task in tasks:
        await task

asyncio.run(start_tournament())