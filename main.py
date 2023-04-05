import json

data_json = json.dumps(json.load(open(".src/utils/url.json")), indent=2)

print(data_json)