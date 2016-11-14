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


class PyKeyLoggerTest(unittest.TestCase):
    def test_monolithicTestCase(self):
        # select by date
        jsonData = PyKeyPress().selectKeyPressData('2016-10-15 11:59:34', '2016-10-15 11:59:34', [], [], [])
        self.assertEqual(5, len(jsonData))
        dataId = jsonData[0]["id"]

        # select by Id
        jsonData = PyKeyPress().selectKeyPressDataById(dataId)
        pprint(jsonData)
        self.assertEqual(1, len(jsonData))

        # select by Tech name
        jsonData = PyKeyPress().selectKeyPressData('2016-10-15 11:59:34', '2016-10-15 11:59:34', ["Alex"], [], [])
        self.assertEqual(2, len(jsonData))

        # select by event name
        jsonData = PyKeyPress().selectKeyPressData('2016-10-15 11:59:34', '2016-10-15 11:59:34', [], ["Super Summer Event"], [])
        self.assertEqual(2, len(jsonData))

        # select by tech name AND event name
        jsonData = PyKeyPress().selectKeyPressData('2016-10-15 11:59:34', '2016-10-15 11:59:34', ["Alex"], ["Super Summer Event"], [])
        self.assertEqual(1, len(jsonData))

        # select by event/tech combo
        jsonData = PyKeyPress().selectKeyPressData('2016-10-15 11:59:34', '2016-10-15 11:59:34', [], [], ["Another Event by Julie"])
        self.assertEqual(1, len(jsonData))

        # test Annotations
        PyKeyPress().addAnnotationKeyPress(dataId, 'test')
        PyKeyPress().addAnnotationKeyPress(dataId, 'test test')
        PyKeyPress().addAnnotationKeyPress(dataId, 'test test test')
        PyKeyPress().addAnnotationKeyPress(dataId, 'test test test')
        addedAnns = PyKeyPress().selectKeyPressDataById(dataId)

        PyKeyPress().editAnnotationKeyPress(dataId, 'test test', 'updated annotation!!')
        changedAnn = PyKeyPress().selectKeyPressDataById(dataId)

        PyKeyPress().deleteAnnotationKeyPress(dataId, 'updated annotation!!')
        deletedChanged = PyKeyPress().selectKeyPressDataById(dataId)

        PyKeyPress().deleteAllAnnotationsForKeyPress(dataId)
        deletedAll = PyKeyPress().selectKeyPressDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # insert Fixed Data
        modifiedCount = PyKeyPress().insertFixedKeyPressData(dataId, '11111', '[New Content Added]', 'Keypresses',
                                                             '2016-10-15 17:58:31')
        self.assertEqual(1, modifiedCount)

        # update Fixed Data
        modifiedCount = PyKeyPress().updateFixedKeyPressData(dataId, '222222', '[Edited Content Added]', 'Keypresses',
                                                             '2016-10-02 18:28:00')
        self.assertEqual(1, modifiedCount)

        # delete Fixed Data
        modifiedCount = PyKeyPress().deleteFixedKeyPressData(dataId)
        self.assertEqual(1, modifiedCount)

        # add Annotation to Timeline
        objectId = PyKeyPress().addAnnotationToKeyPressTimeline('2016-09-16 09:13:57',
                                                                "here's a Keypress timeline annotation", "Alex", "Super Summer Event")
        addtimelineAnnotation = PyKeyPress().selectKeyPressDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertIsNotNone(addtimelineAnnotation)


if __name__ == '__main__':
    unittest.main()

# python -m unittests.test_pyKeyPress
