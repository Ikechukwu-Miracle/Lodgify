#!/usr/bin/python3
"""Contains a command line interpreter class"""
import cmd
import re
import shlex
import sys
from typing import List
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class LodgifyCommand(cmd.Cmd):
    """Class that initializes a cmd interpreter"""
    prompt = "(lodgify) "
    classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
        ]
    objects = storage.all()


    def do_quit(self, line: str) -> bool:
        """command to exit the cmd prompt"""
        return True

    def default(self, line: str) -> None:
        return super().default(line)

    def do_EOF(self, line: str) -> bool:
        """Exits interpreter when user types (ctrl + d)"""
        if sys.stdin.isatty():
            print()
        print()

        return True

    def emptyline(self) -> bool:
        pass

    def precmd(self, line: str) -> str:
        """Defines instructions to execute before interpretation of line"""
        if not line:
            return "\n"

        pattern = re.compile(r"(\w+)\.(\w+)\((.*)\)")
        matchList = pattern.findall(line)
        if not matchList:
            return super().precmd(line)

        args_tup = matchList[0]
        if not args_tup[2]:
            if args_tup[1] == "count":
                count(args_tup[0])
                return "\n"
            form = "{} {}".format(args_tup[1], args_tup[0])
            return form

        passed_args = args_tup[2].split(", ")
        stringVal = ""
        for arg in passed_args:
            arg = re.sub("[\"\']", "", arg)
            stringVal += (arg + " ")

        form = "{} {} {}".format(args_tup[1], args_tup[0], stringVal)
        return form

    def do_create(self, line: str) -> None:
        """Creates an instance of the given class and saves it to file"""
        if not argsCheck(line):
            return

        obj = eval(line)()
        storage.save()
        print(obj.id)

    def do_show(self, line):
        """Prints the str representarion of an instance
        based on the class name and id
        Usage: show <classname> <id>
        """
        if not argsCheck(line, class_id=True):
            return
        args = line.split()
        key = "{}.{}".format(args[0], args[1])
        print(LodgifyCommand.objects[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Usage: destroy <classname> <id>
        """
        if not argsCheck(line, class_id=True):
            return
        args = line.split()
        key = "{}.{}".format(args[0], args[1])
        del(LodgifyCommand.objects[key])
        storage.save()

    def do_all(self, line):
        """Prints a list of all the instances of a given class"""
        if not line:
            print(["{}".format(str(v)) for _, v in LodgifyCommand.objects.items()])
            return
        if line  and line not in LodgifyCommand.classes:
            print("** class doesn't exist **")
            return

        print(["{}".format(str(v)) for _, v in
                       LodgifyCommand.objects.items() if type(v).__name__ == line])

    def do_update(self, line):
        """Updates an instance by adding an attribute and value
        Usage: update <classname> <id> <attribute name> <value>"""
        if argsCheck(line, class_id=True):
            try:
                args = shlex.split(line)
            except ValueError as e:
                print("** syntax error **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            if args[2] in ["id", "created_at", "update_at"]:
                print("** cannot update this attribute **")
                return
            key = "{}.{}".format(args[0], args[1])
            obj = LodgifyCommand.objects
            attr = args[2]
            value = args[3]

            if hasattr(obj, attr):
                current_type = type(getattr(obj, attr))
                try:
                    value = current_type(value)
                except ValueError:
                    print("** invalid value type **")
                    return
            else:
                try:
                    if value.isdigit():
                        value = int(value)
                    elif value.replace('.', '', 1).isdigit():
                        value = float(value)
                    else:
                        value = str(value)
                except ValueError:
                    value = str(value)
                setattr(obj[key], attr, value)
                storage.save()
                return
        else:
            return

def argsCheck(args, class_id=False):
    """Validates arguments passed to the command line"""
    args = args.split()
    if not args:
        print("** class name missing **")
        return False
    if args[0] not in LodgifyCommand.classes:
        print("** class doesn't exist **")
        return False
    if len(args) == 1 and class_id:
        print("** instance id missing **")
        return False
    if len(args) == 2:
        key = "{}.{}".format(args[0], args[1])
        if key not in LodgifyCommand.objects:
            print("** instance not found **")
            return False

    return True

def count(obj_cls):
    """Counts all the instancess of a class"""
    result = 0
    for k, v in LodgifyCommand.objects.items():
        if type(v).__name__ == obj_cls:
            result += 1

    print(result)


if __name__ == "__main__":
    LodgifyCommand().cmdloop()