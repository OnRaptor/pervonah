import json


def load():
    with open('config.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        file.close()

    return data
