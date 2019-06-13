import requests
import json
# response = requests.post(url="https://search.heweather.net/find?", data={
#             "location": "zhengzhou", "key": "20a494ba265d47abafc3adc45dc889f0"
# })
# content = response.text
# cityobj = json.loads(content)
# cityinfo = cityobj['HeWeather6'][0]['basic'][0]
# for i, j in cityinfo.items():
#     print(i, j)
res = requests.post("https://free-api.heweather.net/s6/weather/forecast?", data={
            "location": "zhengzhou", "key": "20a494ba265d47abafc3adc45dc889f0"
})
content = res.text
print(content)
cityobj = json.loads(content)
print(cityobj)
weatherinfo = cityobj['HeWeather6'][0]['daily_forecast']
for i in weatherinfo:
    for v, j in i.items():
        print(v, j)
    print('\r\n')
