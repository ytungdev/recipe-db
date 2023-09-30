import pymongo
from bson.json_util import dumps


class Connection:
    def __init__(self) -> None:
        self.client = pymongo.MongoClient("mongodb://localhost:27017/") 
        self.db = self.client["recipe-db"] 

    def test(self) -> list:
        res = self.client.list_database_names() 
        return res
    
    def save(self, collection, obj) -> None:
        query = { "$or": [ { "name": obj.name }, { "name_alt": obj.name } ] }
        values = { "$set": obj.format() } 
        x = self.db[collection].update_one(query, values, upsert=True)
        print(f'matched  : {x.matched_count}')
        print(f'modified : {x.modified_count}')
        return

    def findRecipe(self, name):
        query = { "$or": [ 
            { "name": {
                "$regex": name,
                "$options" :'i'
            }}, 
            { "name_alt": {
                "$regex": name,
                "$options" :'i'
            }} 
        ]}
        x = self.db['recipes'].find_one(query)
        return dumps(x)

    def list_collection(self, collection) -> list:
        res = self.db[collection].find()
        return dumps(res)