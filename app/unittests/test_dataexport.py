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
from core.config.dataExport import DataExport


class DataImportTest(unittest.TestCase):
    startDate = "2016-10-18 00:00:00"
    endDate = "2016-10-18 23:59:59"
    techName = "Alex"
    eventName = "Super Summer Event"

    # def test_01ExportClick(self):
    #     size = DataExport().exportClickData(self.startDate, self.endDate, self.techName, self.eventName, True, "C:\\temp\export")
    #     self.assertEqual(size, 8)
    #
    # def test_02exportKeypressData(self):
    #     size = DataExport().exportKeyPressData(self.startDate, self.endDate, self.techName, self.eventName, "C:\\temp\export")
    #     self.assertEqual(size, 6)
    #
    # def test_03exportTimed(self):
    #     size = DataExport().exportTimedData(self.startDate, self.endDate, self.techName, self.eventName, True, "C:\\temp\export")
    #     self.assertEqual(size, 6)
    #
    # def test_04exportMultiExcludeThroughput(self):
    #     size = DataExport().exportMultiExcludeThroughputData(self.startDate, self.endDate, self.techName, self.eventName, "C:\\temp\export")
    #     self.assertEqual(size, 77)
    #
    # def test_05exportMultiExcludeProtocol(self):
    #     size = DataExport().exportMultiExcludeProtocolData(self.startDate, self.endDate, self.techName, self.eventName, "C:\\temp\export")
    #     self.assertEqual(size, 77)
    #
    # def test_06exportMultiIncludeThroughput(self):
    #     size = DataExport().exportMultiIncludeThroughputData(self.startDate, self.endDate, self.techName, self.eventName, "C:\\temp\export")
    #     self.assertEqual(size, 77)
    #
    # def test_07exportMultiIncludeProtocol(self):
    #     size = DataExport().exportMultiIncludeProtocolData(self.startDate, self.endDate, self.techName, self.eventName, "C:\\temp\export")
    #     self.assertEqual(size, 77)
    #
    # def test_08exportTsharkThroughput(self):
    #     size = DataExport().exportTsharkThroughputData(self.startDate, self.endDate, self.techName, self.eventName, "C:\\temp\export")
    #     self.assertEqual(size, 79)
    #
    # def test_09exportTsharkProtocol(self):
    #     size = DataExport().exportTsharkProtocolData(self.startDate, self.endDate, self.techName, self.eventName, "C:\\temp\export")
    #     self.assertEqual(size, 79)
    #
    # def test_10ExportManualScreenShot(self):
    #     size = DataExport().exportManualScreenShotData(self.startDate, self.endDate, self.techName, self.eventName, True, "C:\\temp\export")
    #     self.assertEqual(size, 2)

    def test_11exportAllData(self):
        DataExport().exportAllData(self.startDate, self.endDate, self.techName, self.eventName, True, "C:\\temp\export")


if __name__ == '__main__':
    unittest.main()

# python -m unittests.test_dataexport