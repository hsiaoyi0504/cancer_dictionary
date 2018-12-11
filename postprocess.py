import json
from collections import ChainMap
import os

with open('temp.json') as f:
    data = json.load(f)

data = dict(ChainMap(*data))

with open('result.json', 'w') as f:
    json.dump(data, f)

os.remove('temp.json')
