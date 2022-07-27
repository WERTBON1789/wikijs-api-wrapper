from wikijspy.api_client import ApiClient

class UsersApi:
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = ApiClient
    
    def list(self, output, filter: str, orderBy: str):
        pass
    def search(self, output, query: str):
        pass
    def single(self, output, id: int):
        pass
    def profile(self, output):
        pass
    def lastLogins(self, output):
        pass
