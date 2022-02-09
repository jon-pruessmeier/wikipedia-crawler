import json
import sys
from testdata import data
data_json = json.dumps(data)
print(data_json)

sys.stdout.flush()