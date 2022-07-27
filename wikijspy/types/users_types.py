from typing import Dict, List
from wikijspy.types.error import InvalidOutputError
from wikijspy.types.general import DictOutput, Output, ResponseStatusOutput
from wikijspy.types.page_types import PageOutput

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

class UserResponseOutput(DictOutput):
    _validation_list = {
        "responseResult": ResponseStatusOutput._validation_list,
        "user": UserOutput._validation_list
    }
