from typing import List
from wikijspy.types.error import InvalidOutputError
from wikijspy.types.general import Output

class UserMinimalOutput(Output):
    _validation_list = [
        "id",
        "name",
        "email",
        "providerKey",
        "isSystem",
        "isActive",
        "createdAt",
        "lastLoginAt"
    ]
    
    def __init__(self, output: List[str]) -> None:
        for item in output:
            if not item in self._validation_list:
                raise InvalidOutputError(item, self.__class__.__name__)
        self.output = output

class UserOutput(Output):
    _validation_list = [
        "id",
        "name",
        "email",
        "providerKey",
        "providerName",
        "providerId",
        "providerIs2FACapable",
        "isSystem",
        "isActive",
        "isVerified",
        "location",
        "jobTitle",
        "timezone",
        "dateFormat",
        "appearance",
        "createdAt",
        "updatedAt",
        "lastLoginAt",
        "tfaIsActive",
        "groups"
    ]
    
    def __init__(self, output: List[str]) -> None:
        for item in output:
            if not item in self._validation_list:
                raise InvalidOutputError(item, self.__class__.__name__)
        self.output = output
