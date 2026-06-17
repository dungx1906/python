import random
import string


def generate_assignment_code():

    characters = (
        string.ascii_uppercase +
        string.digits
    )

    random_part = "".join(
        random.choices(
            characters,
            k=4
        )
    )

    return f"PY-{random_part}"