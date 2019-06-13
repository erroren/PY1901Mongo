from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float
import requests
import json
import pymongo

engine = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/info", encoding='utf8', echo=True)
Base = declarative_base()


class Hotcitys(Base):
    __tablename__ = 'hotcitys'
    cid = Column(String(50), primary_key=True, nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)


Session = sessionmaker(bind=engine)
session = Session()
citys = session.query(Hotcitys.cid).all()
table = pymongo.MongoClient()['infos']['hotcitys']
for v in citys:
    result = requests.post("https://free-api.heweather.net/s6/weather/forecast?", data={
            "location": v[0], "key": "20a494ba265d47abafc3adc45dc889f0"
    })
    cityinfo = json.loads(result.text)['HeWeather6'][0]['daily_forecast'][0]
    table.insert_one({"cid": v[0], "tmp_max": cityinfo['tmp_max'], "tmp_min": cityinfo['tmp_min']})
res = table.find({})
for cur in res:
    print(cur)
