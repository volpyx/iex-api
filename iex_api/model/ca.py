import datetime
from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase

from iex_api.model.common import IEXTimeSeriesObject


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class BasicDividend(IEXTimeSeriesObject):
    amount: float
    currency: str
    declared_date: datetime.date
    description: str
    ex_date: datetime.date
    flag: str
    frequency: str
    payment_date: datetime.date
    record_date: datetime.date
    refid: int
    symbol: str

    ID = "DIVIDENDS"


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class AdvancedDividend(IEXTimeSeriesObject):
    symbol: str
    ex_date: datetime.date
    record_date: datetime.date
    payment_date: datetime.date
    announce_date: datetime.date
    currency: str
    frequency: str
    amount: float
    description: str
    flag: str
    security_type: str
    notes: str
    figi: str
    last_updated: datetime.date
    country_code: str
    par_value: str
    par_valueCurrency: str
    net_amount: float
    gross_amount: float
    marker: str
    tax_rate: float
    from_factor: float
    to_factor: float
    adr_fee: float
    coupon: float
    declared_currency_CD: str
    declared_gross_amount: float
    is_net_investment_income: bool
    is_DAP: bool
    is_approximate: bool
    fx_date: datetime.date
    second_payment_date: datetime.date
    second_ex_date: datetime.date
    fiscal_year_end_date: datetime.date
    period_end_date: datetime.date
    optional_election_date: datetime.date
    to_date: datetime.date
    registration_date: datetime.date
    installment_pay_date: datetime.date
    declared_date: datetime.date
    refid: int
    created: datetime.date

    ID = "ADVANCED_DIVIDENDS"
