import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    list_numbers = []
    with open(filename) as file:
        input_ = file.readlines()
        input_ = [line.rstrip() for line in input_]
        delimited_list = [value.split(delimiter) for value in input_]
        headers_list = delimited_list[0]
        list_of_dicts = []
        for row in step_1[1:]:
            dicts = {headers_list[data]: row[data] for data in range(len(headers_list))}
            list_of_dicts.append(dicts)
    return list_of_dicts

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))