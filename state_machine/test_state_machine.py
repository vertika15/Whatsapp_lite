from state_machine import WhatsAppLiteStateMachine

if __name__ == "__main__":
    app = WhatsAppLiteStateMachine()

    app.connect()  # Offline -Connecting
    app.connection_successful()  # Connecting - Online
    app.start_chat()  # Online - Typing
    app.disconnect()  # Any -> Offline
