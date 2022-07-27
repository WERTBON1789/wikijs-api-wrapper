from enum import Enum
from typing import Any, Dict, List, Tuple
from wikijspy.types.error import InvalidOutputError
from wikijspy.types.general import ResponseStatusOutput, Output, DictOutput

class PageOrderBy(Enum):
    CREATED = 0
    ID = 1
    PATH = 2
    TITLE = 3
    UPDATED = 4

class PageOrderByDirection(Enum):
    ASC = 0
    DESC = 1

class PageListItemOutput(Output):
    _validation_list = [
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
            if not item in self._validation_list:
                raise InvalidOutputError(item, self.__class__.__name__)
        self.output = output

class PageOutput(Output):
    _validation_list = [
        "id",
        "path",
        "hash",
        "title",
        "description",
        "isPrivate",
        "isPublished",
        "privateNS",
        "publishStartDate",
        "publishEndDate",
        "tags",
        "content",
        "render",
        "toc",
        "contentType",
        "createdAt",
        "updatedAt",
        "editor",
        "locale",
        "scriptCss",
        "scriptJs",
        "authorId",
        "authorName",
        "authorEmail",
        "creatorId",
        "creatorName",
        "creatorEmail"
    ]
    
    def __init__(self, output: List[str]):
        for item in output:
            if not item in self._validation_list:
                raise InvalidOutputError(item, self.__class__.__name__)
        self.output = output

class PageResponseOutput(DictOutput):
    _validation_list = {
        "responseResult": ResponseStatusOutput._validation_list,
        "page": PageOutput._validation_list
    }
    
    def __init__(self, output: Dict[str, List[str]]):
        if not output.get("page") and not output.get("responseResult"):
            raise Exception(f"{self.__class__.__name__} does need to have at least one output!")
        
        for item in output:
            if not isinstance(output[item], list):
                raise Exception(f"Value of dict[\"{item}\"] must be of list type!")
            
            if not item in self._validation_list:
                raise InvalidOutputError(val, self.__class__.__name__)
            
            for val in output[item]:
                if not val in ResponseStatusOutput._validation_list and not val in PageOutput._validation_list:
                    raise InvalidOutputError(val, self.__class__.__name__)
        
        self.output = output
        
        self.iter_dict = []
        
        for element in self.output:
            for item in self.output[element]:
                self.iter_dict.append((element, item))
