import pymongo
import requests
import json
table = pymongo.MongoClient()["info"]["hotcitys"]
result = requests.post("https://search.heweather.net/top?", data={
    "group": "cn",
    "key": "20a494ba265d47abafc3adc45dc889f0",
    "number": 30
})
cityinfo = json.loads(result.text)['HeWeather6'][0]['basic']
for v in cityinfo:
    print(v)
    table.insert_one({"cid": v['cid'], "lat": v['lat'], "lon": v['lon']})
res = table.find({})
for cur in res:
    print(cur)
