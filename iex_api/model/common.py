from dataclasses import dataclass
import datetime

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class IEXTimeSeriesObject:
    id: str = None
    source: str = None
    key: str = None
    sub_key: str = None
    date: datetime.date = None
    updated: datetime.date = None
