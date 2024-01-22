# 데이터명 : 조달청_나라장터 공공데이터개방표준서비스
# from https://www.data.go.kr/iim/api/selectAPIAcountView.do
import requests 

# url 주소 변수 지정
url = 'https://openapi.naver.com/v1/datalab/shopping/categories'

header1 = {'Host': 'openapi.naver.com',
           'X-Naver-Client-Id':'cRMNURzoedZxUwUyW0Hh',
           'X-Naver-Client-Secret':'87bY0YnCTe',
           'Content-Type': 'application/json',
           'Content-Length': '360'
           }
param1 = {
    "startDate": "2017-08-01",
    "endDate": "2017-09-30",
    "timeUnit": "month",
    "category": [
        {"name": "패션의류", "param": [ "50000000"]},
        {"name": "화장품/미용", "param": [ "50000002"]}
        ],
        "device": "pc",
        "gender": "f",
        "ages": [ "20",  "30"]
}

pass
# respose라는 변수로 받음
response = requests.post(url,json = param1, headers=header1) 
pass
# response의 내용을 출력
print(response.content) 

# json 파일을 dictionary 형태로 변환
import json
contents = json.loads(response.content)
pass



# # mongoDB 저장
# from pymongo import MongoClient
# # mongodb에 접속 -> 자원에 대한 class
# mongoClient = MongoClient("mongodb://localhost:27017")
# # database 연결
# database = mongoClient["data_go_kr"]
# # collection 작업
# collection = database['search_shop_info']
# # insert 작업 진행
# collection.delete_many({})
# result = collection.insert_one({'lastBulidDate': contents['lastBuildDate'],
#                                 'total':contents['total'],
#                                 'start':contents['start'],
#                                 'display':contents['display']})
# pass
# for i in range(len(contents['items'])):
#     contents['items'][i]['id_relative'] = result.inserted_id
# pass
# collection = database['serach_shop_list']
# collection.delete_many({})
# collection.insert_many(contents['items'])