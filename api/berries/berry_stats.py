from collections import Counter
from io import BytesIO
from typing import Dict, List, TYPE_CHECKING
from statistics import median, variance, mean

import matplotlib.pyplot as plt


if TYPE_CHECKING:
    from .services import BerryDetail


class BerryStats():
    def __init__(self, berries: List['BerryDetail']) -> None:
        if not berries:
            raise ValueError('berries cannot be empty')
        self._berries = berries

    @property
    def berries(self) -> List['BerryDetail']:
        return self._berries

    def get_min_growth_time(self) -> int:
        return min(b['growth_time'] for b in self._berries)

    def get_max_growth_time(self) -> int:
        return max(b['growth_time'] for b in self._berries)

    def get_median_growth_time(self) -> float:
        return median(b['growth_time'] for b in self._berries)

    def get_variance_growth_time(self) -> float:
        return variance(b['growth_time'] for b in self._berries)

    def get_mean_growth_time(self) -> float:
        return mean(b['growth_time'] for b in self._berries)

    def get_frequency_growth_time(self) -> Dict[int, int]:
        return Counter(b['growth_time'] for b in self._berries)


class BerryStatsStatsPlot():
    def __init__(self, berries: List['BerryDetail']) -> None:
        self._stats = BerryStats(berries)

    def generate_histogram_plot(self):
        fig, ax = plt.subplots()

        ax.hist([b['growth_time'] for b in self._stats.berries])

        tmp_file = BytesIO()
        fig.savefig(tmp_file, format='png')

        return tmp_file
