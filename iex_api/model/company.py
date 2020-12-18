import datetime
from dataclasses import dataclass
from typing import List, Optional

from dataclasses_json import dataclass_json, LetterCase

from iex_api.model.common import SymbolMixin, IEXTimeSeriesObject


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Financials(IEXTimeSeriesObject):
    EBITDA: int
    accounts_payable: int
    capital_surplus: int
    cash_change: int
    cash_flow: int
    cash_flow_financing: int
    changes_in_inventories: int
    changes_in_receivables: int
    common_stock: int
    cost_of_revenue: int
    currency: str
    current_assets: int
    current_cash: int
    current_debt: int
    current_long_term_debt: int
    depreciation: int
    dividends_paid: int
    ebit: int
    exchange_rate_effect: int
    fiscal_date: datetime.date
    goodwill: int
    gross_profit: int
    income_tax: int
    intangible_assets: int
    interest_income: int
    inventory: int
    investing_activity_other: int
    investments: int
    longTerm_debt: int
    longTerm_investments: int
    minority_interest: int
    net_borrowings: int
    net_income: int
    net_income_basic: int
    net_tangible_assets: int
    operating_expense: int
    operating_income: int
    operating_revenue: int
    other_assets: int
    other_current_assets: int
    other_current_liabilities: int
    other_income_expense_net: int
    other_liabilities: int
    pretax_income: int
    property_plant_equipment: int
    receivables: int
    report_date: datetime.date
    research_and_development: int
    retained_earnings: int
    revenue: int
    selling_general_and_admin: int
    shareholder_equity: int
    shortTerm_debt: int
    shortTerm_investments: int
    symbol: str
    total_assets: int
    total_cash: int
    total_debt: int
    total_investing_cash_flows: int
    total_liabilities: int
    total_revenue: int
    treasury_stock: int

    ID = "FINANCIALS"


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class CashFlow(IEXTimeSeriesObject):
    capital_expenditures: int
    cash_change: int
    cash_flow: int
    cash_flow_financing: int
    changes_in_inventories: int
    changes_in_receivables: int
    currency: str
    depreciation: int
    dividends_paid: int
    exchange_rate_effect: int
    fiscal_date: datetime.date
    investing_activity_other: int
    investments: int
    net_borrowings: int
    net_income: int
    other_financing_cash_flows: int
    report_date: datetime.date
    symbol: str
    total_investing_cash_flows: int

    ID = "CASH_FLOW"


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Income(IEXTimeSeriesObject):
    report_date: datetime.date
    fiscal_date: datetime.date
    currency: str
    total_revenue: int
    cost_of_revenue: int
    gross_profit: int
    research_and_development: int
    selling_general_and_admin: int
    operating_expense: int
    operating_income: int
    other_income_expense_net: int
    ebit: int
    interest_income: int
    pretax_income: int
    income_tax: int
    minority_interest: int
    net_income: int
    net_incomeBasic: int

    ID = "INCOME"


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Company(SymbolMixin):
    company_name: str
    exchange: str
    industry: str
    website: str
    description: str
    CEO: str
    security_name: str
    issue_type: str
    sector: str
    primary_sic_code: int
    employees: int
    tags: List[str]
    address: str
    address2: Optional[str]
    state: str
    city: str
    zip: str
    country: str
    phone: str

    @classmethod
    def from_symbol(cls, symbol: str):
        return cls.api().perform_request(f"/stock/{symbol}/company", Company)
