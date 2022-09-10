import os

from config import BASE_DIR
from helpers.helper_init import helper_init

@helper_init
def init_fs() -> None:
    os.makedirs(BASE_DIR, exist_ok=True)
    print("File System initialized, ready to work")
