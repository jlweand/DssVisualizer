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
from core.apis.datasource.pyClick import PyClick
from pprint import pprint


class PyKeyLoggerTest(unittest.TestCase):
    def test_monolithicTestCase(self):
        # select by date
        jsonData = PyClick().selectClickData('2015-10-29 04:23:08', '2015-10-29 04:23:08', [], [], [])
        self.assertEqual(1, len(jsonData))
        dataId = jsonData[0]["id"]

        # select by Id
        jsonData = PyClick().selectClickDataById(dataId)
        pprint(jsonData)
        self.assertEqual(1, len(jsonData))

        # select by Tech name
        jsonData = PyClick().selectClickData('2015-10-29 04:23:08', '2015-10-29 04:23:08', ["Alex"], [], [])
        self.assertEqual(1, len(jsonData))

        # select by event name
        jsonData = PyClick().selectClickData('2015-10-29 04:23:08', '2015-10-29 04:23:08', [], ["Super Summer Event"], [])
        self.assertEqual(1, len(jsonData))

        # select by tech name AND event name
        jsonData = PyClick().selectClickData('2015-10-29 04:23:08', '2015-10-29 04:23:08', ["Alex"], ["Super Summer Event"], [])
        self.assertEqual(1, len(jsonData))

        # select by event/tech combo
        # jsonData = PyClick().selectClickData('2015-10-29 04:23:08', '2015-10-29 04:23:08', [], [], ["Another Event by Julie"])
        # self.assertEqual(1, len(jsonData))

        # insert Fixed Data
        modifiedCount = PyClick().insertFixedClickData(dataId, '2222', '[New Content Added]', 'imgPoint',
                                                       '2016-09-11 17:37:14',
                                                       '/new/path/1474038815.78_TESTING.png',
                                                       'point')
        self.assertEqual(1, modifiedCount)

        # update Fixed Data
        modifiedCount = PyClick().updateFixedClickData(dataId, '1111', '[EDITED UNITTEST Content Added]', ' imgPoint',
                                                       '2016-10-02 19:35:51',
                                                       '/newpath/click_images/1474038815.78_TESTING_UPDATE.png',
                                                       'point')
        self.assertEqual(1, modifiedCount)

        # delete Fixed Data
        modifiedCount = PyClick().deleteFixedClickData(dataId)
        self.assertEqual(1, modifiedCount)

        # test Annotations
        PyClick().addAnnotationClick(dataId, 'test')
        PyClick().addAnnotationClick(dataId, 'test test')
        PyClick().addAnnotationClick(dataId, 'test test test')
        PyClick().addAnnotationClick(dataId, 'test test test')
        addedAnns = PyClick().selectClickDataById(dataId)
        pprint(addedAnns)

        # PyClick().editAnnotationClick(dataId, 'test test', 'updated annotation!!')
        # changedAnn = PyClick().selectClickDataById(dataId)
        #
        # PyClick().deleteAnnotationClick(dataId, 'updated annotation!!')
        # deletedChanged = PyClick().selectClickDataById(dataId)
        #
        # PyClick().deleteAllAnnotationsForClick(dataId)
        # deletedAll = PyClick().selectClickDataById(dataId)
        #
        # self.assertEqual(3, len(addedAnns[0]["annotations"]))
        # self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        # self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])
        #
        # # add Annotation to Timeline
        # objectId = PyClick().addAnnotationToClickTimeline('2016-09-11 17:37:14', "here's a Click timeline annotation", "Alex", "Super Summer Event")
        # addtimelineAnnotation = PyClick().selectClickDataById(objectId)
        # pprint(addtimelineAnnotation)
        # self.assertIsNotNone(addtimelineAnnotation)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
    unittest.main()

# python -m unittests.test_pyClick
