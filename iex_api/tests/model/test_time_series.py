from iex_api.model.common import IEXTimeSeriesObject


def test_time_series_from_dict():
    assert IEXTimeSeriesObject.from_dict({}) == IEXTimeSeriesObject()
