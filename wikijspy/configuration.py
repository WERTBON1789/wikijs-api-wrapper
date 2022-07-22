
class Configuration:
    def __init__(self, hostname: str, api_token: str):
        self.hostname = hostname
        self.token = api_token
    
    @property
    def hostname(self) -> str:
        return self.__hostname
    
    @hostname.setter
    def hostname(self, value: str):
        self.__hostname = value
    
    @property
    def token(self) -> str:
        return self.__token
    
    @token.setter
    def token(self, value: str):
        self.__token = value
