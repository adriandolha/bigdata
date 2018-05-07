import json


class JsonUtils:
    @staticmethod
    def toJson(item):
        return json.dumps(item, default=lambda o: o.__dict__.values()[0])
