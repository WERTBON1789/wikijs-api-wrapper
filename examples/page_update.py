from wikijspy import Configuration, PagesApi, ApiClient
from wikijspy.types.page_types import PageResponseOutput

import json



with open('examples/settings.json', 'r') as f:
    settings_dict = json.loads(f.read())
    WIKIJS_HOST = settings_dict["hostname"]
    TOKEN = settings_dict["token"]

conf = Configuration(WIKIJS_HOST, TOKEN)

pages_api = PagesApi(ApiClient(conf))

print(pages_api.update(PageResponseOutput({
    "responseResult": [
        "message",
        "errorCode"
    ],
    "page": [
        "title",
        "id"
    ]
}),
    id=10637,
    isPrivate=True,
    isPublished=True
))
