from typing import List
from wikijspy.api_client import ApiClient
from wikijspy.types.general import DefaultResponseOutput
from wikijspy.types.users_types import UserMinimalOutput, UserOutput, UserResponseOutput

class UsersApi:
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = ApiClient
    
    def list(self, output: UserMinimalOutput, filter: str, orderBy: str):
        pass
    def search(self, output: UserMinimalOutput, query: str):
        pass
    def single(self, output: UserOutput, id: int):
        pass
    def profile(self, output):
        pass
    def lastLogins(self, output):
        pass
    def create(self, output: UserResponseOutput, email: str, name: str, providerKey: str, passwordRaw: str = None, groups: List[int] = [], mustChangePassword: bool = False, sendWelcomeEmail: bool = False):
        pass
    def update(self, output: DefaultResponseOutput, id: int, email: str = None, name: str = None, newPassword: str = None, groups: List[int] = None, location: str = None, jobTitle: str = None, timezone: str = None, dateFormat: str = None, appearance: str = None):
        pass
    def delete(self, output: DefaultResponseOutput, id: int, replaceId: int):
        pass
    def verify(self, output: DefaultResponseOutput, id: int):
        pass
    def activate(self, output: DefaultResponseOutput, id: int):
        pass
    def deactivate(self, output: DefaultResponseOutput, id: int):
        pass
    def enableTFA(self, output: DefaultResponseOutput, id: int):
        pass
    def disableTFA(self, output: DefaultResponseOutput, id: int):
        pass
    def resetPassword(self, output: DefaultResponseOutput, id: int):
        pass
    def updateProfile(self, output):
        pass
    def changePassword(self, output):
        pass
