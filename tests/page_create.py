from wikijspy import Configuration, ApiClient, PagesApi
from wikijspy.types.page_types import PageResponseOutput
import json

with open('tests/settings.json', 'r') as f:
    settings_dict = json.loads(f.read())
    WIKIJS_HOST = settings_dict["hostname"]
    TOKEN = settings_dict["token"]

conf = Configuration(WIKIJS_HOST, TOKEN)

pages_api = PagesApi(ApiClient(conf))

print(pages_api.create(PageResponseOutput({
    "responseResult": [
        "errorCode"
    ],
    "page": [
        "id"
    ]}),
    content="<a>Test</a>",
    description="Desc",
    editor="markdown",
    isPublished=True,
    isPrivate=True,
    locale="en",
    path="Geile",
    tags=[],
    title="Test"
    ))