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
