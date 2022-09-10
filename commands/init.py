import os

from config import BASE_DIR


def init_fs():
    os.makedirs(BASE_DIR, exist_ok=True)
    print("File System initialized, ready to work")
