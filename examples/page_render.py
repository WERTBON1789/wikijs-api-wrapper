from wikijspy import Configuration, ApiClient, PagesApi
from wikijspy.types.general import DefaultResponseOutput
import json

with open('examples/settings.json', 'r') as f:
    settings_dict = json.loads(f.read())
    WIKIJS_HOST = settings_dict["hostname"]
    TOKEN = settings_dict["token"]

conf = Configuration(WIKIJS_HOST, TOKEN)

pages_api = PagesApi(ApiClient(conf))

print(pages_api.render(DefaultResponseOutput({"responseResult": ["message"]}), 10636))
