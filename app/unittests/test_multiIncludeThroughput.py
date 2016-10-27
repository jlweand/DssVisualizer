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
from core.apis.datasource.multiIncludeThroughput import MultiIncludeThroughput
from pprint import pprint


class MultiIncludeThroughputTest(unittest.TestCase):
    def test_monolithicTestCase(self):
        # select by date
        jsonData = MultiIncludeThroughput().selectMultiIncludeThroughputData('2016-10-15 11:57:19',
                                                                             '2016-10-15 11:57:19', "", "")
        pprint(jsonData)
        dataId = jsonData[0]["id"]
        self.assertEqual(1, len(jsonData))

        # select by Id
        jsonData = MultiIncludeThroughput().selectMultiIncludeThroughputDataById(dataId)
        self.assertEqual(1, len(jsonData))

        # select by Tech name
        jsonData = MultiIncludeThroughput().selectMultiIncludeThroughputData('2016-10-15 11:59:27',
                                                                             '2016-10-15 11:59:27', "Alex", "")
        self.assertEqual(1, len(jsonData))
        # select by event name

        jsonData = MultiIncludeThroughput().selectMultiIncludeThroughputData('2016-10-15 11:59:27',
                                                                             '2016-10-15 11:59:27', "",
                                                                             "Super Summer Event")
        self.assertEqual(1, len(jsonData))

        # select by tech name AND event name
        jsonData = MultiIncludeThroughput().selectMultiIncludeThroughputData('2016-10-15 11:59:27',
                                                                             '2016-10-15 11:59:27', "Alex",
                                                                             "Super Summer Event")
        self.assertEqual(1, len(jsonData))

        # test Annotations
        MultiIncludeThroughput().addAnnotationMultiIncludeThroughput(dataId, 'test')
        MultiIncludeThroughput().addAnnotationMultiIncludeThroughput(dataId, 'test test')
        MultiIncludeThroughput().addAnnotationMultiIncludeThroughput(dataId, 'test test test')
        MultiIncludeThroughput().addAnnotationMultiIncludeThroughput(dataId, 'test test test')
        addedAnns = MultiIncludeThroughput().selectMultiIncludeThroughputDataById(dataId)

        MultiIncludeThroughput().editAnnotationMultiIncludeThroughput(dataId, 'test test', 'updated annotation!!')
        changedAnn = MultiIncludeThroughput().selectMultiIncludeThroughputDataById(dataId)

        MultiIncludeThroughput().deleteAnnotationMultiIncludeThroughput(dataId, 'updated annotation!!')
        deletedChanged = MultiIncludeThroughput().selectMultiIncludeThroughputDataById(dataId)

        MultiIncludeThroughput().deleteAllAnnotationsForMultiIncludeThroughput(dataId)
        deletedAll = MultiIncludeThroughput().selectMultiIncludeThroughputDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # insert Fixed MultiExcludeThroughput Data
        modifiedCount = MultiIncludeThroughput().insertFixedMultiIncludeThroughputData(dataId, '2016-10-02 18:28:00',
                                                                                       1111)
        self.assertEqual(1, modifiedCount)

        # update Fixed MultiExcludeThroughput Data
        modifiedCount = MultiIncludeThroughput().updateFixedMultiIncludeThroughputData(dataId, '2017-01-02 18:28:00',
                                                                                       99999)
        self.assertEqual(1, modifiedCount)

        # delete Fixed MultiExcludeThroughput Data
        modifiedCount = MultiIncludeThroughput().deleteFixedMultiIncludeThroughputData(dataId)
        self.assertEqual(1, modifiedCount)

        # add Annotation To MultiExcludeThroughput Timeline
        objectId = MultiIncludeThroughput().addAnnotationToMultiIncludeThroughputTimeline('2016-08-01 10:00:00',
                                                                                          "here's a timeline annotation")
        addtimelineAnnotation = MultiIncludeThroughput().selectMultiIncludeThroughputDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertIsNotNone(addtimelineAnnotation)


if __name__ == '__main__':
    unittest.main()

# python -m unittests.test_multiIncludeThroughput
