from urllib.parse import urlencode
import requests
import json

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'

queryString = "?" + urlencode(
    {
        'serviceKey' : 'A8UdFEpNexXhl7piKrkDM8PtyYFkOLeJCO5KPn6KjbuJWKsFNMhH90+zHwcc4nSORe4z7yCkGAtjpvCwmMwEaw==', 
        'pageNo' : '1', 
        'numOfRows' : '1000', 
        'dataType' : 'JSON', 
        'base_date' : '20220405', 
        'base_time' : '0600', 
        'nx' : '55', 
        'ny' : '127' 
    }
)

response = requests.get(url + queryString)
print("===== response json data start =====")
print(response)
print("===== response json data end =====")
print()

r_dict = json.loads(response.text)
r_response = r_dict.get("response")
r_body = r_response.get("body")
r_items = r_body.get("items")
r_item = r_items.get("item")
result = {}
for item in r_item:
    if(item.get("category") == "T1H"):
        result = item
        break

print("===== response dictionary(python obj) data start =====")
print(result)
print(" ===== response dictionary(python obj) data end ===== ")
print()