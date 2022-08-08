#!/usr/bin/python3
'''
module = console
contains the entry point of the command interpreter'''


import cmd
from models.base_model import BaseModel
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    '''
    class for command
    '''

    prompt: str = "(hbnb) "

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def help_quit(self):
        '''Prints out how to use the quit command'''
        print("Quit command to exit or quit the program")

    def help_EOF(self):
        '''Prints out how to use the EOF command'''
        print("Exits or quit the program with the EOF command")

    def do_EOF(self, line):
        '''exit the program'''
        return True

    def emptyline(self):
        '''an empty line + ENTER shouldn't execute anything'''
        return cmd.Cmd.emptyline(self)  # or Super().emptyline()
