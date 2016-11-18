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
from core.apis.datasource.pyKeyPress import PyKeyPress
from pprint import pprint


class PyKeyPressTest(unittest.TestCase):

    def test_searching(self):
        # select by only date
        jsonData = PyKeyPress().selectKeyPressData('2016-10-12 17:36:24', '2016-10-12 17:36:24',[], [], [])
        self.assertEqual(5, len(jsonData))

        # select by one Tech name
        jsonData = PyKeyPress().selectKeyPressData('2016-10-12 17:36:24', '2016-10-12 17:36:24',["Alex"], [], [])
        self.assertEqual(2, len(jsonData))

        # select by two Tech names
        jsonData = PyKeyPress().selectKeyPressData('2016-10-12 17:36:24', '2016-10-12 17:36:24',["Alex", "Julie"], [], [])
        self.assertEqual(3, len(jsonData))

        # select by one event name
        jsonData = PyKeyPress().selectKeyPressData('2016-10-12 17:36:24', '2016-10-12 17:36:24', [], ["Super Summer Event"], [])
        self.assertEqual(2, len(jsonData))

        # select by two event names
        jsonData = PyKeyPress().selectKeyPressData('2016-10-12 17:36:24', '2016-10-12 17:36:24', [], ["Super Summer Event", "Another Event"], [])
        self.assertEqual(4, len(jsonData))

        # select by one tech name and one event name
        jsonData = PyKeyPress().selectKeyPressData('2016-10-12 17:36:24', '2016-10-12 17:36:24', ["Alex"], ["Super Summer Event"], [])
        self.assertEqual(1, len(jsonData))

        # select by two tech names and tow event names
        jsonData = PyKeyPress().selectKeyPressData('2016-10-12 17:36:24', '2016-10-12 17:36:24', ["Alex", "Tom"], ["Super Summer Event", "Another Event"], [])
        self.assertEqual(3, len(jsonData))

        # select by one event/tech combo
        jsonData = PyKeyPress().selectKeyPressData('2016-10-12 17:36:24', '2016-10-12 17:36:24', [], [], ["Another Event by Julie"])
        self.assertEqual(1, len(jsonData))

        # select by two event/tech combos
        jsonData = PyKeyPress().selectKeyPressData('2016-10-12 17:36:24', '2016-10-12 17:36:24', [], [], ["Another Event by Julie", "Unicorns and more! by Willow"])
        self.assertEqual(2, len(jsonData))

        # select by one event/tech combo for a full day
        jsonData = PyKeyPress().selectKeyPressData('2016-10-18 00:00:01', '2016-10-18 23:59:59', [], [], ["Another Event by Alex"])
        self.assertEqual(6, len(jsonData))
        dataId = jsonData[0]["id"]

        # select by Id
        jsonData = PyKeyPress().selectKeyPressDataById(dataId)
        pprint(jsonData)
        self.assertEqual(1, len(jsonData))

    def test_fixedData(self):
        jsonData = PyKeyPress().selectKeyPressData('2016-10-12 17:36:24', '2016-10-12 17:36:24', [], [], ["Another Event by Alex"])
        dataId = jsonData[0]["id"]

        # insert Fixed Data
        modifiedCount = PyKeyPress().insertFixedKeyPressData(dataId, '11111', '[New Content Added]', 'Keypresses', '2016-10-15 17:58:31', True)
        self.assertEqual(1, modifiedCount)
        jsonData = PyKeyPress().selectKeyPressDataById(dataId)
        self.assertEqual(jsonData[0]["fixedData"]["keypress_id"], '11111')
        self.assertEqual(jsonData[0]["fixedData"]["content"], '[New Content Added]')
        self.assertEqual(jsonData[0]["fixedData"]["className"], 'Keypresses')
        self.assertEqual(jsonData[0]["fixedData"]["start"], '2016-10-15 17:58:31')
        self.assertTrue(jsonData[0]["fixedData"]["isDeleted"])

        # update Fixed Data
        modifiedCount = PyKeyPress().updateFixedKeyPressData(dataId, '222222', '[Edited Content Added]', 'Keypresses123', '2016-10-02 18:28:00', False)
        jsonData = PyKeyPress().selectKeyPressDataById(dataId)
        self.assertEqual(1, modifiedCount)
        self.assertEqual(jsonData[0]["fixedData"]["keypress_id"], '222222')
        self.assertEqual(jsonData[0]["fixedData"]["content"], '[Edited Content Added]')
        self.assertEqual(jsonData[0]["fixedData"]["className"], 'Keypresses123')
        self.assertEqual(jsonData[0]["fixedData"]["start"], '2016-10-02 18:28:00')
        self.assertFalse(jsonData[0]["fixedData"]["isDeleted"])

        # delete Fixed Data
        modifiedCount = PyKeyPress().deleteFixedKeyPressData(dataId)
        self.assertEqual(1, modifiedCount)
        jsonData = PyKeyPress().selectKeyPressDataById(dataId)
        self.assertRaises(KeyError, lambda: jsonData[0]["fixedData"])

    def test_annotations(self):
        jsonData = PyKeyPress().selectKeyPressData('2016-10-12 17:36:24', '2016-10-12 17:36:24', [], [], ["Another Event by Alex"])
        dataId = jsonData[0]["id"]

        # test Annotations
        PyKeyPress().addAnnotationKeyPress(dataId, 'test')
        PyKeyPress().addAnnotationKeyPress(dataId, 'test test')
        PyKeyPress().addAnnotationKeyPress(dataId, 'test test test')
        PyKeyPress().addAnnotationKeyPress(dataId, 'test test test')
        addedAnns = PyKeyPress().selectKeyPressDataById(dataId)
        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual('test', addedAnns[0]["annotations"][0]["annotation"])
        self.assertEqual('test test', addedAnns[0]["annotations"][1]["annotation"])
        self.assertEqual('test test test', addedAnns[0]["annotations"][2]["annotation"])

        PyKeyPress().editAnnotationKeyPress(dataId, 'test test', 'updated annotation!!')
        changedAnn = PyKeyPress().selectKeyPressDataById(dataId)
        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual('updated annotation!!', changedAnn[0]["annotations"][1]["annotation"])

        PyKeyPress().deleteAnnotationKeyPress(dataId, 'updated annotation!!')
        deletedChanged = PyKeyPress().selectKeyPressDataById(dataId)
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))

        PyKeyPress().deleteAllAnnotationsForKeyPress(dataId)
        deletedAll = PyKeyPress().selectKeyPressDataById(dataId)
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # add Annotation to Timeline
        objectId = PyKeyPress().addAnnotationToKeyPressTimeline('2016-09-16 09:13:57',
                                                                "here's a Keypress timeline annotation", "Alex", "Super Summer Event")
        addtimelineAnnotation = PyKeyPress().selectKeyPressDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertEqual(addtimelineAnnotation[0]["className"], 'annotation')
        self.assertEqual(addtimelineAnnotation[0]["start"], '2016-09-16 09:13:57')
        self.assertEqual(addtimelineAnnotation[0]["annotations"]["annotation"], "here's a Keypress timeline annotation")
        self.assertEqual(addtimelineAnnotation[0]["metadata"]["techName"], 'Alex')
        self.assertEqual(addtimelineAnnotation[0]["metadata"]["eventName"], 'Super Summer Event')


if __name__ == '__main__':
    unittest.main()

# python -m unittests.test_pyKeyPress
