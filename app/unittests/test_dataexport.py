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
from core.config.dataExportConfig import DataExportConfig


class DataImportTest(unittest.TestCase):
    startDate = "2016-10-18 00:00:00"
    endDate = "2016-10-18 23:59:59"
    techName = "Alex"
    eventName = "Super Summer Event"

    def test_1ExportClick(self):
        size = DataExportConfig().exportClickData(self.startDate, self.endDate, self.techName, self.eventName, False, "C:\\temp\export")
        self.assertEqual(size, 8)


    def test_2exportKeypressData(self):
        size = DataExportConfig().exportKeyPressData(self.startDate, self.endDate, self.techName, self.eventName, "C:\\temp\export")
        self.assertEqual(size, 6)


    def test_3exportTimed(self):
        size = DataExportConfig().exportTimedData(self.startDate, self.endDate, self.techName, self.eventName, False, "C:\\temp\export")
        self.assertEqual(size, 6)


    def test_4exportMultiExcludeThroughput(self):
        size = DataExportConfig().exportMultiExcludeThroughputData(self.startDate, self.endDate, self.techName, self.eventName, "C:\\temp\export")
        self.assertEqual(size, 77)


    def test_5exportMultiExcludeProtocol(self):
        size = DataExportConfig().exportMultiExcludeProtocolData(self.startDate, self.endDate, self.techName, self.eventName, "C:\\temp\export")
        self.assertEqual(size, 77)


    def test_6exportMultiIncludeThroughput(self):
        size = DataExportConfig().exportMultiIncludeThroughputData(self.startDate, self.endDate, self.techName, self.eventName, "C:\\temp\export")
        self.assertEqual(size, 77)


    def test_7exportMultiIncludeProtocol(self):
        size = DataExportConfig().exportMultiIncludeProtocolData(self.startDate, self.endDate, self.techName, self.eventName, "C:\\temp\export")
        self.assertEqual(size, 77)


    def test_8exportTsharkThroughput(self):
        size = DataExportConfig().exportTsharkThroughputData(self.startDate, self.endDate, self.techName, self.eventName, "C:\\temp\export")
        self.assertEqual(size, 79)


    def test_9exportTsharkProtocol(self):
        size = DataExportConfig().exportTsharkProtocolData(self.startDate, self.endDate, self.techName, self.eventName, "C:\\temp\export")
        self.assertEqual(size, 79)
    #
    # def test_01exportAllData(self):
    #     DataExportConfig().exportAllDataFromFilesData(self.startDate, self.endDate, self.techName, self.eventName, False, "C:\\temp\export")


if __name__ == '__main__':
    unittest.main()

# python -m unittests.test_dataexport