import os

from config import BASE_DIR
from helpers.helper_delete import helper_delete


@helper_delete
def del_file(name):
    os.remove(f"{BASE_DIR}{name}")
    print(f"file {name} was successfully deleted")