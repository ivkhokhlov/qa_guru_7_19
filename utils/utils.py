import json
import os
from config import BASE_DIR


def load_file(file_path):
    with open(file_path) as f:
        return f.read()


def load_schema(name):
    file_path = os.path.join(BASE_DIR, 'schemas', name)
    schema_json = load_file(file_path)
    return json.loads(schema_json)
