# -*- coding: utf-8 -*-

"""IUGW custom tags."""

from dojson import utils
from dojson.contrib.marc21 import marc21


@marc21.over('base', '^960__')
# We use for_each_value decorator, because 960 is a repeatable field
@utils.for_each_value
def base(self, key, value):
    """Base."""
    return value.get('a')


@marc21.over('status_week', '^916__')
@utils.for_each_value
# We use filter_values to remore None from the dictionary
@utils.filter_values
def status_week(self, key, value):
    """Status week."""
    return {
        'acquisition_of_proceedings_code': value.get('a'),
        'display_period_for_books': value.get('d'),
        'number_of_copies_bought_by_cern': value.get('e'),
        'status_of_record': value.get('s'),
        'status_week': value.get('w'),
        'year_for_annual_list': value.get('y'),
    }
