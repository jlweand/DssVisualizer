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
from core.apis.datasource.manualScreenShot import ManualScreenShot
from pprint import pprint


class ManualScreenShotTest(unittest.TestCase):
    def test_monolithicTestCase(self):
        # select by date
        jsonData = ManualScreenShot().selectManualScreenShotData('2016-10-12 17:37:00', '2016-10-12 17:37:02', [], [], [])
        self.assertEqual(5, len(jsonData))
        dataId = jsonData[0]["id"]

        # select by Id
        jsonData = ManualScreenShot().selectManualScreenShotDataById(dataId)
        pprint(jsonData)
        self.assertEqual(1, len(jsonData))

        # select by Tech name
        jsonData = ManualScreenShot().selectManualScreenShotData('2016-10-12 17:37:00', '2016-10-12 17:37:02', ["Alex"], [], [])
        self.assertEqual(2, len(jsonData))

        # select by event name
        jsonData = ManualScreenShot().selectManualScreenShotData('2016-10-12 17:37:00', '2016-10-12 17:37:02', [], ["Super Summer Event"], [])
        self.assertEqual(2, len(jsonData))

        # select by tech name AND event name
        jsonData = ManualScreenShot().selectManualScreenShotData('2016-10-12 17:37:00', '2016-10-12 17:37:02', ["Alex"], ["Super Summer Event"], [])
        self.assertEqual(1, len(jsonData))

        # select by event/tech combo
        jsonData = ManualScreenShot().selectManualScreenShotData('2016-10-12 17:37:00', '2016-10-12 17:37:02', [], [], ["Another Event by Julie"])
        self.assertEqual(1, len(jsonData))

        # test Annotations
        ManualScreenShot().addAnnotationManualScreenShot(dataId, 'test')
        ManualScreenShot().addAnnotationManualScreenShot(dataId, 'test test')
        ManualScreenShot().addAnnotationManualScreenShot(dataId, 'test test test')
        ManualScreenShot().addAnnotationManualScreenShot(dataId, 'test test test')
        addedAnns = ManualScreenShot().selectManualScreenShotDataById(dataId)

        ManualScreenShot().editAnnotationManualScreenShot(dataId, 'test test', 'updated annotation!!')
        changedAnn = ManualScreenShot().selectManualScreenShotDataById(dataId)

        ManualScreenShot().deleteAnnotationManualScreenShot(dataId, 'updated annotation!!')
        deletedChanged = ManualScreenShot().selectManualScreenShotDataById(dataId)

        ManualScreenShot().deleteAllAnnotationsForManualScreenShot(dataId)
        deletedAll = ManualScreenShot().selectManualScreenShotDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # insert Fixed Data
        modifiedCount = ManualScreenShot().insertFixedManualScreenShotData(dataId, '2222', '[New Content Added]', 'imgPoint',
                                                       '2016-10-29 15:07:00',
                                                       '/new/path/1474038815.78_TESTING.png',
                                                       'point')
        self.assertEqual(1, modifiedCount)

        # update Fixed Data
        modifiedCount = ManualScreenShot().updateFixedManualScreenShotData(dataId, '1111', '[EDITED UNITTEST Content Added]', ' imgPoint',
                                                       '2016-10-29 15:07:00',
                                                       '/newpath/manualscreenshot/1474038815.78_TESTING_UPDATE.png',
                                                       'point')
        self.assertEqual(1, modifiedCount)

        # delete Fixed Data
        modifiedCount = ManualScreenShot().deleteFixedManualScreenShotData(dataId)
        self.assertEqual(1, modifiedCount)

        # add Annotation to Timeline
        objectId = ManualScreenShot().addAnnotationToManualScreenShotTimeline('2016-10-29 15:07:00', "here's a ManualScreenShot timeline annotation", "Alex", "Super Summer Event")
        addtimelineAnnotation = ManualScreenShot().selectManualScreenShotDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertIsNotNone(addtimelineAnnotation)


if __name__ == '__main__':
    unittest.main()

# python -m unittests.test_manualScreenShot
