import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    list_numbers = []
    with open(filename) as file:
        input_ = file.readlines()
        input_ = [line.rstrip() for line in input_]
        step_1 = [value.split(delimiter) for value in input_]
        headers_list = step_1[0]
        fake_json = []
        for row in step_1[1:]:
            dicts = {headers_list[data]: row[data] for data in range(len(headers_list))}
            fake_json.append(dicts)
    return fake_json




print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))