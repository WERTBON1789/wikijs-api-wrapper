from typing import List
from wikijspy.api_client import ApiClient
from wikijspy.types.page_types import PageOrderBy, PageOrderByDirection, PageListItemOutput
import json

class PagesApi:
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    def list(self,
             output: PageListItemOutput,
             authorId: int = None,
             creatorId: int = None,
             limit: int = None,
             locale: str = None,
             orderBy: PageOrderBy = None,
             orderByDirection: PageOrderByDirection = None,
             tags: List[str] = None
             ):
        
        output_str: str = ""
        
        for item in output:
            output_str += item+","
        
        query = """
        query($authorId: Int, $creatorId: Int, $limit: Int, $locale: String, $orderBy: PageOrderBy, $orderByDirection: PageOrderByDirection, $tags: [String!]){
                pages {
                    list(
                        authorId: $authorId,
                        creatorId: $creatorId,
                        limit: $limit,
                        locale: $locale,
                        orderBy: $orderBy,
                        orderByDirection: $orderByDirection,
                        tags: $tags
                    ){
                        OUTPUT
                    }
                }
        }
        """.replace('OUTPUT', output_str)
        
        return self.api_client.send_request(query, json.dumps({
                "authorId": authorId,
                "creatorId": creatorId,
                "limit": limit,
                "locale": locale,
                "orderBy": orderBy,
                "orderByDirection": orderByDirection,
                "tags": tags
        }))
