from typing import List
from wikijspy.api_client import ApiClient
from wikijspy.types.page_types import PageOrderBy, PageOrderByDirection, PageListItemOutput, PageResponseOutput
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
    
    def create(self,
        output: PageResponseOutput,
        content: str,
        description: str,
        editor: str,
        isPublished: bool,
        isPrivate: bool,
        locale: str,
        path: str,
        tags: List[str],
        title: str,
        publishEndDate: str = None,
        publishStartDate: str = None,
        scriptCss: str = None,
        scriptJs: str = None,
    ):
        
        output_str = ""
        
        output_dict = {
            "responseResult": [],
            "page": []
        }
        
        for i in output:
            output_dict[i[0]].append(i[1])
        
        for key,val in output_dict.items():
            if not val:
                continue
            
            output_str += key+'{'
            
            for i in val:
                output_str += i+','
            output_str += '}'
        
        
        print(output_str)
        
        query = """
        mutation($content: String!, $description: String!, $editor: String!, $isPublished: Boolean!, $isPrivate: Boolean!, $locale: String!, $path: String!, $publishEndDate: Date, $publishStartDate: Date, $scriptCss: String, $scriptJs: String, $tags: [String]!, $title: String!){
            pages{
                create(
                    content: $content,
                    description: $description,
                    editor: $editor,
                    isPublished: $isPublished,
                    isPrivate: $isPrivate,
                    locale: $locale,
                    path: $path,
                    publishEndDate: $publishEndDate,
                    publishStartDate: $publishStartDate,
                    scriptCss: $scriptCss,
                    scriptJs: $scriptJs,
                    tags: $tags,
                    title: $title
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', output_str)
        return self.api_client.send_request(query, json.dumps({
            "content": content,
            "description": description,
            "editor": editor,
            "isPublished": isPublished,
            "isPrivate": isPrivate,
            "locale": locale,
            "path": path,
            "tags": tags,
            "title": title,
            "publishEndDate": publishEndDate,
            "publishStartDate": publishStartDate,
            "scriptCss": scriptCss,
            "scriptJs": scriptJs
        }))
        
        
    
