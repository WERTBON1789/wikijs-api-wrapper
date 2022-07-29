


from enum import Enum
from wikijspy.types.general import Output

class AssetKind(Enum):
    IMAGE = 0
    BINARY = 1
    ALL = 2

class AssetItemOutput(Output):
    _validation_list = [
        "id",
        "filename",
        "ext",
        "kind",
        "mime",
        "fileSize",
        "metadata",
        "createdAt",
        "updatedAt",
        "folder",
        "author"
    ]

class AssetFolderOutput(Output):
    _validation_list = [
        "id",
        "slug",
        "name"
    ]
