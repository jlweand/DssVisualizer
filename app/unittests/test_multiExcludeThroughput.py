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
from core.apis.datasource.multiExcludeThroughput import MultiExcludeThroughput
from pprint import pprint


class MultiExcludeThroughputTest(unittest.TestCase):
    def test_searching(self):
        # select by only date
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-15 11:57:19', '2016-10-15 11:57:19', [], [], [])
        self.assertEqual(5, len(jsonData))

        # select by one Tech name
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-15 11:57:19', '2016-10-15 11:57:19', ["Alex"], [], [])
        self.assertEqual(2, len(jsonData))

        # select by two Tech names
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-15 11:57:19', '2016-10-15 11:57:19', ["Alex", "Julie"], [], [])
        self.assertEqual(3, len(jsonData))

        # select by one event name
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-15 11:57:19', '2016-10-15 11:57:19', [], ["Super Summer Event"], [])
        self.assertEqual(2, len(jsonData))

        # select by two event names
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-15 11:57:19', '2016-10-15 11:57:19', [], ["Super Summer Event", "Another Event"], [])
        self.assertEqual(4, len(jsonData))

        # select by one tech name and one event name
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-15 11:57:19', '2016-10-15 11:57:19', ["Alex"], ["Super Summer Event"], [])
        self.assertEqual(1, len(jsonData))

        # select by two tech names and tow event names
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-15 11:57:19', '2016-10-15 11:57:19', ["Alex", "Tom"], ["Super Summer Event", "Another Event"], [])
        self.assertEqual(3, len(jsonData))

        # select by one event/tech combo
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-15 11:57:19', '2016-10-15 11:57:19', [], [], ["Another Event by Julie"])
        self.assertEqual(1, len(jsonData))

        # select by two event/tech combos
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-15 11:57:19', '2016-10-15 11:57:19', [], [], ["Another Event by Julie", "Unicorns and more! by Willow"])
        self.assertEqual(2, len(jsonData))

        # select by one event/tech combo for a full day
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-18 00:00:01', '2016-10-18 23:59:59', [], [], ["Another Event by Alex"])
        self.assertEqual(77, len(jsonData))
        dataId = jsonData[0]["id"]

        # select by Id
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)
        self.assertEqual(1, len(jsonData))

    def test_fixedData(self):
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-15 11:57:19', '2016-10-15 11:57:19', [], [], ["Another Event by Alex"])
        dataId = jsonData[0]["id"]

        # insert Fixed MultiExcludeThroughput Data
        modifiedCount = MultiExcludeThroughput().modifyFixedMultiExcludeThroughputData(dataId, 123, 'trafficThroughput', '2016-10-02 18:28:00', 1111, True)
        self.assertEqual(1, modifiedCount)
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)
        self.assertEqual(jsonData[0]["fixedData"]["traffic_xy_id"], 123)
        self.assertEqual(jsonData[0]["fixedData"]["x"], '2016-10-02 18:28:00')
        self.assertEqual(jsonData[0]["fixedData"]["y"], 1111)
        self.assertTrue(jsonData[0]["fixedData"]["isDeleted"])

        # update Fixed MultiExcludeThroughput Data
        modifiedCount = MultiExcludeThroughput().modifyFixedMultiExcludeThroughputData(dataId, 456, 'trafficThroughput', '2017-01-02 18:28:00', 99999, False)
        self.assertEqual(1, modifiedCount)
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)
        self.assertEqual(jsonData[0]["fixedData"]["traffic_xy_id"], 456)
        self.assertEqual(jsonData[0]["fixedData"]["x"], '2017-01-02 18:28:00')
        self.assertEqual(jsonData[0]["fixedData"]["y"], 99999)
        self.assertFalse(jsonData[0]["fixedData"]["isDeleted"])

        # delete Fixed MultiExcludeThroughput Data
        modifiedCount = MultiExcludeThroughput().deleteFixedMultiExcludeThroughputData(dataId)
        self.assertEqual(1, modifiedCount)
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)
        self.assertRaises(KeyError, lambda: jsonData[0]["fixedData"])


    def test_annotations(self):
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-15 11:57:19', '2016-10-15 11:57:19', [], [], ["Another Event by Alex"])
        dataId = jsonData[0]["id"]

        # test single Annotation
        MultiExcludeThroughput().modifyAnnotationMultiExcludeThroughput(dataId, 'single annotation')
        addedAnn = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)
        self.assertEqual('single annotation', addedAnn[0]["annotation"])

        MultiExcludeThroughput().modifyAnnotationMultiExcludeThroughput(dataId, 'update annotation')
        addedAnn = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)
        self.assertEqual('update annotation', addedAnn[0]["annotation"])

        # test Annotation array
        MultiExcludeThroughput().addAnnotationToArrayMultiExcludeThroughput(dataId, 'test')
        MultiExcludeThroughput().addAnnotationToArrayMultiExcludeThroughput(dataId, 'test test')
        MultiExcludeThroughput().addAnnotationToArrayMultiExcludeThroughput(dataId, 'test test test')
        MultiExcludeThroughput().addAnnotationToArrayMultiExcludeThroughput(dataId, 'test test test')
        addedAnns = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)
        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual('test', addedAnns[0]["annotations"][0]["annotation"])
        self.assertEqual('test test', addedAnns[0]["annotations"][1]["annotation"])
        self.assertEqual('test test test', addedAnns[0]["annotations"][2]["annotation"])

        MultiExcludeThroughput().editAnnotationInArrayMultiExcludeThroughput(dataId, 'test test', 'updated annotation!!')
        changedAnn = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)
        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual('updated annotation!!', changedAnn[0]["annotations"][1]["annotation"])

        MultiExcludeThroughput().deleteAnnotationFromArrayMultiExcludeThroughput(dataId, 'updated annotation!!')
        deletedChanged = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))

        # test annotation delete
        MultiExcludeThroughput().deleteAllAnnotationsForMultiExcludeThroughput(dataId)
        deletedAll = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotation"])

        # add Annotation To MultiExcludeThroughput Timeline
        objectId = MultiExcludeThroughput().addAnnotationToMultiExcludeThroughputTimeline('2016-08-01 10:00:00',
                                                                                          "here's a timeline annotation", "Alex", "Super Summer Event")
        addtimelineAnnotation = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertEqual(addtimelineAnnotation[0]["className"], 'annotation')
        self.assertEqual(addtimelineAnnotation[0]["x"], '2016-08-01 10:00:00')
        self.assertEqual(addtimelineAnnotation[0]["content"], "here's a timeline annotation")
        self.assertEqual(addtimelineAnnotation[0]["metadata"]["techName"], 'Alex')
        self.assertEqual(addtimelineAnnotation[0]["metadata"]["eventName"], 'Super Summer Event')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
    unittest.main()

# python -m unittests.test_multiExcludeThroughput
