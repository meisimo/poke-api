from typing import List, TYPE_CHECKING, TypedDict, Iterable
import math

import requests

from api.settings import (
    BERRIES_PER_PAGE_LIMIT,
    REQUEST_TIMEOUT,
)


if TYPE_CHECKING:
    class BerryPage(TypedDict):
        count: int
        next: str
        previous: str
        results: List[TypedDict('Berry', {'name': str, 'url': str})]

    class BerryDetail(TypedDict):
        firmness: dict
        flavors: List[dict]
        growth_time: int
        id: int
        item: TypedDict('Item', {'name': str, 'url': str})
        max_harvest: int
        name: str
        natural_gift_power: int
        natural_gift_type: dict
        size: int
        smoothness: int
        soil_dryness: int

def _raise_errors_and_extract_json(request_fn):
    def fn(*args, **kwargs):
        response = request_fn(*args, **kwargs)
        response.raise_for_status()
        return response.json()
    return fn


@_raise_errors_and_extract_json
def _fetch_berries_page(page: int) -> 'BerryPage':
    params = {
        'limit': BERRIES_PER_PAGE_LIMIT,
        'offset': (page - 1) * BERRIES_PER_PAGE_LIMIT,
    }
    return requests.get(
        "https://pokeapi.co/api/v2/berry/",
        params=params,
        timeout=REQUEST_TIMEOUT)

@_raise_errors_and_extract_json
def _fetch_berry_detail(berry_url: str) -> 'BerryDetail':
    return requests.get(
        berry_url,
        timeout=REQUEST_TIMEOUT)

def _fetch_berrie_pages() -> Iterable['BerryPage']:
    first_page = _fetch_berries_page(1)
    n_pages    = math.ceil(first_page['count'] / BERRIES_PER_PAGE_LIMIT)

    yield first_page

    for page in range(2, n_pages + 1):
        yield _fetch_berries_page(page)

def fetch_all_berries() -> List['BerryDetail']:
    """Fetch all berries details from the pokeapi.co API"""

    details = []
    for page in _fetch_berrie_pages():
        for berry in page['results']:
            details.append(_fetch_berry_detail(berry['url']))
    return details
