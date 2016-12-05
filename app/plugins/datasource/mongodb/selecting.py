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

import ujson
from datetime import datetime
from plugins.datasource.mongodb.common import Common
from bson.json_util import dumps

class Selecting:
    """Here lies the logic for selecting and returning data.  It generates the select query and cleans up the data being returned."""

    def getSelectJsonQuery(self, startDate, endDate, techNames, eventNames, eventTechList, hasStartDate, hasXdate):
        """Generates the select query for searching on date, tech, and event names.

        :param startDate: Start of date range
        :type startDate: datetime
        :param endDate: End of date range
        :type endDate: datetime
        :param techNames: A list of technician names to search on
        :type techNames: list
        :param eventNames: A list of event names to search on
        :type eventNames: list
        :param eventTechList: A list of a combination of event and tech names to return data
        :type eventTechList: list
        :param hasStartDate: If json file has start field
        :type hasStartDate: boolean
        :param hasXdate: If json file has x field instead of start field
        :type hasXdate: boolean
        :returns: mongoDB search command
        """

        findJson = {}
        findJson["$and"] = []
        findJson["$and"].append(self.getStartJson(startDate, endDate, hasStartDate, hasXdate))

        if len(eventTechList) > 0:
            findJson["$and"].append(self.getComboEventTechJson(eventTechList))

        else:
            if len(techNames) > 0:
                findJson["$and"].append(self.getEventTechNamesJson(techNames, "metadata.techName"))
            if len(eventNames) > 0:
                findJson["$and"].append(self.getEventTechNamesJson(eventNames, "metadata.eventName"))

        return findJson

    def getStartJson(self, startDate, endDate, hasStartDate, hasXdate):
        """Get the json for the search dates.
        looks something like:
        {
          "start": {
            "$gte": datetime.datetime(2016, 10, 18, 6, 0, tzinfo=<UTC>)
            "$lte": datetime.datetime(2016, 10, 19, 5, 59, 59, tzinfo=<UTC>)
          }
        }

        :param startDate: Start of date range
        :type startDate: datetime
        :param endDate: End of date range
        :param hasStartDate: If json file has start field
        :type hasStartDate: boolean
        :param hasXdate: If json file has x field instead of start field
        :type hasXdate: boolean
        :return: the json for searching by date range
        """
        if hasStartDate:
            startJson = {"start": {"$gte": startDate, "$lte": endDate}}

        if hasXdate:
            startJson = {"x": {"$gte": startDate, "$lte": endDate}}

        return startJson

    def getComboEventTechJson(self, eventTechList):
        """Get the json for searching for the combinations of event/tech names.
        Looks something like:
        {
          $or: [
            {
              $and: [
                {"metadata.eventName":"Another Event"},
                {"metadata.techName":"Alex"}
              ]
            },
            {
              $and: [
                {"metadata.eventName":"Super Summer Event"},
                {"metadata.techName":"Tom"}
              ]
            }
          ]
        }

        :param eventTechList: A list of a combination of event and tech names to return data
        :type eventTechList: list
        :return: the json for searching on event/tech combinations
        """
        theOr = {}
        theOr["$or"] = []
        for eventTech in eventTechList:
            etl = eventTech.split(" by ")
            theAnd = {}
            theAnd["$and"] = []
            theAnd["$and"].append({"metadata.eventName": etl[0]})
            theAnd["$and"].append({"metadata.techName": etl[1]})
            theOr["$or"].append(theAnd)

        return theOr

    def getEventTechNamesJson(self, names, searchAttribute):
        """For a given list, creates the json for searching on all values.
        looks something like:
        {
          "$or": [
            {"metadata.eventName": "Another Event"},
            {"metadata.eventName": "Super Summer Event"}
          ]
        }

        :param names: A list of names (tech or event) to search on
        :type names: list
        :param searchAttribute: The attribute that we're searching on. 'metadata.techName' for example
        :type searchAttribute: string
        :return: the json for searching on all values of the name
        """
        theOr = []
        for name in names:
            theOr.append({searchAttribute: name})

        return {"$or": theOr}

    def formatOutput(self, cursor):
        """Dump the MongoDB cursor into bson and load it into an object for manipulation.

        :param cursor: The documents that MongoDb returns
        :type cursor: documents
        :returns: Python object (list)
        """
        objects = self.getPythonObjects(cursor)
        for obj in objects:
            obj["id"] = obj["_id"]["$oid"]
            obj["metadata"]["importDate"] = Common().formatEpochDatetime(obj["metadata"]["importDate"]["$date"])

            try:
                obj["start"] = Common().formatEpochDatetime(obj["start"]["$date"])
            except KeyError:
                obj["x"] = Common().formatEpochDatetime(obj["x"]["$date"])

            try:
                obj["fixedData"]["start"] = Common().formatEpochDatetime(obj["fixedData"]["start"]["$date"])
            except KeyError:
                try:
                    obj["fixedData"]["x"] = Common().formatEpochDatetime(obj["fixedData"]["x"]["$date"])
                except KeyError:
                    pass

        return objects

    def getPythonObjects(self, cursor):
        bsonResult = dumps(cursor)
        return ujson.loads(bsonResult)


