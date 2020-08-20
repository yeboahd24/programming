import asyncio

'''looping through a range of numbers'''

async def cor1():
	print('cor1 start')
	for i in range(10):
		await asyncio.sleep(1.5)
		print('cor1:', i)

async def cor2():
	print('cor2 start')
	for i in range(10):
		await asyncio.sleep(1)
		print('cor2:', i)


loop = asyncio.get_event_loop()
cors = asyncio.wait([cor1(), cor2()])
loop.run_until_complete(cors)

