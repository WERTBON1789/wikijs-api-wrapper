from typing import List
from wikijspy.types.error import InvalidOutputError

class ResponseStatusOutput:
    _validation_list = [
        "succeeded",
        "errorCode",
        "slug",
        "message"
    ]

    def __init__(self, output: List[str]) -> None:
        for item in output:
            if not item in self._validation_list:
                raise InvalidOutputError(item, self.__class__.__name__)
        self.output = output
    
    def __iter__(self):
        self.i = 0
        self.max = len(self.output)
        return self
    
    def __next__(self):
        if self.i <= self.max:
            result = self.i
            self.i += 1
            return self.output[result]
        else:
            raise StopIteration
