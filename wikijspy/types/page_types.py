from enum import Enum

class PageOrderBy(Enum):
    CREATED = 0
    ID = 1
    PATH = 2
    TITLE = 3
    UPDATED = 4

class PageOrderByDirection(Enum):
    ASC = 0
    DESC = 1