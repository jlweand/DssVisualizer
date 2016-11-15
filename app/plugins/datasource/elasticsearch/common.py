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

import pytz
from datetime import datetime
from tzlocal import get_localzone
from dateutil.parser import parse
from pprint import pprint

class Common:
    """Here lies some common functions so they don't have to continue to be written over and over again."""

    def getIndexName(self):
        """Keep the index named in only one location. It helps keep typos down and
        creating a bunch of different indices and mass confusion when the computer
        is doing exactly what you're telling it to instead of what you want it to.

        :returns: string name of the one index we're using
        """
        return "dssvisualizer"

    def getSizeToReturn(self):
        """ElasticSearch defaults to returning 10 records.  This is great for paging and all that, but right now we just
         want all records back.  Assumption, the search will find no more than 50000 records so we will be returning them all.
        """
        return 5000

    def fixAllTheData(self, selectedData):
        """Format the JSON into what the application is expecting.

        :param selectedData: The JSON that elasticSearch returns when returning more than one record
        :return: object[] of data
        """
        records = selectedData["hits"]["hits"]
        cleanedUpData = []

        for record in records:
            cleanedUpData.append(self.fixData(record))

        return cleanedUpData

    def fixOneData(self, record):
        """Format the JSON into what the application is expecting.

        :param record: one record from the returned JSON data
        :return: object of data
        """
        cleanedUpData = []
        cleanedUpData.append(self.fixData(record))
        return cleanedUpData

    def fixData(self, record):
        _id = record["_id"]
        data = record["_source"]
        data["id"] = _id
        data["metadata"]["importDate"] = self.formateDateStringUTCtoStringLocalTime(data["metadata"]["importDate"])

        try:
            data["start"] = self.formateDateStringUTCtoStringLocalTime(data["start"])
        except KeyError:
            data["x"] = self.formateDateStringUTCtoStringLocalTime(data["x"])

        return data

    def formateDateStringUTCtoStringLocalTime(self, utcDateString):
        _date = parse(utcDateString)
        local_tz = get_localzone()
        local_now = _date.replace(tzinfo=pytz.utc).astimezone(local_tz)  # utc -> local
        return local_now.strftime('%Y-%m-%d %H:%M:%S')


    def createMetadataForTimelineAnnotations(self, techName, eventName):
        """Creates the generic metadata for the object when adding an annotation to just the timeline

        :returns: a metadata object.
        """
        metadata = {}
        metadata["techName"] = techName
        metadata["eventName"] = eventName
        metadata["comments"] = ""

        _date = datetime.now()
        local_tz = get_localzone()
        local_dt = local_tz.localize(_date)
        datimeNow = local_dt.astimezone(pytz.utc)
        metadata["importDate"] = datimeNow

        return metadata

    def getDateRangeJson(self, startDate, endDate, hasStartDate, hasXDate):
        """Returns the start or x date search query formatted for ElasticSearch

        :param startDate: Start of date range
        :type startDate: datetime
        :param endDate: End of date range
        :type endDate: datetime
        :param hasStartDate: If json file has start field
        :type hasStartDate: boolean
        :param hasXDate: If json file has x field instead of start field
        :type hasXDate: boolean
        :returns: ElasticSearch command for date range searching
        """

        if hasStartDate:
            daterange = { "range": {"start": {"gte": startDate, "lte": endDate}}}

        if hasXDate:
            daterange = { "range": {"x": {"gte": startDate, "lte": endDate}}}

        return daterange

    def getSearchStringJson(self, searchString, attributeName):
        """Returns the techName, eventName search query formatted for ElasticSearch

        :param searchString: The value to search for
        :type searchString: string
        :param attributeName: Name of attribute to search on
        :type attributeName: string
        :returns: ElasticSearch command for matching
        """

        match = { }
        if len(searchString) > 0 :
            match = {"match" : { attributeName: searchString[0]}}
        return match

    def generateSelectQuery(self, startDate, endDate, techNames, eventNames, eventTechNames, hasStartDate, hasXdate):
        daterange = self.getDateRangeJson(startDate, endDate, hasStartDate, hasXdate)
        techNameMatch = self.getSearchStringJson(techNames, "metadata.techName")
        eventNameMatch = self.getSearchStringJson(eventNames, "metadata.eventName")

        jsonQuery = {}
        jsonQuery["query"] = {}
        jsonQuery["query"]["bool"] = {}
        jsonQuery["query"]["bool"]["filter"] = daterange

        if len(techNameMatch) > 0 or len(eventNameMatch) > 0:
            jsonQuery["query"]["bool"]["must"] = []

            if len(techNameMatch) > 0:
                jsonQuery["query"]["bool"]["must"].append(techNameMatch)

            if len(eventNameMatch) > 0:
                jsonQuery["query"]["bool"]["must"].append(eventNameMatch)

        # pprint(jsonQuery)
        return jsonQuery

    def getModfiedCount(self, result):
        """Parse through the result from elasticsearch and return how many records were modified.

        :param result: the JSON result from the elasticsearch query
        :return: number of records modified
        """
        shards = result["_shards"]
        return shards["successful"]