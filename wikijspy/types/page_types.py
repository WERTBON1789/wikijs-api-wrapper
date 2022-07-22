from enum import Enum
from typing import List

class PageOrderBy(Enum):
    CREATED = 0
    ID = 1
    PATH = 2
    TITLE = 3
    UPDATED = 4

class PageOrderByDirection(Enum):
    ASC = 0
    DESC = 1

class PageListItemOutput:
    __validation_list = [
        "id",
        "path",
        "locale",
        "title",
        "description",
        "contentType",
        "isPublished",
        "isPrivate",
        "privateNS",
        "createdAt",
        "updatedAt",
        "tags"
    ]
    
    def __init__(self, output: List[str]):
        for item in output:
            if not item in self.__validation_list:
                raise InvalidOutputError(item, self.__class__.__name__)
        self.output = output
    
    def __iter__(self):
        self.i = 0
        self.max = len(self.output)-1
        return self
    
    def __next__(self):
        if self.i <= self.max:
            result = self.i
            self.i += 1
            return self.output[result]
        else:
            raise StopIteration

class InvalidOutputError(Exception):
    def __init__(self, output: str, caller: str):
        self.output = output
        super().__init__(f"The given output parameter \"{output}\" is invalid for {caller}!")
