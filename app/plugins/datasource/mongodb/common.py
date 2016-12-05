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
from datetime import datetime
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

    def addIndex(self, collection, hasStart):
        """Adds an index to the collection if it does not already exist

        :param collection: The collection to add the index to
        :type collection: MongoDB collection
        :param hasStart: True if the date to search by is 'start' otherwise it's assumed to be 'x'
        :type hasStart: boolean
        """

        if hasStart:
            collection.create_index([("start", pymongo.ASCENDING),
                                     ("metadata.techName", pymongo.ASCENDING),
                                     ("metadata.eventName", pymongo.ASCENDING)], background=True)
        else:
            collection.create_index([("x", pymongo.ASCENDING),
                                     ("metadata.techName", pymongo.ASCENDING),
                                     ("metadata.eventName", pymongo.ASCENDING)], background=True)
