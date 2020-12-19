import asyncio
import datetime
from dataclasses import dataclass
from typing import Iterable
from itertools import chain
from dataclasses_json import dataclass_json, LetterCase

from iex_api.model.common import IEXTimeSeriesObject


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class EndOfDayOptions(IEXTimeSeriesObject):
    ask: float
    bid: float
    cfi_code: str
    close: float
    closing_price: float
    contract_description: str
    contract_name: str
    contract_size: int
    currency: str
    exchange_code: str
    exchange_MIC: str
    exercise_style: str
    expiration_date: datetime.date
    figi: str
    high: float
    is_adjusted: bool
    last_trade_date: datetime.date
    last_trade_time: datetime.time
    last_updated: datetime.date
    low: float
    margin_price: float
    open: float
    open_interest: int
    settlement_price: float
    side: str
    strike_price: float
    symbol: str
    type: str
    volume: int

    @classmethod
    async def latest(cls, symbol: str, *args, **kwargs) -> Iterable["EndOfDayOptions"]:
        if "n" in kwargs and kwargs["n"] != 1:
            raise ValueError("Latest end of day options only supports n=1")
        expiry_dates = await cls.api().perform_request(f"/stock/{symbol}/options/", str)
        return await asyncio.gather(
            *chain(
                asyncio.ensure_future(
                    cls.api().perform_request(
                        f"/stock/{symbol}/options/{expiry_date}", EndOfDayOptions
                    )
                )
                for expiry_date in expiry_dates
            )
        )
