#!/usr/bin/env python

import sys
from modules.CommandHandler import CommandHandler

class Main:
    def __init__(self):
        self.command_handler = CommandHandler()

    def run(self):
        self.command_handler.handle(user_input=sys.argv)

def main():
    app = Main()
    app.run()

if __name__ == "__main__":
    main()