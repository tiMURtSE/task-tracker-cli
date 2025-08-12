import re
from modules.Storage import Storage

class CommandHandler:
    def __init__(self):
        self.storage = Storage()

    def _check_description(self, rest: list[str]):
        pattern = r'^"[^"]+"$'

        return bool(re.match(pattern, " ".join(rest)))

    def handle(self, command: str):
        splitted_command = command.split(" ")
        command, *rest = splitted_command

        match command:
            case "add":
                if self._check_description(rest):
                    description = " ".join(rest)
                    self.storage.add_new_task(description)
                    
                    print("*выполняется команда add*")
                else:
                    raise Exception(f"Лишний аргумент в введенной команде: rest: {rest}.")
            case "delete":
                if len(rest) == 1 and isinstance(int(rest[0]), int):
                    id = int(rest[0])

                    self.storage.delete_task(id)
                    print("*выполняется команда delete*")
                else:
                    raise Exception("Что-то не так в команда 'delete'.")
            case "list":
                if len(rest) == 0:
                    self.storage.list_tasks()
                elif len(rest) == 1 and rest[0] in ["todo", "in-progress", "done"]:
                    status = rest[0]
                    self.storage.list_tasks(status)
                else:
                    raise Exception("Что-то не так в команда 'list'.")
            case "update":
                if isinstance(int(rest[0]), int) and self._check_description(rest[1:]):
                    id = int(rest[0])
                    description = " ".join(rest[1:])

                    self.storage.update_task(id, description)
                else:
                    raise Exception("Что-то не так в команда 'update'.")
            case "mark-in-progress":
                if len(rest) == 1 and isinstance(int(rest[0]), int):
                     id = int(rest[0])

                     self.storage.update_status(id, "in-progress")
                else:
                    raise Exception("Что-то не так в команда 'mark-in-progress'.")
            case "mark-done":
                if len(rest) == 1 and isinstance(int(rest[0]), int):
                     id = int(rest[0])

                     self.storage.update_status(id, "done")
                else:
                    raise Exception("Что-то не так в команда 'mark-done'.")
            case _:
                print("Ошибка при вводе команды.")