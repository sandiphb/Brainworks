#Dumps
import json

x={
    "a":12,
    "b":20,
    "c":30
}
print(type(x))
y=json.dumps(x)
print(y)
print(type(y))