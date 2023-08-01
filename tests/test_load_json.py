# -*- coding: utf-8 -*-
import pytest
from load_json import load_json, search_for_errors, removees_canceled, date_correction, sorting
from utils import get_five_operations
data1 = get_five_operations()
def test_load_json():
    test_list = load_json()
    assert isinstance(test_list, list)

@pytest.mark.parametrize('arrey'[data1])
def test_search_for_errors(arrey):
    assert len(get_five_operations()) == len(search_for_errors(arrey))



