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

from plugins.datasource.mongodb.selecting import Selecting

class TechAndEventNames:

    def getDistinctTechAndEventNames(self, collection):
        cursor = collection.aggregate([{"$group": {"_id": {"metadata.techName": "$metadata.techName", "metadata.eventName": "$metadata.eventName"}}}])
        pyObjects = Selecting().getPythonObjects(cursor)
        distinctList = []
        for obj in pyObjects:
            distinctList.append(obj["_id"]["metadata.eventName"] + " by " + obj["_id"]["metadata.techName"])
        return sorted(distinctList, key=str.lower)

    def getDistinctTechNamesForEvents(self, collection, eventNames):

        eventOr = []
        if len(eventNames) > 0:
            for name in eventNames:
                eventOr.append({"metadata.eventName": name})
            eventJson = { "$or": eventOr }

        match = [ { "$match": eventJson }, { "$group": {"_id": {"metadata.techName": "$metadata.techName"}}} ]
        cursor = collection.aggregate(match)
        pyObjects = Selecting().getPythonObjects(cursor)
        distinctList = []
        for obj in pyObjects:
            distinctList.append(obj["_id"]["metadata.techName"])
        return sorted(distinctList, key=str.lower)

    def getDistinctEventNames(self, collection):
        cursor = collection.find().distinct("metadata.eventName")
        distinctList = Selecting().getPythonObjects(cursor)
        return sorted(distinctList, key=str.lower)
