from pymongo import MongoClient


class BSMongo:
    def __init__(self, conn_string: str, db_name: str):
        self.client = MongoClient(conn_string)
        self.db = self.client[db_name]

    def insert_one(self, collection, document):
        return self.db[collection].insert_one(document)

    def find_one(self, collection, query):
        return self.db[collection].find_one(query)

    def find(self, collection, query):
        return self.db[collection].find(query)

    def update_one(self, collection, query, update):
        return self.db[collection].update_one(query, update)

    def delete_one(self, collection, query):
        return self.db[collection].delete_one(query)
