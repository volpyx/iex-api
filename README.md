# iex-api

[![Build Status](https://github.com/volpyx/iex-api/workflows/Build%20Main/badge.svg)](https://github.com/volpyx/iex-api/actions)
[![Documentation](https://github.com/volpyx/iex-api/workflows/Documentation/badge.svg)](https://volpyx.github.io/iex-api/)
[![Code Coverage](https://codecov.io/gh/volpyx/iex-api/branch/main/graph/badge.svg)](https://codecov.io/gh/volpyx/iex-api)

Unofficial Python IEX Cloud Api.

---

## Features

-   Supports Income, CashFlow, Financials, Quote, EndOfDayPrice
-   Primarily uses time-series to make it easier to query older data
-   Is asynchronous
-   Typed

## Quick Start

```python
import asyncio
import os

from iex_api.model.company import Income, CashFlow, Financials

os.environ.update({
    "IEX_API_URL": "https://sandbox.iexapis.com/stable/",
    "IEX_API_TOKEN": "<>",
})


async def gather_company_info(symbol: str):
    income, cashflow, financials = await asyncio.gather(
        Income.latest(symbol),
        CashFlow.latest(symbol),
        Financials.latest(symbol)
    )
    print(income.gross_profit)
    print(cashflow.cash_flow)
    print(financials.ebit)

loop = asyncio.get_event_loop()
loop.run_until_complete(gather_company_info('AAPL'))

```

## Installation

**Stable Release:** `pip install iex_api`<br>
**Development Head:** `pip install git+https://github.com/volpyx/iex_api.git`

## Documentation

For full package documentation please visit [volpyx.github.io/iex_api](https://volpyx.github.io/iex-api).

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

## The Four Commands You Need To Know

1. `pip install -e .[dev]`

    This will install your package in editable mode with all the required development
    dependencies (i.e. `tox`).

2. `make build`

    This will run `tox` which will run all your tests in both Python 3.7
    and Python 3.8 as well as linting your code.

3. `make clean`

    This will clean up various Python and build generated files so that you can ensure
    that you are working in a clean environment.

4. `make docs`

    This will generate and launch a web browser to view the most up-to-date
    documentation for your Python package.
