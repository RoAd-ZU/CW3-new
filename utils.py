# -*- coding: utf-8 -*-

from load_json import load_json, search_for_errors, removees_canceled, date_correction, sorting

data1 = load_json()
data2 = search_for_errors(data1)
data3 = removees_canceled(data2)
data4 = date_correction(data3)


def get_five_operations():
    sort = sorting(data4)[-5:]
    sort.reverse()
    return sort


#
def hide_symbols():
    five_operations = get_five_operations()
    for element in five_operations:
        if element['to'][0] == 'С':
            element['to'] = 'Счет ' + '**' + element['to'][-4:]
        else:
            element['to'] = element['to'][:-12] + ' ' + element['to'][-11:-9] + '** ' + '**** ' + element['to'][-4:]
        if 'from' in element:
            if element['from'][0] == 'С':
                element['from'] = 'Счет ' + '**' + element['from'][-4:]
            else:
                element['from'] = element['from'][:-12] + ' ' + element['from'][-11:-9] + '** ' + '**** ' + element[
                                                                                                                'from'][
                                                                                                            -4:]
        else:
            continue

    return five_operations
