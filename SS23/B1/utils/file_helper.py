import os


def create_log_directory(directory_name):

    if not os.path.exists(directory_name):
        os.makedirs(directory_name)