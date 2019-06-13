from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float
import requests
import json


engine = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/info", encoding='utf8', echo=True)
Base = declarative_base()


class Hotcitys(Base):
    __tablename__ = 'hotcitys'
    cid = Column(String(50), primary_key=True, nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)


# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
result = requests.post("https://search.heweather.net/top?", data={
    "group": "cn",
    "key": "20a494ba265d47abafc3adc45dc889f0",
    "number": 30
})
cityinfo = json.loads(result.text)['HeWeather6'][0]['basic']
for v in cityinfo:
    session.add(Hotcitys(cid=v['cid'], lat=v['lat'], lon=v['lon']))
    session.commit()
session.close()
