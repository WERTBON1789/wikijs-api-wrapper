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
    
    
    def __init__(self, output: Dict[str, List[str]]):
        if not isinstance(output, dict):
            raise Exception(f"{self.__class__.__name__} needs an dictionary as parameter!")
        if not output.keys() in self._validation_list.keys():
            raise InvalidOutputError(','.join(list(output.keys())), self.__class__.__name__)
        
        if not (self._validation_list.keys()[0] in output or self._validation_list.keys()[1] in output):
            raise Exception(f"{self.__class__.__name__} needs at least one of these dict keys: {','.join(list(self._validation_list.keys()))}")
        
        for key,val in output.items():
            if not isinstance(val, list):
                raise Exception(f"{self.__class__.__name__} values behind the dict keys must be of type list!")

            for item in val:
                if not item in self._validation_list[key]:
                    raise InvalidOutputError(item, self.__class__.__name__)
        
        self.output = output
        
        self.iter_dict = []
        
        for element in self.output:
            for item in self.output[element]:
                self.iter_dict.append((element, item))