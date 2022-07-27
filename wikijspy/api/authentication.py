import json
from wikijspy.api_client import ApiClient
from wikijspy.api.shared import _generate_output_str
from wikijspy.types.authentication_types import AuthenticationStrategyOutput, AuthenticationActiveStrategyOutput
class AuthenticationApi:
    
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    def strategies(self, output: AuthenticationStrategyOutput):
        query = """
        query{
            authentication{
                strategies{
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))

        return self.api_client.send_request(query)
    
    def activeStrategies(self, output: AuthenticationActiveStrategyOutput, enabledOnly: bool = None):
        query = """
        query($enabledOnly: Boolean){
            authentication{
                activeStrategies(
                    enabledOnly: $enabledOnly
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))
        
        return self.api_client.send_request(query, json.dumps({
            "enabledOnly": enabledOnly
        }))