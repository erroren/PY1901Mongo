import pymongo
# res = pymongo.MongoClient()["goods"]["user"].find({"gender": 0})
# print(res)
# for cur in res:
#     print(cur)
# pymongo.MongoClient()["goods"]["user"].update_one({"name": "aaa"}, {"$set": {"age": 30}})
res = pymongo.MongoClient()["goods"]["user"].find_one({"name": "aaa"})
print(res)
# pymongo.MongoClient()["goods"].authenticate('tempp', "123456")