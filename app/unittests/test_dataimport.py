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

    # def test_01importClick(self):
    #     size = DataImport().importClick(self.techName, self.eventName, self.comments, self.nowString, False)
    #     self.assertEqual(size, 29)
    #
    # def test_02insertKeypressData(self):
    #     size = DataImport().importKeypressData(self.techName, self.eventName, self.comments, self.nowString)
    #     self.assertEqual(size, 71)
    #
    # def test_03importTimed(self):
    #     size = DataImport().importTimed(self.techName, self.eventName, self.comments, self.nowString, False)
    #     self.assertEqual(size, 48)

    # def test_04importMultiExcludeThroughput(self):
    #     size = DataImport().importMultiExcludeThroughput(self.techName, self.eventName, self.comments, self.nowString)
    #     self.assertEqual(size, 222)
    #
    # def test_05importMultiExcludeProtocol(self):
    #     size = DataImport().importMultiExcludeProtocol(self.techName, self.eventName, self.comments, self.nowString)
    #     self.assertEqual(size, 222)
    #
    # def test_06importMultiIncludeThroughput(self):
    #     size = DataImport().importMultiIncludeThroughput(self.techName, self.eventName, self.comments, self.nowString)
    #     self.assertEqual(size, 221)
    #
    # def test_07importMultiIncludeProtocol(self):
    #     size = DataImport().importMultiIncludeProtocol(self.techName, self.eventName, self.comments, self.nowString)
    #     self.assertEqual(size, 221)
    #
    # def test_08importTsharkThroughput(self):
    #     size = DataImport().importTsharkThroughput(self.techName, self.eventName, self.comments, self.nowString)
    #     self.assertEqual(size, 371)
    #
    # def test_09importTsharkProtocol(self):
    #     size = DataImport().importTsharkProtocol(self.techName, self.eventName, self.comments, self.nowString)
    #     self.assertEqual(size, 371)
    #
    # def test_10importManualScreenShot(self):
    #     size = DataImport().importManualScreenShot(self.techName, self.eventName, self.comments, self.nowString, False)
    #     self.assertEqual(size, 15)

    def test_11ImportAllFiles(self):
        DataImport().importAllDataFromFiles("C:\\temp\json", self.techName, self.eventName, self.comments, self.nowString, False)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
    unittest.main()

# python -m unittests.test_dataimport
