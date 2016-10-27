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

from datetime import datetime, timezone
from pymongo import MongoClient
from bson.json_util import dumps
import ujson
import pytz
from tzlocal import get_localzone
from core.apis.datasource.common import Common

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


    def createMetadataForTimelineAnnotations(self):
        """Creates the generic metadata for the object when adding an annotation to just the timeline

        :returns: a metadata object.
        """
        metadata = {}
        metadata["techName"] = "Manual Entry"
        metadata["eventName"] = ""
        metadata["comments"] = ""

        _date = datetime.now()
        local_tz = get_localzone()
        local_dt = local_tz.localize(_date)
        datimeNow = local_dt.astimezone(pytz.utc)
        metadata["importDate"] = datimeNow

        return metadata

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
