import asyncio
from django.http import HttpResponse


async def contador():
    for i in range(1, 6):
        print(i)
        await asyncio.sleep(1)

    print('Contador Finalizado com sucesso')

async def hello_world(request):
    asyncio.create_task(contador())
    return HttpResponse("Hello World")
