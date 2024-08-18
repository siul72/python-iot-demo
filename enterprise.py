import json
from json import JSONDecodeError
from datetime import datetime

class BaseJson:
    def __init__(self, j=None):
        if j is not None:
            if isinstance(j, dict):
                self.__dict__ = json.loads(j)

    def get_json_string(self):
        return json.dumps(self.__dict__)


class TagPayload(BaseJson):
    def __init__(self, value):
        super().__init__()
        self.timestamp = int(datetime.utcnow().timestamp())
        self.value = value
        self.type = f"{type(self.value)}"
    
