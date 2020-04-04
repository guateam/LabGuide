import json


def read_json(case_dir):
    with open('./test_cases/' + case_dir) as file:
        return json.loads(file.read())
