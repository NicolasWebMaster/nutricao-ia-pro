class ConversationMemory:

    def __init__(self):

        self.messages = []


    def add_user_message(self, message):

        self.messages.append(
            f"Usuário: {message}"
        )


    def add_ai_message(self, message):

        self.messages.append(
            f"Assistente: {message}"
        )


    def get_history(self):

        return "\n".join(
            self.messages[-8:]
        )
