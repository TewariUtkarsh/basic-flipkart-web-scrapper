import pymongo


class DB_operation:

    def __init__(self):
        self.password = "Kavita19"
        self.client = None

    def create_client(self):
        client = pymongo.MongoClient(f"mongodb+srv://tewariutkarsh:{self.password}@cluster0.plsxw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.client = client.test

    def create_database(self, db_name):
        database = self.client[db_name]
        return database

    def create_collection(self, database, coll_name):
        collection = database[coll_name]
        return collection

    def insert_record(self, collection, record):
        collection.insert_one(record)

    def delete_record(self, collection):
        rec = collection.find().sort({'_id':-1}).limit(1)
        collection.delete_one(rec)


