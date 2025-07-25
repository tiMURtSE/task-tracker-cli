#!/usr/bin/env python

import sys
from modules.CommandHandler import CommandHandler

class Main:
    def __init__(self):
        self.command_handler = CommandHandler()

        if len(sys.argv) > 1:
            self.user_input = " ".join(sys.argv[1:])
        else:
            self.user_input = input("Введите команду: ")

    def _handle_user_input(self):
        user_input = self.user_input.strip()
        self.command_handler.handle(command=user_input)

    def run(self):
        self._handle_user_input()

if __name__ == "__main__":
    app = Main()
    app.run()
