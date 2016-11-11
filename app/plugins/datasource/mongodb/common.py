#  Copyright (C) 2016  Jamie Acosta, Jennifer Weand, Juan Soto, Mark Eby, Mark Smith, Andres Olivas
#
# This file is part of DssVisualizer.
#
# DssVisualizer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DssVisualizer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DssVisualizer.  If not, see <http://www.gnu.org/licenses/>.

import pymongo
import ujson
import pytz
from datetime import datetime
from tzlocal import get_localzone
from bson.json_util import dumps

class Common:
    """Here lies some common functions so they don't have to continue to be written over and over again."""

    def formatEpochDatetime(self, epoch):
        """Formats an epoch in UTC ISO_8601 format

        :param epoch: The epoch from MongoDB (date in milliseconds)
        :type epoch: long
        :returns: UTC ISO_8601 formatted date
        """
        stringTime =  datetime.fromtimestamp(epoch / 1e3).isoformat()
        return stringTime.replace('T', ' ')

    def getDatetimeFormatString(self):
        """Returns the string of how we want to format dates

        :returns: format string
        """
        return '%Y-%m-%d %H:%M:%S'

    def getDatabase(self):
        """Keep the database named in only one location. It helps keep typos down and
        creating a bunch of different databases and mass confusion when the computer
        is doing exactly what you're telling it to instead of what you want it to.

        :returns: MongoDB Database
        """
        client = pymongo.MongoClient()
        return client.dssvisualizer

    def formatOutput(self, cursor):
        """Dump the MongoDB cursor into bson and load it into an object for manipulation.

        :param cursor: The documents that MongoDb returns
        :type cursor: documents
        :returns: Python object (list)
        """
        objects = self.getPythonObjects(cursor)

        for obj in objects:
            obj["id"] = obj["_id"]["$oid"]
            obj["metadata"]["importDate"] = self.formatEpochDatetime(obj["metadata"]["importDate"]["$date"])

            try:
                obj["start"] = self.formatEpochDatetime(obj["start"]["$date"])
            except KeyError:
                obj["x"] = self.formatEpochDatetime(obj["x"]["$date"])

        return objects

    def getPythonObjects(self, cursor):
        bsonResult = dumps(cursor)
        return ujson.loads(bsonResult)

    def updateTechAndEventNames(self, startDate, endDate, techName, eventName, hasStartDate, hasXdate):
        """Updates tech name and event name depending on what is found in the database

        :param starDate: Start of date range
        :type startDate: datetime
        :param endDate: End of date range
        :type endDate: datetime
        :param techName: Name of technician
        :type techName: string
        :param eventName: Name of event where data was gathered
        :type eventName: string
        :param hasStartDate: If json file has start field
        :type hasStartDate: boolean
        :param hasXdate: If json file has x field instead of start field
        :type hasXdate: boolean
        :returns: mongoDB command with updated variables
        """
        if hasStartDate:
            findJson = {"start": {"$gte" : startDate, "$lte": endDate}}

        if hasXdate:
            findJson = {"x": {"$gte" : startDate, "$lte": endDate}}

        if len(techName) > 0 :
            findJson["metadata.techName"] = techName
        if len(eventName) > 0:
            findJson["metadata.eventName"] = eventName
        return findJson

    def addIndex(self, collection, hasStart):
        """Adds an index to the collection if it does not already exist

        :param collection: The collection to add the index to
        :type collection: MongoDB collection
        :param hasStart: True if the date to search by is 'start' otherwise it's assumed to be 'x'
        :type hasStart: boolean
        :return:
        """

        if hasStart:
            collection.create_index([("start", pymongo.ASCENDING),
                                     ("metadata.techName", pymongo.ASCENDING),
                                     ("metadata.eventName", pymongo.ASCENDING)], background=True)
        else:
            collection.create_index([("x", pymongo.ASCENDING),
                                     ("metadata.techName", pymongo.ASCENDING),
                                     ("metadata.eventName", pymongo.ASCENDING)], background=True)
