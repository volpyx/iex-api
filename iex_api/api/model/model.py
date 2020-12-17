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
]


@dataclass
class IEXRange:
    value: str
    requires_calendar: bool


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


def d(amount: int) -> IEXRange:
    return IEXRange(f"d{amount}", False)


def w(amount: int) -> IEXRange:
    return IEXRange(f"w{amount}", False)


def m(amount: int) -> IEXRange:
    return IEXRange(f"m{amount}", False)


def q(amount: int) -> IEXRange:
    return IEXRange(f"q{amount}", False)


def y(amount: int) -> IEXRange:
    return IEXRange(f"y{amount}", False)
