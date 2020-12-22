import datetime
from dataclasses import dataclass
from typing import Optional

from dataclasses_json import LetterCase, dataclass_json

from iex_api.api.model.model import IEXRange
from iex_api.model.common import IEXTimeSeriesObject, SymbolMixin


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class IntraDayStockPrice:
    date: datetime.date
    minute: datetime.time
    market_average: float
    market_number_of_trades: int
    market_open: float
    market_close: float
    market_high: float
    market_low: float
    market_volume: int
    market_change_over_time: float
    change_over_time: float
    label: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class HistoricalStockPrice(IEXTimeSeriesObject, SymbolMixin):
    symbol: str
    close: float
    high: float
    low: float
    open: float
    volume: int
    change_over_time: float
    market_change_over_time: float
    u_open: Optional[float]
    u_close: Optional[float]
    u_high: Optional[float]
    u_low: Optional[float]
    u_volume: Optional[int]
    f_open: Optional[float]
    f_close: Optional[float]
    f_high: Optional[float]
    f_flow: Optional[float]
    f_volume: Optional[int]
    label: str
    change: Optional[float]
    change_percent: Optional[float]

    @classmethod
    async def from_symbol(
        cls, symbol: str, range: IEXRange, **kwargs
    ) -> "HistoricalStockPrice":
        return await cls.api().chart(symbol, range, cls, **kwargs)
