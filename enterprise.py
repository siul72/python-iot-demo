"""
Enterprise helps
A collection of helper classes

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Luis Coelho"
__contact__ = "luis.coelho.720813@gmail.com"
__date__ = "2024.08"
__deprecated__ = False
__license__ = "BSD 2-Clause License"
__status__ = "Production"
__version__ = "0.0.1"

import json
from json import JSONDecodeError
from datetime import datetime

class BaseJson:
    def __init__(self, j=None):
        if j is not None:
            if isinstance(j, dict):
                self.__dict__ = json.loads(j)
            elif isinstance(j, str):
                self.__dict__ = json.loads(j)    
            else:
                print(f"{j} is {type(j)}")         

    def get_json_string(self):
        return json.dumps(self.__dict__)


class TagPayload(BaseJson):
    def __init__(self, value):
        super().__init__()
        self.timestamp = int(datetime.utcnow().timestamp())
        self.value = value
        self.type = f"{type(self.value)}"

class Temperature(BaseJson):
    def __init__(self, j):
        super().__init__(j)
    
