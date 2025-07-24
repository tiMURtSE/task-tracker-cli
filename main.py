from modules.CommandHandler import CommandHandler

class Main:
    def __init__(self):
        self.command_handler = CommandHandler()

        self.user_input = input("Введите команду: ")

    def _handle_user_input(self):
        user_input = self.user_input.strip()
        self.command_handler.handle(command=user_input)

    def run(self):
        self._handle_user_input()

app = Main()
app.run()