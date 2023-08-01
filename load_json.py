# -*- coding: utf-8 -*-

import json
from datetime import datetime


def load_json():
    with open('operations.json', 'r', encoding="utf-8") as operations_:
        return json.load(operations_)


def search_for_errors(data1):
    operations = []
    for element in data1:
        if 'state' in element:
            operations.append(element)
    return operations


def removees_canceled(data2):
    operetion_executed = []
    for element in data2:
        if element['state'] == 'EXECUTED':
            operetion_executed.append(element)
    return operetion_executed


def date_correction(data3):
    operations = []
    for element in data3:
        date = datetime.strptime(element['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        element['date'] = date
        operations.append(element)
    return operations


def sorting(data4):
    return sorted(data4, key=lambda e: '.'.join(reversed(e['date'].split('.'))))


data1 = load_json()
data2 = search_for_errors(data1)
data3 = removees_canceled(data2)
data4 = date_correction(data3)
