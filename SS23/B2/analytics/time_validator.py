from datetime import datetime


def parse_and_inspect_date(date_string):


    try:
        upload_date = datetime.strptime(
            date_string,
            "%Y-%m-%d"
        )

        return upload_date

    except ValueError:
        return None