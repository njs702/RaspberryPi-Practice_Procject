import os
from urllib.parse import urlencode
import requests
import json

# 인증키 : 6ed17cf124c83b31abe1be252d04abcf 
# https://www.eshare.go.kr/eshare-openapi/rsrc/list/자원분류코드/인증키
# 주차장 자원분류코드 : 010700
# https://www.eshare.go.kr/OpenApi/Info/detail.do?svcNo=15

url = "https://www.eshare.go.kr/eshare-openapi/rsrc/list/010700/6ed17cf124c83b31abe1be252d04abcf"
#url = "https://www.eshare.go.kr/OpenApi/Info/detail.do?svcNo=15/010700/6ed17cf124c83b31abe1be252d04abcf"
headers = {
    'Content-Type': 'aapplication/json; charset=utf-8',
    'Accept': '*/*'    
}

response = requests.get(url,headers=headers)
print(response)
