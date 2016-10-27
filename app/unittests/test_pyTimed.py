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


class PyKeyLoggerTest(unittest.TestCase):
    def test_monolithicTestCase(self):
        # select by date
        jsonData = PyTimed().selectTimedData('2016-09-16 09:16:34', '2016-09-16 09:16:40', "", "")
        dataId = jsonData[0]["id"]
        self.assertEqual(1, len(jsonData))

        # select by Id
        jsonData = PyTimed().selectTimedDataById(dataId)
        pprint(jsonData)
        self.assertEqual(1, len(jsonData))

        # select by Tech name
        jsonData = PyTimed().selectTimedData('2016-09-16 09:16:34', '2016-09-16 09:16:40', "Alex", "")
        self.assertEqual(1, len(jsonData))

        # select by event name
        jsonData = PyTimed().selectTimedData('2016-09-16 09:16:34', '2016-09-16 09:16:40', "", "Super Summer Event")
        self.assertEqual(1, len(jsonData))

        # select by tech name AND event name
        jsonData = PyTimed().selectTimedData('2016-09-16 09:16:34', '2016-09-16 09:16:40', "Alex", "Super Summer Event")
        self.assertEqual(1, len(jsonData))

        # test Annotations
        PyTimed().addAnnotationTimed(dataId, 'test')
        PyTimed().addAnnotationTimed(dataId, 'test test')
        PyTimed().addAnnotationTimed(dataId, 'test test test')
        PyTimed().addAnnotationTimed(dataId, 'test test test')
        addedAnns = PyTimed().selectTimedDataById(dataId)

        PyTimed().editAnnotationTimed(dataId, 'test test', 'updated annotation!!')
        changedAnn = PyTimed().selectTimedDataById(dataId)

        PyTimed().deleteAnnotationTimed(dataId, 'updated annotation!!')
        deletedChanged = PyTimed().selectTimedDataById(dataId)

        PyTimed().deleteAllAnnotationsForTimed(dataId)
        deletedAll = PyTimed().selectTimedDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # insert Fixed Data
        modifiedCount = PyTimed().insertFixedTimedData(dataId, '11111', '[New Content Added]', 'imgPoint',
                                                       '2016-09-16 15:16:35',
                                                       '/new/path/1465515528.8_screenshotTIMED_TESTING.png',
                                                       'point')
        self.assertEqual(1, modifiedCount)

        # update Fixed Data
        modifiedCount = PyTimed().updateFixedTimedData(dataId, '22222', '[EDITED UNITTEST Content Added]', 'imgPoint',
                                                       '2016-10-03 18:38:48',
                                                       '/newpath/click_images/1474038815.78_TESTING_UPDATE.png',
                                                       'point')
        self.assertEqual(1, modifiedCount)

        # delete Fixed Data
        modifiedCount = PyTimed().deleteFixedTimedData(dataId)
        self.assertEqual(1, modifiedCount)

        # add Annotation to Timeline
        objectId = PyTimed().addAnnotationToTimedTimeline('2016-09-16 15:16:34', "here's a Timed timeline annotation")
        addtimelineAnnotation = PyTimed().selectTimedDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertIsNotNone(addtimelineAnnotation)


if __name__ == '__main__':
    unittest.main()

# python -m unittests.test_pyTimed
