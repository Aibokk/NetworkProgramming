import asyncio

async def say(what, when):
    await asyncio.sleep(when)
    print(what)

async def stop_after(loop, when):
    await asyncio.sleep(when)
    loop.stop()


loop = asyncio.get_event_loop()
loop.create_task(say('First', 2))
loop.create_task(say('Second', 1))
loop.create_task(say('Third', 4))
loop.create_task(stop_after(loop, 3))

loop.run_forever()
loop.close()