import pymongo
from bson.objectid import ObjectId
from repository.user_model import User, to_obj

class UserRepository():
    def __init__(self, db: pymongo.MongoClient, db_name:str):
        self.db = db
        self.collection = db[db_name]["users"]

    def create(self, req: User):
        req_dict = req.__dict__
        x = self.collection.insert_one(req_dict)
        return x.inserted_id

    def find_by_id(self, user_id):
        user = self.collection.find_one({"_id": ObjectId(user_id)})
        return to_obj(user)

    def find_all(self):
        res = []
        for i in self.collection.find():
            res.append(to_obj(i))
        return res