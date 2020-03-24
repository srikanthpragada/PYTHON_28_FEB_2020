import json


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(10, 20)
js = json.dumps(p.__dict__)  # Convert dict to JSON
print("Json : ", js)
pd = json.loads(js)   # Convert JSON to dict
print("Dict : ", pd)
