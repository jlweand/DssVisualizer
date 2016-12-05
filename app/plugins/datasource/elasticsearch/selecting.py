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

class Selecting:
    """Here lies the logic for selecting and returning data.  It generates the select query and cleans up the data being returned."""

    def generateSelectQuery(self, startDate, endDate, techNames, eventNames, eventTechNames, hasStartDate, hasXdate):
        """Generates the select query for searching on date, tech, and event names.

        :param startDate: Start of date range
        :type startDate: datetime
        :param endDate: End of date range
        :type endDate: datetime
        :param techNames: A list of technician names to search on
        :type techNames: list
        :param eventNames: A list of event names to search on
        :type eventNames: list
        :param eventTechNames: A list of a combination of event and tech names to return data
        :type eventTechNames: list
        :param hasStartDate: If json file has start field
        :type hasStartDate: boolean
        :param hasXdate: If json file has x field instead of start field
        :type hasXdate: boolean
        :returns: elasticsearch search command
        """

        daterange = self.getDateRangeJson(startDate, endDate, hasStartDate, hasXdate)

        jsonQuery = {}
        jsonQuery["query"] = {}
        jsonQuery["query"]["bool"] = {}
        jsonQuery["query"]["bool"]["filter"] = daterange

        if len(eventTechNames) > 0:
            jsonQuery["query"]["bool"]["should"] = []

            for eventTech in eventTechNames:
                etl = eventTech.split(" by ")
                theBool = {"bool": {"must": []}}
                theBool["bool"]["must"].append({"match_phrase": {"metadata.eventName": etl[0]}})
                theBool["bool"]["must"].append({"match_phrase": {"metadata.techName": etl[1]}})
                jsonQuery["query"]["bool"]["should"].append(theBool)

            jsonQuery["query"]["bool"]["minimum_should_match"] = 1

        elif len(techNames) > 0 or len(eventNames) > 0:
            jsonQuery["query"]["bool"]["should"] = []

            if len(techNames) > 0:
                for techName in techNames:
                    techNameMatch = {"match_phrase": {"metadata.techName": techName}}
                    jsonQuery["query"]["bool"]["should"].append(techNameMatch)

            if len(eventNames) > 0:
                for eventName in eventNames:
                    eventNameMatch = {"match_phrase": {"metadata.eventName": eventName}}
                    jsonQuery["query"]["bool"]["should"].append(eventNameMatch)

            if len(techNames) > 0 and len(eventNames) > 0:
                jsonQuery["query"]["bool"]["minimum_should_match"] = 2
            else:
                jsonQuery["query"]["bool"]["minimum_should_match"] = 1

        return jsonQuery

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
            daterange = {"range": {"start": {"gte": startDate, "lte": endDate}}}

        if hasXDate:
            daterange = {"range": {"x": {"gte": startDate, "lte": endDate}}}

        return daterange

    def formateDateStringUTCtoStringLocalTime(self, utcDateString):
        _date = parse(utcDateString)
        local_tz = get_localzone()
        local_now = _date.replace(tzinfo=pytz.utc).astimezone(local_tz)  # utc -> local
        return local_now.strftime('%Y-%m-%d %H:%M:%S')

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

        try:
            data["fixedData"]["start"] = self.formateDateStringUTCtoStringLocalTime(data["fixedData"]["start"])
        except KeyError:
            try:
                data["fixedData"]["x"] = self.formateDateStringUTCtoStringLocalTime(data["fixedData"]["x"])
            except KeyError:
                pass

        return data

