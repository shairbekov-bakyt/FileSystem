import sys

from commands.init import init_fs
from commands.add import add_file
from commands.delete import del_file

commands = {
    'add': add_file,
    'del': del_file,
    'init': init_fs,
    'list': 'list',
}

if len(sys.argv) < 2:
    print("wrong argument")
    exit(0)

_, command, *args = sys.argv

if command not in commands:
    print("command not found")
    exit(0)

commands[command](*args)