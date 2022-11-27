import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(delimiter=','):
    list_numbers = []
    with open(INPUT_FILE) as filename:
        input = filename.readlines()
        headers_list = input[0].rstrip().split(delimiter)
        for row in input[1:]:
            list_numbers.append(row.rstrip().split(delimiter))
        dicts = dict(zip(headers_list, list_numbers))
    return dicts


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))