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


class PyClickTest(unittest.TestCase):

    def test_searching(self):
        # select by only date
        jsonData = PyClick().selectClickData('2016-10-18 18:26:43', '2016-10-18 18:26:43',[], [], [])
        self.assertEqual(5, len(jsonData))

        # select by one Tech name
        jsonData = PyClick().selectClickData('2016-10-18 18:26:43', '2016-10-18 18:26:43',["Alex"], [], [])
        self.assertEqual(2, len(jsonData))

        # select by two Tech names
        jsonData = PyClick().selectClickData('2016-10-18 18:26:43', '2016-10-18 18:26:43',["Alex", "Julie"], [], [])
        self.assertEqual(3, len(jsonData))

        # select by one event name
        jsonData = PyClick().selectClickData('2016-10-18 18:26:43', '2016-10-18 18:26:43', [], ["Super Summer Event"], [])
        self.assertEqual(2, len(jsonData))

        # select by two event names
        jsonData = PyClick().selectClickData('2016-10-18 18:26:43', '2016-10-18 18:26:43', [], ["Super Summer Event", "Another Event"], [])
        self.assertEqual(4, len(jsonData))

        # select by one tech name and one event name
        jsonData = PyClick().selectClickData('2016-10-18 18:26:43', '2016-10-18 18:26:43', ["Alex"], ["Super Summer Event"], [])
        self.assertEqual(1, len(jsonData))

        # select by two tech names and tow event names
        jsonData = PyClick().selectClickData('2016-10-18 18:26:43', '2016-10-18 18:26:43', ["Alex", "Tom"], ["Super Summer Event", "Another Event"], [])
        self.assertEqual(3, len(jsonData))

        # select by one event/tech combo
        jsonData = PyClick().selectClickData('2016-10-18 18:26:43', '2016-10-18 18:26:43', [], [], ["Another Event by Julie"])
        self.assertEqual(1, len(jsonData))

        # select by two event/tech combos
        jsonData = PyClick().selectClickData('2016-10-18 18:26:43', '2016-10-18 18:26:43', [], [], ["Another Event by Julie", "Unicorns and more! by Willow"])
        self.assertEqual(2, len(jsonData))

        # select by one event/tech combo for a full day
        jsonData = PyClick().selectClickData('2016-10-18 00:00:01', '2016-10-18 23:59:59', [], [], ["Another Event by Alex"])
        self.assertEqual(8, len(jsonData))
        dataId = jsonData[0]["id"]

        # select by Id
        jsonData = PyClick().selectClickDataById(dataId)
        self.assertEqual(1, len(jsonData))

    def test_fixedData(self):
        jsonData = PyClick().selectClickData('2016-10-18 18:26:43', '2016-10-18 18:26:43', [], [], ["Another Event by Alex"])
        dataId = jsonData[0]["id"]

        # insert Fixed Data
        modifiedCount = PyClick().insertFixedClickData(dataId, '2222', '[New Content Added]', 'imgPoint',
                                                       '2016-09-11 17:37:14',
                                                       '/new/path/1474038815.78_TESTING.png',
                                                       'point')
        self.assertEqual(1, modifiedCount)
        jsonData = PyClick().selectClickDataById(dataId)
        self.assertEqual(jsonData[0]["fixedData"]["clicks_id"], '2222')
        self.assertEqual(jsonData[0]["fixedData"]["content"], '[New Content Added]')
        self.assertEqual(jsonData[0]["fixedData"]["className"], 'imgPoint')
        self.assertEqual(jsonData[0]["fixedData"]["start"], '2016-09-11 17:37:14')
        self.assertEqual(jsonData[0]["fixedData"]["title"], '/new/path/1474038815.78_TESTING.png')
        self.assertEqual(jsonData[0]["fixedData"]["type"], 'point')

        # update Fixed Data
        modifiedCount = PyClick().updateFixedClickData(dataId, '1111', '[EDITED UNITTEST Content Added]', 'imgPoint123',
                                                       '2016-10-02 19:35:51',
                                                       '/newpath/click_images/1474038815.78_TESTING_UPDATE.png',
                                                       'point123')
        self.assertEqual(1, modifiedCount)
        jsonData = PyClick().selectClickDataById(dataId)
        self.assertEqual(jsonData[0]["fixedData"]["clicks_id"], '1111')
        self.assertEqual(jsonData[0]["fixedData"]["content"], '[EDITED UNITTEST Content Added]')
        self.assertEqual(jsonData[0]["fixedData"]["className"], 'imgPoint123')
        self.assertEqual(jsonData[0]["fixedData"]["start"], '2016-10-02 19:35:51')
        self.assertEqual(jsonData[0]["fixedData"]["title"], '/newpath/click_images/1474038815.78_TESTING_UPDATE.png')
        self.assertEqual(jsonData[0]["fixedData"]["type"], 'point123')

        # delete Fixed Data
        modifiedCount = PyClick().deleteFixedClickData(dataId)
        self.assertEqual(1, modifiedCount)
        jsonData = PyClick().selectClickDataById(dataId)
        self.assertRaises(KeyError, lambda: jsonData[0]["fixedData"])

    def test_annotations(self):
        jsonData = PyClick().selectClickData('2016-10-18 18:26:43', '2016-10-18 18:26:43', [], [], ["Another Event by Alex"])
        dataId = jsonData[0]["id"]

        # test Annotations
        PyClick().addAnnotationClick(dataId, 'test')
        PyClick().addAnnotationClick(dataId, 'test test')
        PyClick().addAnnotationClick(dataId, 'test test test')
        PyClick().addAnnotationClick(dataId, 'test test test')
        addedAnns = PyClick().selectClickDataById(dataId)
        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual('test', addedAnns[0]["annotations"][0]["annotation"])
        self.assertEqual('test test', addedAnns[0]["annotations"][1]["annotation"])
        self.assertEqual('test test test', addedAnns[0]["annotations"][2]["annotation"])

        PyClick().editAnnotationClick(dataId, 'test test', 'updated annotation!!')
        changedAnn = PyClick().selectClickDataById(dataId)
        self.assertEqual('updated annotation!!', changedAnn[0]["annotations"][1]["annotation"])

        PyClick().deleteAnnotationClick(dataId, 'updated annotation!!')
        deletedChanged = PyClick().selectClickDataById(dataId)
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))

        PyClick().deleteAllAnnotationsForClick(dataId)
        deletedAll = PyClick().selectClickDataById(dataId)
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # add Annotation to Timeline
        objectId = PyClick().addAnnotationToClickTimeline('2016-09-11 17:37:14', "here's a Click timeline annotation", "Alex", "Super Summer Event")
        addtimelineAnnotation = PyClick().selectClickDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertEqual(addtimelineAnnotation[0]["className"], 'annotation')
        self.assertEqual(addtimelineAnnotation[0]["start"], '2016-09-11 17:37:14')
        self.assertEqual(addtimelineAnnotation[0]["annotations"]["annotation"], "here's a Click timeline annotation")
        self.assertEqual(addtimelineAnnotation[0]["metadata"]["techName"], 'Alex')
        self.assertEqual(addtimelineAnnotation[0]["metadata"]["eventName"], 'Super Summer Event')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    unittest.main()

# python -m unittests.test_pyClick
