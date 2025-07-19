from modules.FileHandler import FileHandler

file_handler = FileHandler()

def handle_user_input(user_input: str):
    user_input = user_input.strip()
    command = user_input.split(" ")[0]

    file_handler.fsdf()

    print(f"Command: {command}")

def show_error(msg: str):
    if isinstance(msg, str):
        print(f"Ошибка: {msg}")
    else:
        print(f"Error 500")

user_input = input("Введите команду: ")

handle_user_input(user_input)