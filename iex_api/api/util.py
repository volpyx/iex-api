import datetime

__all__ = ["convert_date_to_string"]


def convert_date_to_string(date: datetime.date) -> str:
    return date.strftime("%Y-%m-%d")
