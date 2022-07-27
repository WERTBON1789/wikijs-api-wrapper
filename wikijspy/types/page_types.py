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


class PageResponseOutput(DictOutput):
    _validation_list = {
        "responseResult": ResponseStatusOutput._validation_list,
        "page": PageOutput._validation_list
    }
