import asyncio
import EchoClientProtocol
import EchoServerProtocol


async def main():
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()
    message = 'Hello World!'

    transport, protocol = await loop.create_connection(
        lambda: EchoClientProtocol(message, on_con_lost),
        '127.0.0.1', 8888)

    try:
        await on_con_lost
    finally:
        transport.close()

    #Ecibido    
    loop = asyncio.get_running_loop()    
    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()


asyncio.run(main())
