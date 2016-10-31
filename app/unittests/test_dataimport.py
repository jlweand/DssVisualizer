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
from datetime import datetime
from core.config.dataImport import DataImport


class DataImportTest(unittest.TestCase):
    now = datetime.now()
    nowString = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    techName = "Alex"
    eventName = "Super Summer Event"
    comments = "here are some comments"

    def test_1importClick(self):
        size = DataImport().importClick(self.techName, self.eventName, self.comments, self.nowString, False)
        self.assertEqual(size, 29)

    def test_2insertKeypressData(self):
        size = DataImport().importKeypressData(self.techName, self.eventName, self.comments, self.nowString)
        self.assertEqual(size, 71)

    def test_3importTimed(self):
        size = DataImport().importTimed(self.techName, self.eventName, self.comments, self.nowString, False)
        self.assertEqual(size, 48)

    def test_4importMultiExcludeThroughput(self):
        size = DataImport().importMultiExcludeThroughput(self.techName, self.eventName, self.comments,
                                                               self.nowString)
        self.assertEqual(size, 222)

    def test_5importMultiExcludeProtocol(self):
        size = DataImport().importMultiExcludeProtocol(self.techName, self.eventName, self.comments,
                                                             self.nowString)
        self.assertEqual(size, 222)

    def test_6importMultiIncludeThroughput(self):
        size = DataImport().importMultiIncludeThroughput(self.techName, self.eventName, self.comments,
                                                               self.nowString)
        self.assertEqual(size, 221)

    def test_7importMultiIncludeProtocol(self):
        size = DataImport().importMultiIncludeProtocol(self.techName, self.eventName, self.comments,
                                                             self.nowString)
        self.assertEqual(size, 221)

    def test_8importTsharkThroughput(self):
        size = DataImport().importTsharkThroughput(self.techName, self.eventName, self.comments, self.nowString)
        self.assertEqual(size, 371)

    def test_9importTsharkProtocol(self):
        size = DataImport().importTsharkProtocol(self.techName, self.eventName, self.comments, self.nowString)
        self.assertEqual(size, 371)

    # def test_01ImportAllFiles(self):
    #     DataImport().importAllDataFromFiles("C:\\temp\json", self.techName, self.eventName, self.comments,
    #                                               self.nowString)


if __name__ == '__main__':
    unittest.main()

# python -m unittests.test_dataimport
