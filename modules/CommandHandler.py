from modules.FileHandler import FileHandler
from modules.Task import Task

class CommandHandler:
    def __init__(self):
        self.file_handler = FileHandler()

    def handle(self, command: str):
        splitted_command = command.split(" ")
        command, *rest = splitted_command

        match command:
            case "add":
                print("*выполняет команда add*")
                self.file_handler.add_new_task()
            case _:
                print("Ошибка")