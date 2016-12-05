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

    def getModfiedCount(self, result):
        """Parse through the result from elasticsearch and return how many records were modified.

        :param result: the JSON result from the elasticsearch query
        :return: number of records modified
        """
        shards = result["_shards"]
        return shards["successful"]

    def getInsertedId(self, result):
        """Parse through the result from elasticsearch and return id that was inserted.

        :param result: the JSON result from the elasticsearch query
        :return: id of inserted records
        """
        return result["_id"]
