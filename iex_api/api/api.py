import requests
import datetime

from dataclasses import dataclass

from requests import Response
from requests.adapters import HTTPAdapter, Retry
from typing import TypeVar, Generic

from iex_api.api.model import IEXRange
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


class IEXApi:
    def __init__(self, configuration: IEXApiConfiguration):
        self.configuration = configuration

        self._messages_used = 0

    def perform_time_series_request(
        self,
        id: str,
        key: str,
        cls: Generic[T],
        sub_key: str = None,
        range: IEXRange = None,
        calendar: bool = False,
        limit: int = 1,
        date_field: datetime.date = None,
        from_date: datetime.date = None,
        to_date: datetime.date = None,
        on_date: datetime.date = None,
        last: int = None,
        first: int = None,
    ) -> T:
        assert (
            not range or range.requires_calendar and calendar
        ), f"Calendar must be set to True if using {range}"
        assert limit >= 1, "Limit must be > 1"

        params = {}
        if first is not None:
            params["first"] = first
        if last is not None:
            params["last"] = last
        if date_field is not None:
            params["dateField"] = convert_date_to_string(date_field)
        if to_date is not None:
            params["to"] = convert_date_to_string(to_date)
        if from_date is not None:
            params["from"] = convert_date_to_string(from_date)
        if on_date is not None:
            params["on"] = convert_date_to_string(on_date)

        path = f"/time-series/{id}/{key}"
        if sub_key is not None:
            path = f"{path}/{sub_key}"
        return self.perform_request(path, params, cls)

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

    def perform_request(self, path: str, parameters: dict, cls: Generic[T]) -> T:
        if not path.startswith("/"):
            path = "/" + path

        params = dict(parameters, token=self.configuration.api_token)
        url = self.configuration.api_url + path
        response = self.session().get(url, params=params)

        response.raise_for_status()

        self._messages_used = self._messages_used + _extract_messages_used(response)

        return cls.from_dict(response.json())
