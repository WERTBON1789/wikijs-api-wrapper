import json
from typing import List
from wikijspy.api_client import ApiClient
from wikijspy.types.general import DefaultResponseOutput
from wikijspy.types.users_types import UserMinimalOutput, UserOutput, UserResponseOutput
from wikijspy.api.shared import _generate_output_str

class UsersApi:
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client
    
    def list(self, output: UserMinimalOutput, filter: str = None, orderBy: str = None):
        query = """
        query($filter: String, $orderBy: String){
            users{
                list(
                    filter: $filter,
                    orderBy: $orderBy
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))

        return self.api_client.send_request(query, json.dumps({
            "filter": filter,
            "orderBy": orderBy
        }))
        
    def search(self, output: UserMinimalOutput, query: str):
        gql_query = """
        query($query: String!){
            users{
                search(
                    query: $query
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))
        
        return self.api_client.send_request(gql_query, json.dumps({
            "query": query
        }))
    def single(self, output: UserOutput, id: int):
        query = """
        query($id: Int!){
            users{
                single(
                    id: $id 
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))

        return self.api_client.send_request(query, json.dumps({
            "id": id
        }))
    def profile(self, output):
        query = """
        query{
            users{
                profile{
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))

        return self.api_client.send_request(query)
    def lastLogins(self, output):
        query = """
        query{
            users{
                lastLogins{
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))

        return self.api_client.send_request(query)
    def create(self, output: UserResponseOutput, email: str, name: str, providerKey: str, passwordRaw: str = None, groups: List[int] = [], mustChangePassword: bool = False, sendWelcomeEmail: bool = False):
        query = """
        mutation($email: String!, $name: String!, $passwordRaw: String, $providerKey: String!, $groups: [Int]!, $mustChangePassword: Boolean, $sendWelcomeEmail: Boolean){
            users{
                create(
                    email: $email
                    name: $name
                    passwordRaw: $passwordRaw
                    providerKey: $providerKey
                    groups: $groups
                    mustChangePassword: $mustChangePassword
                    sendWelcomeEmail: $sendWelcomeEmail
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))

        return self.api_client.send_request(query, json.dumps({
            "email": email,
            "name": name,
            "providerKey": providerKey,
            "passwordRaw": passwordRaw,
            "groups": groups,
            "mustChangePassword": mustChangePassword,
            "sendWelcomeEmail": sendWelcomeEmail
        }))
    def update(self, output: DefaultResponseOutput, id: int, email: str = None, name: str = None, newPassword: str = None, groups: List[int] = None, location: str = None, jobTitle: str = None, timezone: str = None, dateFormat: str = None, appearance: str = None):
        query = """
        mutation($id: Int!, $email: String, $name: String, $newPassword: String, $groups: [Int], $location: String, $jobTitle: String, $timezone: String, $dateFormat: String, $appearance: String){
            users{
                update(
                    id: $id
                    email: $email
                    name: $name
                    newPassword: $newPassword
                    groups: $groups
                    location: $location
                    jobTitle: $jobTitle
                    timezone: $timezone
                    dateFormat: $dateFormat
                    appearance: $appearance
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))

        return self.api_client.send_request(query, json.dumps({
            "id": id,
            "email": email,
            "name": name,
            "newPassword": newPassword,
            "groups": groups,
            "location": location,
            "jobTitle": jobTitle,
            "timezone": timezone,
            "dateFormat": dateFormat,
            "appearance": appearance
        }))
    def delete(self, output: DefaultResponseOutput, id: int, replaceId: int):
        query = """
        mutation($id: Int!, $replaceId: Int!){
            users{
                delete(
                    id: $id
                    replaceId: $replaceId
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))

        return self.api_client.send_request(query, json.dumps({
            "id": id,
            "replaceId": replaceId
        }))
    def verify(self, output: DefaultResponseOutput, id: int):
        query = """
        
        """.replace('OUTPUT', _generate_output_str(output))

        return self.api_client.send_request(query, json.dumps({
            "id": id
        }))
    def activate(self, output: DefaultResponseOutput, id: int):
        query = """
        mutation($id: Int!){
            users{
                activate(
                    id: $id
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))

        return self.api_client.send_request(query, json.dumps({
            "id": id
        }))
    def deactivate(self, output: DefaultResponseOutput, id: int):
        query = """
        mutation($id: Int!){
            users{
                deactivate(
                    id: $id
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))

        return self.api_client.send_request(query, json.dumps({
            "id": id
        }))
    def enableTFA(self, output: DefaultResponseOutput, id: int):
        query = """
        
        """.replace('OUTPUT', _generate_output_str(output))
    def disableTFA(self, output: DefaultResponseOutput, id: int):
        query = """
        
        """.replace('OUTPUT', _generate_output_str(output))
    def resetPassword(self, output: DefaultResponseOutput, id: int):
        query = """
        
        """.replace('OUTPUT', _generate_output_str(output))
    def updateProfile(self, output):
        pass
    def changePassword(self, output):
        pass
