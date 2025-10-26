import json


json_path = 'memes.json'
def load_data():
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

def find_object_by_name(name):
    data = load_data()
    for obj in data:
        if obj['name'] == name:
            return obj
    return None

def send_first_15_objects():
    data = load_data()
    return data[:15]
def add_object(new_object):
    data = load_data()
    data.append(new_object)
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)