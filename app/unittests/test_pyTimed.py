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
from core.apis.datasource.pyTimed import PyTimed
from pprint import pprint


class PyTimedTest(unittest.TestCase):

    def test_searching(self):
        # select by only date
        jsonData = PyTimed().selectTimedData('2016-10-18 18:26:37', '2016-10-18 18:26:37',[], [], [])
        self.assertEqual(5, len(jsonData))

        # select by one Tech name
        jsonData = PyTimed().selectTimedData('2016-10-18 18:26:37', '2016-10-18 18:26:37',["Alex"], [], [])
        self.assertEqual(2, len(jsonData))

        # select by two Tech names
        jsonData = PyTimed().selectTimedData('2016-10-18 18:26:37', '2016-10-18 18:26:37',["Alex", "Julie"], [], [])
        self.assertEqual(3, len(jsonData))

        # select by one event name
        jsonData = PyTimed().selectTimedData('2016-10-18 18:26:37', '2016-10-18 18:26:37', [], ["Super Summer Event"], [])
        self.assertEqual(2, len(jsonData))

        # select by two event names
        jsonData = PyTimed().selectTimedData('2016-10-18 18:26:37', '2016-10-18 18:26:37', [], ["Super Summer Event", "Another Event"], [])
        self.assertEqual(4, len(jsonData))

        # select by one tech name and one event name
        jsonData = PyTimed().selectTimedData('2016-10-18 18:26:37', '2016-10-18 18:26:37', ["Alex"], ["Super Summer Event"], [])
        self.assertEqual(1, len(jsonData))

        # select by two tech names and tow event names
        jsonData = PyTimed().selectTimedData('2016-10-18 18:26:37', '2016-10-18 18:26:37', ["Alex", "Tom"], ["Super Summer Event", "Another Event"], [])
        self.assertEqual(3, len(jsonData))

        # select by one event/tech combo
        jsonData = PyTimed().selectTimedData('2016-10-18 18:26:37', '2016-10-18 18:26:37', [], [], ["Another Event by Julie"])
        self.assertEqual(1, len(jsonData))

        # select by two event/tech combos
        jsonData = PyTimed().selectTimedData('2016-10-18 18:26:37', '2016-10-18 18:26:37', [], [], ["Another Event by Julie", "Unicorns and more! by Willow"])
        self.assertEqual(2, len(jsonData))

        # select by one event/tech combo for a full day
        jsonData = PyTimed().selectTimedData('2016-10-18 00:00:01', '2016-10-18 23:59:59', [], [], ["Another Event by Alex"])
        self.assertEqual(6, len(jsonData))
        dataId = jsonData[0]["id"]

        # select by Id
        jsonData = PyTimed().selectTimedDataById(dataId)
        pprint(jsonData)
        self.assertEqual(1, len(jsonData))

    def test_fixedData(self):
        jsonData = PyTimed().selectTimedData('2016-09-16 09:16:34', '2016-09-16 09:16:40', [], [], ["Another Event by Alex"])
        dataId = jsonData[0]["id"]

        # insert Fixed Data
        modifiedCount = PyTimed().insertFixedTimedData(dataId, '11111', '[New Content Added]', 'imgPoint',
                                                       '2016-09-16 15:16:35',
                                                       '/new/path/1465515528.8_screenshotTIMED_TESTING.png',
                                                       'point')
        self.assertEqual(1, modifiedCount)
        jsonData = PyTimed().selectTimedDataById(dataId)
        self.assertEqual(jsonData[0]["fixedData"]["timed_id"], '11111')
        self.assertEqual(jsonData[0]["fixedData"]["content"], '[New Content Added]')
        self.assertEqual(jsonData[0]["fixedData"]["className"], 'imgPoint')
        self.assertEqual(jsonData[0]["fixedData"]["start"], '2016-09-16 15:16:35')
        self.assertEqual(jsonData[0]["fixedData"]["title"], '/new/path/1465515528.8_screenshotTIMED_TESTING.png')
        self.assertEqual(jsonData[0]["fixedData"]["type"], 'point')

        # update Fixed Data
        modifiedCount = PyTimed().updateFixedTimedData(dataId, '22222', '[EDITED UNITTEST Content Added]', 'imgPoint123',
                                                       '2016-10-03 18:38:48',
                                                       '/newpath/click_images/1474038815.78_TESTING_UPDATE.png',
                                                       'point123')
        self.assertEqual(1, modifiedCount)
        jsonData = PyTimed().selectTimedDataById(dataId)
        self.assertEqual(jsonData[0]["fixedData"]["timed_id"], '22222')
        self.assertEqual(jsonData[0]["fixedData"]["content"], '[EDITED UNITTEST Content Added]')
        self.assertEqual(jsonData[0]["fixedData"]["className"], 'imgPoint123')
        self.assertEqual(jsonData[0]["fixedData"]["start"], '2016-10-03 18:38:48')
        self.assertEqual(jsonData[0]["fixedData"]["title"], '/newpath/click_images/1474038815.78_TESTING_UPDATE.png')
        self.assertEqual(jsonData[0]["fixedData"]["type"], 'point123')

        # delete Fixed Data
        modifiedCount = PyTimed().deleteFixedTimedData(dataId)
        self.assertEqual(1, modifiedCount)
        jsonData = PyTimed().selectTimedDataById(dataId)
        self.assertRaises(KeyError, lambda: jsonData[0]["fixedData"])

    def test_annotations(self):
        jsonData = PyTimed().selectTimedData('2016-09-16 09:16:34', '2016-09-16 09:16:40', [], [], ["Another Event by Alex"])
        dataId = jsonData[0]["id"]

        # test Annotations
        PyTimed().addAnnotationTimed(dataId, 'test')
        PyTimed().addAnnotationTimed(dataId, 'test test')
        PyTimed().addAnnotationTimed(dataId, 'test test test')
        PyTimed().addAnnotationTimed(dataId, 'test test test')
        addedAnns = PyTimed().selectTimedDataById(dataId)
        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual('test', addedAnns[0]["annotations"][0]["annotation"])
        self.assertEqual('test test', addedAnns[0]["annotations"][1]["annotation"])
        self.assertEqual('test test test', addedAnns[0]["annotations"][2]["annotation"])

        PyTimed().editAnnotationTimed(dataId, 'test test', 'updated annotation!!')
        changedAnn = PyTimed().selectTimedDataById(dataId)
        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual('updated annotation!!', changedAnn[0]["annotations"][1]["annotation"])

        PyTimed().deleteAnnotationTimed(dataId, 'updated annotation!!')
        deletedChanged = PyTimed().selectTimedDataById(dataId)
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))

        PyTimed().deleteAllAnnotationsForTimed(dataId)
        deletedAll = PyTimed().selectTimedDataById(dataId)
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # add Annotation to Timeline
        objectId = PyTimed().addAnnotationToTimedTimeline('2016-09-16 15:16:34', "here's a Timed timeline annotation", "Alex", "Super Summer Event")
        addtimelineAnnotation = PyTimed().selectTimedDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertEqual(addtimelineAnnotation[0]["className"], 'annotation')
        self.assertEqual(addtimelineAnnotation[0]["start"], '2016-09-16 15:16:34')
        self.assertEqual(addtimelineAnnotation[0]["annotations"]["annotation"], "here's a Timed timeline annotation")
        self.assertEqual(addtimelineAnnotation[0]["metadata"]["techName"], 'Alex')
        self.assertEqual(addtimelineAnnotation[0]["metadata"]["eventName"], 'Super Summer Event')


if __name__ == '__main__':
    unittest.main()

# python -m unittests.test_pyTimed
