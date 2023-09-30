def handle_request(message) -> str:
    p_message = message.lower()

    if (p_message == "Hello"):
        return "Hi, how is it going"

    if (p_message == "Help"):
        return "How can I help you"    
