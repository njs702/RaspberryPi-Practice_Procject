from urllib.parse import urlencode
import requests
import json

url = "http://data.ex.co.kr/openapi/odtraffic/trafficAmountByRealtime"
queryString = "?" + urlencode(
    {
        "key" : "2412828365",
        "type" : "json"
    }
)
my_query_string_list = []
my_query_string = "영동선 속사 IC 교통상황 알려 줘"
my_query_string_list = my_query_string.split(" ")
print(my_query_string_list)
my_query_routeName = my_query_string_list[0]
my_query_cozoneName = my_query_string_list[1]

response = requests.get(url + queryString)
r_dict = json.loads(response.text)
r_item = r_dict.get("list")

result = {}

for item in r_item:
    if item.get("routeName") == my_query_routeName and my_query_cozoneName in item.get("conzoneName"):
        result = item
        break

if my_query_string_list[-3] == "교통상황" and my_query_string_list[-2] == "알려" and my_query_string_list[-1] == "줘": 
    my_response_string = "현재 " + my_query_routeName + " " + my_query_cozoneName + " 지역의 속도는 " + result['speed'] + " 이고, 차량 트래픽은 " + result['trafficAmout'] + " 입니다." 
    print(my_response_string)