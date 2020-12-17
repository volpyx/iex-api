from dataclasses import dataclass
import datetime

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class IEXTimeSeriesObject:
    id: str
    source: str
    key: str
    sub_key: str
    date: datetime.date
    updated: datetime.date
