from pymongo import MongoClient

class PyKeyLogger:

    def getDatabase(self):
        client = MongoClient()
        return client.jensTest

    def importKeypressData(self, json):
        collection = self.getDatabase().keypressData
        result = collection.insert_many(json)
        return len(result.inserted_ids)

    def importClick(self, json):
        collection = self.getDatabase().click
        result = collection.insert_one(json)
        return result.inserted_id

    def importTimed(self, json):
        collection = self.getDatabase().timed
        result = collection.insert_one(json)
        return result.inserted_id
