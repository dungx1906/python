import os


def safe_create_dir(directory_path):

    os.makedirs(
        directory_path,
        exist_ok=True
    )