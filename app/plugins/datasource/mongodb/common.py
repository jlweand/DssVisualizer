from datetime import datetime
from pymongo import MongoClient
from bson.json_util import dumps
import ujson

class Common:
    """Here lies some common functions so they don't have to continue to be written over and over again."""

    def formatDatetime(self, epoch):
        """Formats an epoch in UTC ISO_8601 format

        :param epoch: The epoch from MongoDB (date in milliseconds)
        :type epoch: long
        :returns: UTC ISO_8601 formatted date
        """
        return datetime.utcfromtimestamp(epoch / 1e3).isoformat()

    def getDatabase(self):
        """Keep the database named in only one location. It helps keep typos down and
        creating a bunch of different databases and mass confusion when the computer
        is doing exactly what you're telling it to instead of what you want it to.

        :returns: MongoDB Database
        """
        client = MongoClient()
        return client.dssvisualizer

    def formatOutput(self, cursor):
        """Dump the MongoDB cursor into bson and load it into an object for manipulation.

        :param cursor: The documents that MongoDb returns
        :type cursor: documents
        :returns: Python object (list)
        """
        bsonResult = dumps(cursor)
        objects = ujson.loads(bsonResult)
        return objects
