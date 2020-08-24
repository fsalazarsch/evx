import asyncio, crcmod


class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        crc16_func = crcmod.predefined.mkPredefinedCrcFun("crc-16")
        
        crc16_res = crc16_func( message[-4: -1].encode('utf-8'))
        crc16_res2 = crc16_func( message[-4].encode('utf-8'))
        
        #CRC-16 is 4 bytes, but first two are zeroes and last two are CRC-16 calculated for [codec id, number of data 2]
        

        if( str(hex(crc16_res)) ==  '00'+str(crc16_func('08'.encode('utf-8')))+str(hex(crc16_res2)) ):
            print("Chequeado")
        
        print('Send: {!r}'.format(message))
        self.transport.write(data)

        #print('Close the client socket')
        #self.transport.close()


async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        '127.0.0.1', 8888)




    async with server:
        await server.serve_forever()


asyncio.run(main())
