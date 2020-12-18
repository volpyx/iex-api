import datetime
from dataclasses import dataclass

__all__ = [
    "today",
    "tomorrow",
    "yesterday",
    "year_to_date",
    "last_week",
    "last_month",
    "last_quarter",
    "this_week",
    "this_month",
    "this_quarter",
    "next_week",
    "next_month",
    "next_quarter",
    "d",
    "w",
    "m",
    "q",
    "y",
    "IEXRange",
    "TimeSeriesRequest",
]

from iex_api.api.util import convert_date_to_string


@dataclass
class IEXRange:
    value: str
    requires_calendar: bool

    def minute_intervals(self):
        return IEXRange(
            value=f"{self.value}m", requires_calendar=self.requires_calendar
        )


max = IEXRange("max", False)

today = IEXRange("today", False)
tomorrow = IEXRange("tomorrow", True)
yesterday = IEXRange("yesterday", False)
year_to_date = IEXRange("ytd", False)
last_week = IEXRange("last-week", False)
last_month = IEXRange("last-month", False)
last_quarter = IEXRange("last-quarter", False)
this_week = IEXRange("this-week", True)
this_month = IEXRange("this-month", True)
this_quarter = IEXRange("this-quarter", True)
next_week = IEXRange("next-week", True)
next_month = IEXRange("next-month", True)
next_quarter = IEXRange("next-quarter", True)


def date(date: datetime.date) -> IEXRange:
    return IEXRange(convert_date_to_string(date), False)


def d(amount: int) -> IEXRange:
    return IEXRange(f"{amount}d", False)


def w(amount: int) -> IEXRange:
    return IEXRange(f"{amount}w", False)


def m(amount: int) -> IEXRange:
    return IEXRange(f"{amount}m", False)


def q(amount: int) -> IEXRange:
    return IEXRange(f"{amount}q", False)


def y(amount: int) -> IEXRange:
    return IEXRange(f"{amount}y", False)


@dataclass
class TimeSeriesRequest:
    range: IEXRange = None
    calendar: bool = None
    limit: int = 1
    date_field: datetime.date = None
    from_date: datetime.date = None
    to_date: datetime.date = None
    on_date: datetime.date = None
    last: int = None
    first: int = None
