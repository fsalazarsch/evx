import asyncio

messagebyte = '000000000000008c08010000013feb55ff74000f0ea850209a690000940000120000001e09010002000300040016014703f0001504c8000c0900730a00460b00501300464306d7440000b5000bb60007422e9f180000cd0386ce000107c700000000f10000601a46000001344800000bb84900000bb84a00000bb84c00000000024e0000000000000000cf00000000000000000100003fca'


class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, on_con_lost):
        self.message = message
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print('Data enviada: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data recibida: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('El servidor cerro la coneccion')
        self.on_con_lost.set_result(True)


async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()
    print("Ingresado")

    on_con_lost = loop.create_future()
    message = str(bytes.fromhex(messagebyte))

    transport, protocol = await loop.create_connection(
        lambda: EchoClientProtocol(message, on_con_lost),
        '127.0.0.1', 8888)

    #protocol.data_received(data)
    
    # Wait until the protocol signals that the connection
    # is lost and close the transport.
    try:
        await on_con_lost
    except KeyboardInterrupt:
        pass
    finally:
        print('Desconectado')
        transport.close()


asyncio.run(main())
