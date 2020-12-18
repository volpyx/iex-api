from dataclasses import dataclass
import datetime
from typing import Optional, List

from dataclasses_json import dataclass_json, LetterCase

from iex_api.api.api import IEXApi
from iex_api.api.model.model import TimeSeriesRequest


class IEXBaseMixin:
    _API = None

    @classmethod
    def api(cls):
        if IEXBaseMixin._API is None:
            IEXBaseMixin._API = IEXApi.from_env()
        return IEXBaseMixin._API


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class IEXTimeSeriesObject(IEXBaseMixin):
    id: str
    key: str
    source: Optional[str]
    sub_key: Optional[str]
    date: Optional[datetime.date]
    updated: Optional[datetime.date]

    @classmethod
    def all(cls, key: str, sub_key: str = None, output_constructor=list):
        return cls.series(
            key, sub_key, TimeSeriesRequest(last=1_000_000), output_constructor
        )

    @classmethod
    def latest(cls, key: str, sub_key: str = None, n: int = 1, output_constructor=list):
        return cls.series(
            key,
            sub_key,
            TimeSeriesRequest(last=n),
            output_constructor=output_constructor,
        )

    @classmethod
    def series(
        cls,
        key: str,
        sub_key: str,
        request: TimeSeriesRequest = None,
        output_constructor=list,
    ):
        return output_constructor(
            cls.api().perform_time_series_request(cls.ID, key, cls, sub_key, request)
        )


@dataclass(frozen=True)
class SymbolMixin(IEXBaseMixin):
    symbol: str

    @classmethod
    def from_symbol(cls, symbol: str):
        raise NotImplementedError


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Symbol(IEXBaseMixin):
    symbol: str
    exchange: str
    name: str
    date: datetime.date
    type: str
    iexId: str
    region: str
    currency: str
    isEnabled: bool

    @classmethod
    def get_all_symbols_for_region(cls, region: str) -> List["Symbol"]:
        return cls.api().perform_request(f"/ref-data/region/{region}/symbols", cls)
