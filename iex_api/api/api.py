import os
import requests
import datetime

from dataclasses import dataclass

from requests import Response
from requests.adapters import HTTPAdapter, Retry
from typing import TypeVar, Generic, List

from iex_api.api.model.model import IEXRange, TimeSeriesRequest
from iex_api.api.util import convert_date_to_string


def _extract_messages_used(response: Response) -> int:
    return int(response.headers.get("iexcloud-messages-used", 0))


T = TypeVar("T")


@dataclass
class IEXApiConfiguration:
    api_token: str
    api_url: str

    retry_count: int = 10
    backoff_factor: float = 0.5

    def __post_init__(self):
        if self.api_url.endswith("/"):
            self.api_url = self.api_url[: len(self.api_url) - 1]

    @classmethod
    def from_env(cls):
        return cls(os.environ["IEX_API_TOKEN"], os.environ["IEX_API_URL"])


class IEXApi:
    def __init__(self, configuration: IEXApiConfiguration):
        self.configuration = configuration
        self._messages_used = 0

    @property
    def message_count(self):
        return self._messages_used

    @classmethod
    def from_env(cls):
        return cls(IEXApiConfiguration.from_env())

    def chart(
        self,
        symbol: str,
        range: IEXRange,
        cls: T,
        chart_close_only: bool = None,
        chart_by_day: bool = None,
        chart_simplify: bool = None,
        chart_interval: int = None,
        change_from_close: bool = None,
        chart_last: int = None,
        display_percent: bool = None,
        exact_date: datetime.date = None,
        sort: bool = None,
        include_today: bool = None,
    ) -> List[T]:
        params = {}
        if chart_close_only is not None:
            params["chartCloseOnly"] = chart_close_only
        if chart_by_day is not None:
            params["chartByDay"] = chart_by_day
        if chart_simplify is not None:
            params["chartSimplify"] = chart_simplify
        if chart_interval is not None:
            params["chartInterval"] = chart_interval
        if change_from_close is not None:
            params["changeFromClose"] = change_from_close
        if chart_last is not None:
            params["chartLast"] = chart_last
        if display_percent is not None:
            params["displayPercent"] = display_percent
        if exact_date is not None:
            params["exactDate"] = convert_date_to_string(exact_date)
        if sort is not None:
            params["sort"] = sort
        if include_today is not None:
            params["includeToday"] = include_today

        return self.perform_request(f"/stock/{symbol}/chart/{range.value}", cls, params)

    def perform_time_series_request(
        self,
        id: str,
        key: str,
        cls: Generic[T],
        sub_key: str = None,
        request: TimeSeriesRequest = None,
    ) -> List[T]:
        params = {}
        if request:
            assert (
                not request.range
                or request.range.requires_calendar
                and request.calendar
            ), f"Calendar must be set to True if using {range}"
            assert request.limit >= 1, "Limit must be > 1"

            if request.range is not None:
                params["range"] = request.range.value
            if request.first is not None:
                params["first"] = request.first
            if request.last is not None:
                params["last"] = request.last
            if request.date_field is not None:
                params["dateField"] = convert_date_to_string(request.date_field)
            if request.to_date is not None:
                params["to"] = convert_date_to_string(request.to_date)
            if request.from_date is not None:
                params["from"] = convert_date_to_string(request.from_date)
            if request.on_date is not None:
                params["on"] = convert_date_to_string(request.on_date)

        path = f"/time-series/{id}/{key}"
        if sub_key is not None:
            path = f"{path}/{sub_key}"
        return self.perform_request(path, cls, params)

    def session(self) -> requests.Session:
        session = requests.Session()
        session.mount(
            "https://",
            HTTPAdapter(
                max_retries=Retry(
                    total=self.configuration.retry_count,
                    backoff_factor=self.configuration.backoff_factor,
                    status_forcelist=[429, 500],
                    method_whitelist=False,
                )
            ),
        )
        return session

    def perform_request(self, path: str, cls: Generic[T], parameters: dict = None) -> T:
        if parameters is None:
            parameters = {}
        if not path.startswith("/"):
            path = "/" + path

        params = dict(parameters, token=self.configuration.api_token)
        url = self.configuration.api_url + path
        response = self.session().get(url, params=params)
        print(url)
        response.raise_for_status()

        self._messages_used = self._messages_used + _extract_messages_used(response)

        data = response.json()
        if isinstance(data, list):

            def from_dict(source: dict):
                return cls.from_dict(source, infer_missing=True)

            return map(from_dict, data)
        return cls.from_dict(data, infer_missing=True)
