import json
from uuid import UUID
from aiohttp import web


class ResponseTemplate:
    def __init__(self, request: web.Request, result, addition=None, description=''):
        self.method = request.method
        self.result = result
        self.addition = to_dict(addition)
        self.description = description

    def to_dict(self):
        return json.dumps({"status": self.method,
                           "result": self.result,
                           "addition": self.addition,
                           "description": self.description}, cls=UUIDEncoder)


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        return json.JSONEncoder.default(self, obj)


def to_dict(record):
    if record is None:
        return record
    return {k: record[k] for k in record.keys()}
