import asyncio
import zmq
import zmq.asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def chat_client():
    ctx = zmq.asyncio.Context()
    socket = ctx.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # Pretend this is me sending WhatsApp messages
    messages = ["Hello Friend ", "How are you?", "Bye "]

    for msg in messages:
        print(f" You: {msg}")
        await socket.send_string(msg)

        # Wait for reply
        reply = await socket.recv_string()
        print(f"{reply}")

        await asyncio.sleep(1)  # small delay for realism


if __name__ == "__main__":
    asyncio.run(chat_client())
