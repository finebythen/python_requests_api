import requests
import pandas as pd

"""
Rest-API for testing: https://gorest.co.in/
"""

search_id = 123

api_base_url = "https://gorest.co.in"
endpoint_path = f"/public-api/users/{search_id}"
endpoint = f"{api_base_url}{endpoint_path}"

r = requests.get(endpoint)

print(r.status_code)
print(r.text)

r_json = r.json()

print(r_json['code'])
print(r_json['data']['name'])


# --> convert json into dataframe (pandas)
# df = pd.DataFrame.from_dict(r_json, orient='columns')  # --> without nested data in json-file
# df = pd.DataFrame.from_dict(pd.json_normalize(r_json), orient='columns')  # --> with nested data in json-file

