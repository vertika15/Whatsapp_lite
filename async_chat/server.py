import asyncio
import zmq
import zmq.asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def chat_server():
    ctx = zmq.asyncio.Context()
    socket = ctx.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print(" Friend: Hey! I'm online, waiting for your messages...")

    while True:
        try:
            # wait for a message
            msg = await socket.recv_string()
            print(f" Friend got your message: {msg}")

            # friend replies back
            reply = f" Friend: I received -> {msg}"
            await socket.send_string(reply)

        except Exception as e:
            print(f" Oops, something went wrong: {e}")
            break

if __name__ == "__main__":
    asyncio.run(chat_server())
