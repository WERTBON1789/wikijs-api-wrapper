from typing import Dict, List, Tuple
from wikijspy.api_client import ApiClient
from wikijspy.types.page_types import PageOrderBy, PageOrderByDirection, PageListItemOutput, PageOutput, PageResponseOutput
from wikijspy.types.general import DefaultResponseOutput, ResponseStatusOutput
import re
import json

def _generate_output_str(output) -> str:
    if type(output[0]) is str:
        output_str: str = ""
        for item in output:
            output_str += item+","
        return output_str
    if isinstance(output[0], Tuple):
        output_str: str = ""
        output_dict: Tuple[str, str] = {}
        
        for item in output:
            if output_dict.get(item[0]) is None:
                output_dict[item[0]] = []
            output_dict[item[0]].append(item[1])
        
        for key,val in output_dict.items():
            if not val:
                continue
            
            output_str += key+'{'
            
            for item in val:
                output_str += item+','
            output_str += '}'
        return output_str


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
        """.replace('OUTPUT', _generate_output_str(output))
        
        return self.api_client.send_request(query, json.dumps({
                "authorId": authorId,
                "creatorId": creatorId,
                "limit": limit,
                "locale": locale,
                "orderBy": orderBy,
                "orderByDirection": orderByDirection,
                "tags": tags
        }))
    
    def single(self,
        output: PageOutput,
        id: int
    ):
        query = """
        query($id: Int!){
            pages{
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
        """.replace('OUTPUT', _generate_output_str(output))
        
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
        
    def update(self,
        output: PageResponseOutput,
        id: int,
        content: str = None,
        description: str = None,
        editor: str = None,
        isPrivate: bool = None,
        isPublished: bool = None,
        locale: str = None,
        path: str = None,
        publishEndDate: str = None,
        publishStartDate: str = None,
        scriptCss: str = None,
        scriptJs: str = None,
        tags: List[str] = [],
        title: str = None
    ):
        query = """
        mutation($id: Int!, $content: String, $description: String, $editor: String, $isPrivate: Boolean, $isPublished: Boolean, $locale: String, $path: String, $publishEndDate: Date, $publishStartDate: Date, $scriptCss: String, $scriptJs: String, $tags: [String], $title: String) {
            pages {
                update(
                    id: $id
                    content: $content
                    description: $description
                    editor: $editor
                    isPrivate: $isPrivate
                    isPublished: $isPublished
                    locale: $locale
                    path: $path
                    publishEndDate: $publishEndDate
                    publishStartDate: $publishStartDate
                    scriptCss: $scriptCss
                    scriptJs: $scriptJs
                    tags: $tags
                    title: $title
                ){
                    OUTPUT
                }
            }
        }
        """.replace('OUTPUT', _generate_output_str(output))
        
        if content is None:
            content = self.single(PageOutput(["content"]), id)["pages"]["single"]["content"]
        
        split_query = query.split("\n")
        
        for key,val in locals().items():
            if val is None:
                split_query[0] = re.sub(r"\$.+, ", "", split_query[0])
                for index,line in enumerate(split_query):
                    if not re.search(f" +{key}: \$\w+", line) is None:
                        split_query[index] = ""
        
        all_vars = {
            "id": id,
            "content": content,
            "description": description,
            "editor": editor,
            "isPrivate": isPrivate,
            "isPublished": isPublished,
            "locale": locale,
            "path": path,
            "publishEndDate": publishEndDate,
            "publishStartDate": publishStartDate,
            "scriptCss": scriptCss,
            "scriptJs": scriptJs,
            "tags": tags,
            "title": title
        }
        
        query_variables = {}
        
        for key,val in all_vars.items():
            if not val is None:
                query_variables[key] = val
                
        return self.api_client.send_request(query, json.dumps(query_variables))
    
    def delete(self,
        output: DefaultResponseOutput,
        id: int
    ):
        query = """
        mutation($id: Int!){
            pages{
                delete(
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
    
    def render(self,
        output: DefaultResponseOutput,
        id: int
    ):
        query = """
        mutation($id: Int!){
            pages{
                render(
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
