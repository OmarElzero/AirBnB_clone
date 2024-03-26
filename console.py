#!/usr/bin/python3
"""this is  Entry point for the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """ processor Command"""

    prompt = "(hbnb) "
    l_classes = ['BaseModel', 'User', 'Amenity',
                 'Place', 'City', 'State', 'Review']

    l_c = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """parses for command inputs"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in HBNBCommand.l_classes and cnd[0] in HBNBCommand.l_c:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def help_help(self):
        """ Printing help commands descriptions """
        print("Provides description of a given command")

    def emptyline(self):
        """do nothing when  it ia an empty line"""
        pass

    def do_count(self, cls_name):
        """do count number of instances of  classes"""
        count = 0
        all_objs = storage.all()
        for m, z in all_objs.items():
            clss = m.split('.')
            if clss[0] == cls_name:
                count = count + 1
        print(count)

    def do_create(self, type_model):
        """ Creating an instance due to a given class """

        if not type_model:
            print("** class name missing **")
        elif type_model not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'City': City, 'Amenity': Amenity, 'State': State,
                   'Review': Review}
            my_model = dct[type_model]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """ Showing string representation of  passed instance"""

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for dic_k, res in all_objs.items():
                ob_name = res.__class__.__name__
                ob_id = res.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    print(res)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deleteing an instance passed """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for dic_k, res in all_objs.items():
                ob_name = res.__class__.__name__
                ob_id = res.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    del res
                    del storage._FileStorage__objects[dic_k]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints string represention of all instances of a given class """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            for dic_k, res in all_objs.items():
                ob_name = res.__class__.__name__
                if ob_name == args[0]:
                    list_instances += [res.__str__()]
            print(list_instances)

    def do_update(self, arg):
        """ Updating an instance based on the classes name ,id """

        if not arg:
            print("** class name missing **")
            return

        a = ""
        for argv in arg.split(','):
            a = a + argv

        args = shlex.split(a)

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for dic_k, objc in all_objs.items():
                ob_name = objc.__class__.__name__
                ob_id = objc.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** res missing **")
                    else:
                        setattr(objc, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """ Quit command to exit  """
        return True

    def do_EOF(self, line):
        """ EOF command for exiting the command interpreter """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
