import requests
import json

headers={'Content-type': 'application/json', 'Accept': 'text/plain'}
url_api='http://127.0.0.1:5000/1'

content_json={"Valor":"79","idpos":"asd","huella":"asdasd"}
content=json.dumps(content_json)
#resp = requests.get(url_api,headers=header)

resp =requests.post(url_api, data=content_json)
print(resp)