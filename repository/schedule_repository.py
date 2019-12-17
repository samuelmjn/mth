import pymongo
from repository.schedule_model import Schedule, to_obj

class ScheduleRepository():
    def __init__(self, db: pymongo.MongoClient, db_name:str):
        self.db = db
        self.collection = db[db_name]["schedules"]

    def create(self, req: Schedule):
        req_dict = req.__dict__
        x = self.collection.insert_one(req_dict)
        return x.inserted_id

    def find_all(self):
        res = []
        for i in self.collection.find():
            res.append(to_obj(i))
        
        return res

    def find_by_user_id(self, user_id):
        res = []
        for i in self.collection.find({"$or":[{"worship_leader":user_id},{"keyboard":user_id},{"bass":user_id},{"drum":user_id},{"e_guitar":user_id},{"acc_guitar":user_id},{"aux_keys":user_id}]}):
            res.append(to_obj(i))

        return res