import os

from config import BASE_DIR
from helpers.helper_list import helper_list


@helper_list
def list_files():
    files = os.listdir(BASE_DIR)
    print('\n'.join(files))