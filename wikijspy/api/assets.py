from wikijspy import ApiClient
from wikijspy.types.assets_types import *
from wikijspy.api.shared import _generate_output_str
from wikijspy.types.general import DefaultResponseOutput
import json


class AssetsApi:
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    def list(self, output: AssetItemOutput, folderId: int, kind: AssetKind):
        query = """
        query($folderId: Int!, $kind: AssetKind!){
            assets{
                list(
                    folderId: $folderId,
                    kind: $kind
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))
        
        return self.api_client.send_request(query, json.dumps({
            "folderId": folderId,
            "kind": kind
        }))
    
    def folders(self, output: AssetFolderOutput, parentFolderId: int):
        query = """
        query($parentFolderId: Int!){
            assets{
                folders(
                    parentFolderId: $parentFolderId
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))
        
        return self.api_client.send_request(query, json.dumps({
            "parentFolderId": parentFolderId
        }))
    
    def createFolder(self, output: DefaultResponseOutput, parentFolderId: int, slug: str, name: str = None):
        query = """
        mutation($parentFolderId: Int!, $slug: String!, $name: String){
            assets{
                createFolder(
                    parentFolderId: $parentFolderId,
                    slug: $slug,
                    name: $name
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))

        self.api_client.send_request(query, json.dumps({
            "parentFolderId": parentFolderId,
            "slug": slug,
            "name": name
        }))

    def renameAsset(self, output: DefaultResponseOutput, id: int, filename: str):
        query = """
        mutation($id: Int!, $filename: String!){
            assets{
                renameAsset(
                    id: $id,
                    filename: $filename
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))

        self.api_client.send_request(query, json.dumps({
            "id": id,
            "filename": filename
        }))

    def deleteAsset(self, output: DefaultResponseOutput, id: int):
        query = """
        mutation($id: Int!){
            assets{
                deleteAsset(
                    id: $id
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))

        self.api_client.send_request(query, json.dumps({
            "id": id
        }))

    def flushTempUploads(self, output: DefaultResponseOutput):
        query = """
        mutation{
            assets{
                flushTempUploads{
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))

        self.api_client.send_request(query)




