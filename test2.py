import pymongo
import requests
import json
table = pymongo.MongoClient()["info"]["hotcitys"]
citys = table.find()
# print(citys)
for v in citys:
    # print(v['cid'])
    result = requests.post("https://free-api.heweather.net/s6/weather/forecast?", data={
            "location": v['cid'], "key": "20a494ba265d47abafc3adc45dc889f0"
    })
    cityinfo = json.loads(result.text)['HeWeather6'][0]['daily_forecast'][0]
    # print(cityinfo['tmp_max'])
    table.update_one({"cid": v['cid']}, {"$set": {"tmp_max": cityinfo['tmp_max'],
                                                  "tmp_min": cityinfo['tmp_min']}})
res = table.find({})
for cur in res:
    print(cur)
