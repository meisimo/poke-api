import json
from typing import Dict, TYPE_CHECKING, TypedDict

from api.cache import cache_static_endpoint

from .services import fetch_all_berries
from .berry_stats import BerryStats

if TYPE_CHECKING:
    class BerryStatsDict(TypedDict):
        berries_names: list[str]
        min_growth_time: int
        median_growth_time: float
        max_growth_time: int
        variance_growth_time: float
        mean_growth_time: float
        frequency_growth_time: Dict[int, int]


def _serialize_berry_stats(berry_stats: BerryStats) -> 'BerryStatsDict':
    return {
        'berries_names': [b['name'] for b in berry_stats.berries],
        'min_growth_time': berry_stats.get_min_growth_time(),
        'median_growth_time': berry_stats.get_median_growth_time(),
        'max_growth_time': berry_stats.get_max_growth_time(),
        'variance_growth_time': berry_stats.get_variance_growth_time(),
        'mean_growth_time': berry_stats.get_mean_growth_time(),
        'frequency_growth_time': berry_stats.get_frequency_growth_time(),
    }


@cache_static_endpoint(
    'allBerryStats',
    serialize_cb   = json.dumps,
    deserialize_cb = json.loads,
    timeout = 60*60*24
)
def get_all_berries_stats() -> 'BerryStatsDict':
    """ Fetch all the berries and return their stats structured in the expected format """
    berries = fetch_all_berries()
    stats   = BerryStats(berries)
    return _serialize_berry_stats(stats)
