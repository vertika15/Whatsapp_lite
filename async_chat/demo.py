import asyncio
import zmq
import zmq.asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def chat_server():
    ctx = zmq.asyncio.Context.instance()
    socket = ctx.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    print(" Friend: Hey! I'm online, waiting for your messages...")

    while True:
        msg = await socket.recv_string()
        print(f" Friend got your message: {msg}")

        reply = f" Friend: I received -> {msg}"
        await socket.send_string(reply)


async def chat_client():
    await asyncio.sleep(1)  # wait time
    ctx = zmq.asyncio.Context.instance()
    socket = ctx.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    messages = ["Hello Friend ", "How are you?", "Bye "]

    for msg in messages:
        print(f" You: {msg}")
        await socket.send_string(msg)

        reply = await socket.recv_string()
        print(reply)

        await asyncio.sleep(1)


async def main():
    # server and client running parallely
    server_task = asyncio.create_task(chat_server())
    client_task = asyncio.create_task(chat_client())

    await asyncio.wait([client_task], return_when=asyncio.ALL_COMPLETED)
    #canceling server so it does not wait forever
    server_task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
