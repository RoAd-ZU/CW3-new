# -*- coding: utf-8 -*-


from utils import hide_symbols


def start_main():
    for element in hide_symbols():
        print(f"{element['date']} {element['description']}")
        if 'from' in element:
            print(f"{element['from']} -> {element['to']}")
        else:
            print(element['to'])
        print(f"{element['operationAmount']['amount']} {element['operationAmount']['currency']['name']}")
        print()


if __name__ == "__main__":
    start_main()
