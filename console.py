#!/usr/bin/python3
"""Module for class HBNBCommand and set the console"""
import cmd
from models.base_model import BaseModel
from models.user import User
import models


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand for the console"""
    prompt = '(hbnb) '

    def do_create(self, line):
        """Create an object"""
        if line == "":
            print("** class name missing **")
        else:
            try:
                instance = eval("{}()".format(line))
                instance.save()
                print(instance.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Show the information about an object"""
        split_line = line.split()
        if len(split_line) == 0:
            print("** class name missing **")
        elif len(split_line) > 0:
            try:
                instance = eval("{}()".format(split_line[0]))
                if len(split_line) != 2:
                    print("** instance id missing **")
                else:
                    dictionary_isntance = models.storage.all()
                    for key, value in dictionary_isntance.items():
                        splited = key.split('.')
                        if split_line[1] == splited[1] and splited[0] == split_line[0]:
                            return print(value)
                    print("** no instance found **")
            except Exception:
                print("** class doesn't exist **")


    def do_destroy(self, line):
        """Delete an object"""
        split_line = line.split()
        if len(split_line) == 0:
            print("** class name missing **")
        elif len(split_line) > 0:
            try:
                instance = eval("{}()".format(split_line[0]))
                if len(split_line) != 2:
                    print("** instance id missing **")
                else:
                    dictionary_isntance = models.storage.all()
                    for key, value in dictionary_isntance.items():
                        splited = key.split('.')
                        if split_line[1] == splited[1] and splited[0] == split_line[0]:
                            del dictionary_isntance[key]
                            models.storage.save()
                            return
                    print("** no instance found **")
            except Exception:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Show all objects of the same class"""
        split_line = line.split()
        if len(split_line) == 0:
            print("** class name missing **")
        elif len(split_line) > 0:
            try:
                eval("{}()".format(split_line[0]))
                models.storage.reload()
                dictionary_isntance = models.storage.all()
                new_list = []
                for key, value in dictionary_isntance.items():
                    splited = key.split('.')
                    if splited[0] == split_line[0]:
                        new_list.append(str(value))
                print(new_list)
            except Exception:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Usage: update <class name> <id> <attribute name> "<attribute value>
        update attribute instance object
        """
        flag = False
        key_dictionary = ""
        copy_object = object
        split_line = line.split()
        if len(split_line) == 0:
            print("** class name missing **")
        elif len(split_line) > 0:
            try:
                instance = eval("{}()".format(split_line[0]))
                if len(split_line) < 2:
                    print("** instance id missing **")
                else:
                    dictionary_isntance = models.storage.all()
                    for key, value in dictionary_isntance.items():
                        splited = key.split('.')
                        if split_line[1] == splited[1] and splited[0] == split_line[0]:
                            key_dictionary = key
                            copy_object = value
                            flag = True
                    if flag == False:
                        print("** no instance found **")
                    elif len(split_line) < 3:
                        print("** attribute name missing **")
                    elif len(split_line) < 4:
                        print("** value missing **")
                    else:
                        value_string = HBNBCommand.group_word(self, line)
                        if value_string == "":
                            value_string = split_line[3]
                        setattr(copy_object, split_line[2], value_string)
                        dictionary_isntance[key_dictionary] = copy_object
                        models.storage.save()
            except Exception:
                print("** class doesn't exist **")

    def do_quit(self, line):
        """Command to exit from the console\n"""
        return True

    def emptyline(self):
        """It repeats the last nonempty command entered"""
        pass

    def do_EOF(self, line):
        """It exit from the console when the user type Ctrl + D\n"""
        return True

    def group_word(self, line):
        """Convert a single string inside double quotes"""
        result_string = ""
        flag = False
        i = 0

        while len(line) > i:
            if line[i] == '"' or flag == True:
                flag = True
                result_string += line[i + 1]
                if line[i + 1] == '"':
                    result_string = result_string[:-1]
                    break
            i += 1
        return result_string


if __name__ == '__main__':
    HBNBCommand().cmdloop()
