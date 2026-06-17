import math


def calculate_disk_blocks(
        size_bytes,
        block_size=4096):

    required_blocks = math.ceil(
        size_bytes / block_size
    )

    return required_blocks