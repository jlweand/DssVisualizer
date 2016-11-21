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

import unittest
import time
from datetime import datetime
from pprint import pprint
from plugins.datasource.elasticsearch.pyClick import PyClick
from core.config.dataImport import DataImport
from core.apis.datasource.common import Common
from elasticsearch import Elasticsearch

class CleanupDatabases(unittest.TestCase):

    def test_cleanEverythingUp(self):
        now = datetime.now()
        rightNow = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
        comments = "here are some comments"

        es = Elasticsearch()
        es.indices.delete(index="dssvisualizer", ignore=[400, 404])

        DataImport().importAllDataFromFiles("json/unittestDatasets/anotherAlex", "   Alex", "Another Event",         comments, rightNow, False)
        DataImport().importAllDataFromFiles("json/unittestDatasets/unicornWillow",   "Willow", "Unicorns and more!", comments, rightNow, False)
        DataImport().importAllDataFromFiles("json/unittestDatasets/superSummerAlex", "Alex", "Super Summer Event",   comments, rightNow, False)
        DataImport().importAllDataFromFiles("json/unittestDatasets/superSummerTom",  "Tom", "Super Summer Event",    comments, rightNow, False)
        DataImport().importAllDataFromFiles("json/unittestDatasets/anotherJulie",    "Julie", "Another Event",       comments, rightNow, False)

        time.sleep(5)
        jsonData = PyClick().selectClickData(Common().formatDateStringToUTC('2016-10-18 18:26:43'),
                                             Common().formatDateStringToUTC('2016-10-18 18:26:43'), [], [], [])
        pprint(jsonData)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    unittest.main()

#python -m unittests.cleanupESDatabases
