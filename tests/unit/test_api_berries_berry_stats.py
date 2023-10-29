import json
import os
import pytest

from api.berries.berry_stats import BerryStats

file_path = os.path.dirname(os.path.abspath(__file__))
test_resources = os.path.join(file_path, '..', 'resources')

def stats_from_resource(file_name):
    with open(os.path.join(test_resources, file_name), encoding='utf8') as file:
        return BerryStats(json.load(file))


def test_get_min_growth_time():
    berry_stats = stats_from_resource('berry_details_list.json')
    assert berry_stats.get_min_growth_time() == 8

def test_get_max_growth_time():
    berry_stats = stats_from_resource('berry_details_list.json')
    assert berry_stats.get_max_growth_time() == 24

def test_get_median_growth_time():
    berry_stats = stats_from_resource('berry_details_list.json')
    assert berry_stats.get_median_growth_time() == 18

def test_get_variance_growth_time():
    berry_stats = stats_from_resource('berry_details_list.json')
    assert berry_stats.get_variance_growth_time() == 33.142857142857146

def test_get_mean_growth_time():
    berry_stats = stats_from_resource('berry_details_list.json')
    assert berry_stats.get_mean_growth_time() == 19.142857142857142

def test_get_frequency_growth_time():
    berry_stats = stats_from_resource('berry_details_list.json')

    expected_frequency = {
        8: 1,
        18: 3,
        24: 3,
    }

    assert berry_stats.get_frequency_growth_time() == expected_frequency

def test_berry_stats_from_empty_list_raise_exception():
    with pytest.raises(ValueError):
        BerryStats([])
