import json
import pytest
import requests

from requests import Response

from api.berries import services
from api.berries.services import (
    fetch_all_berries,
)


def build_response(body: dict, status: int = 200) -> Response:
    response = Response()
    response.status_code = status
    response._content = json.dumps(body)  # pylint: disable=protected-access
    response.json = lambda: body
    return response

def set_mock_requests(mocker, monkeypatch, all_berries_count: int, berries_per_page: int) -> None:
    last_offset = (all_berries_count // berries_per_page) * berries_per_page

    def mock_requests(url: str, *_, **kwargs):
        params = kwargs.get('params', {})

        if url.endswith('/berry/'):
            if params.get('offset', 0)< last_offset:
                n_results = berries_per_page
            else:
                n_results = all_berries_count - last_offset

            response = {
                'count': all_berries_count,
                'next': None,
                'previous': None,
                'results': [
                    {'name': 'cheri', 'url': 'https://pokeapi.co/api/v2/berry/1/'}
                    for _ in range(n_results)
                ]
            }
        else:
            response = {
                'fake': 'details'
            }

        return build_response(response)

    mocker.patch(
        'requests.get',
        mock_requests
    )
    monkeypatch.setattr(services, 'BERRIES_PER_PAGE_LIMIT', berries_per_page)

def test_fetch_all_berries_returns_all_berries(mocker, monkeypatch) -> None:
    set_mock_requests(mocker, monkeypatch, all_berries_count=14, berries_per_page=3)

    berries = fetch_all_berries()
    assert len(berries) == 14

def test_fetch_all_berries_returns_all_berries_one_page(mocker, monkeypatch) -> None:
    set_mock_requests(mocker, monkeypatch, all_berries_count=11, berries_per_page=15)

    berries = fetch_all_berries()
    assert len(berries) == 11

def test_fetch_zero_berries_returns_empty_list(mocker, monkeypatch) -> None:
    set_mock_requests(mocker, monkeypatch, all_berries_count=0, berries_per_page=15)

    berries = fetch_all_berries()
    assert len(berries) == 0

def test_all_berries_raise_for_status_no_200(mocker) -> None:
    mocker.patch(
        'requests.get',
        lambda *_, **__: build_response({'fake': 'response'}, status=500)
    )

    with pytest.raises(requests.HTTPError):
        fetch_all_berries()
