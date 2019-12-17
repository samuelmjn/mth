import pymongo
from bson.objectid import ObjectId
from repository.branch_model import Branch, to_obj

class BranchRepository():
    def __init__(self, db: pymongo.MongoClient, db_name:str):
        self.db = db
        self.collection = db[db_name]["branches"]

    def create(self, req: Branch):
        req_dict = req.__dict__
        x = self.collection.insert_one(req_dict)
        return x.inserted_id

    def find_all(self):
        res = []
        for i in self.collection.find():
            res.append(to_obj(i))
        
        return res

    def find_by_id(self, branch_id):
        res = self.collection.find_one({"_id": ObjectId(branch_id)})
        return to_obj(res)