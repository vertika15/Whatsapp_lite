from enum import Enum, auto

# Define possible states
class ChatState(Enum):
    OFFLINE = auto()
    CONNECTING = auto()
    ONLINE = auto()
    CHATTING = auto()

class WhatsAppLiteStateMachine:
    def __init__(self):
        self.state = ChatState.OFFLINE

    def connect(self):
        if self.state == ChatState.OFFLINE:
            print("Connecting to server...")
            self.state = ChatState.CONNECTING
        elif self.state == ChatState.CONNECTING:
            print("Already connecting...")
        else:
            print("Invalid connect() call in state:", self.state)

    def connection_successful(self):
        if self.state == ChatState.CONNECTING:
            print("Connected! You are online now.")
            self.state = ChatState.ONLINE
        else:
            print("Cannot mark connection successful in state:", self.state)

    def start_chat(self):
        if self.state == ChatState.ONLINE:
            print("Starting chat...")
            self.state = ChatState.CHATTING
        else:
            print("Can't start chat in state:", self.state)

    def disconnect(self):
        print("Disconnected.")
        self.state = ChatState.OFFLINE
