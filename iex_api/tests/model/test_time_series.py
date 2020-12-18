from iex_api.model.common import IEXTimeSeriesObject


def test_time_series_from_dict():
    assert IEXTimeSeriesObject.from_dict(
        {"id": "id", "key": "key"}, infer_missing=True
    ) == IEXTimeSeriesObject(
        key="key",
        id="id",
        source=None,
        sub_key=None,
        date=None,
        updated=None,
    )
