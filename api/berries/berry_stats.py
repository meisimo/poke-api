from typing import List, TYPE_CHECKING, TypedDict


if TYPE_CHECKING:
    from .services import BerryDetail

    class BerryStatsDict(TypedDict):
        berries_names: list[str]
        min_growth_time: int
        median_growth_time: float
        max_growth_time: int
        variance_growth_time: float
        mean_growth_time: float
        frequency_growth_time: float


class BerryStats():
    def __init__(self, berries: List['BerryDetail']) -> None:
        self._berries = berries

    @property
    def berries(self) -> List['BerryDetail']:
        return self._berries

    def get_min_growth_time(self) -> int:
        # TODO: Pending to implement
        ...

    def get_max_growth_time(self) -> int:
        # TODO: Pending to implement
        ...

    def median_growth_time(self) -> float:
        # TODO: Pending to implement
        ...

    def variance_growth_time(self) -> float:
        # TODO: Pending to implement
        ...

    def mean_growth_time(self) -> float:
        # TODO: Pending to implement
        ...

    def frequency_growth_time(self) -> float:
        # TODO: Pending to implement
        ...
