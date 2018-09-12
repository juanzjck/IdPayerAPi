import requests
import json

# importing the requests library
import requests

# api-endpoint


headers={'Content-type': 'application/json', 'Accept': 'text/plain'}
#url_api='http://192.168.40.57:5000/1'
url_api='http://192.168.4.254:5000/pos/4'


content_json={"Valor":"79","idpos":"asd","huella":"sdas334","PIN":"0224"}
content=json.dumps(content_json)
#resp = requests.get(url_api,headers=header)

resp =requests.post(url_api, data=content_json)
#resp.status_code
#200
#resp.headers['content-type']
#text/json
#resp.encoding
#resp.json()
#mensaje en jsnon
print(resp.json())