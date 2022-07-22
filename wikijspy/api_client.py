import json
from wikijspy.configuration import Configuration
from gql.transport.requests import RequestsHTTPTransport
from gql.client import Client
from gql import gql


class ApiClient:
    def __init__(self, configuration: Configuration) -> None:
        self.client = configuration
    
    @property
    def client(self):
        return self.__client
    
    @client.setter
    def client(self, conf: Configuration):
        headers = {
            'Authorization': f'Bearer {conf.token}',
            'Content-Type': 'application/json'
        }
        
        self.transport = RequestsHTTPTransport(url=f"{conf.hostname}/graphql", headers=headers)
        self.__client = Client(transport=self.transport, fetch_schema_from_transport=True)

    def send_request(self, graphql_query: str, graphql_variables: str = None):
        if graphql_variables is None:
            return self.client.execute(gql(graphql_query))
        else:
            return self.client.execute(gql(graphql_query), json.loads(graphql_variables))
