#JSON to Python dictionary

import json

x='{"a":12,"b":20,"c":30}'
print(type(x))
y=json.loads(x)
print(y["a"])