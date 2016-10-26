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

        #select by Tech name
        jsonData = PyTimed().selectTimedData('2016-09-16 09:16:34', '2016-09-16 09:16:40', "Alex", "")
        self.assertEqual(1, len(jsonData))

        #select by event name
        jsonData = PyTimed().selectTimedData('2016-09-16 09:16:34', '2016-09-16 09:16:40', "", "Super Summer Event")
        self.assertEqual(1, len(jsonData))

        #select by tech name AND event name
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
        modifiedCount = PyTimed().insertFixedTimedData(dataId, '11111', '[New Content Added]', 'imgPoint', '2016-09-16 15:16:35', 'http://localhost/dssserver/logs/timed_screenshots/1465515528.8_screenshotTIMED_TESTING.png', 'point')
        self.assertEqual(1, modifiedCount)

        # update Fixed Data
        modifiedCount = PyTimed().updateFixedTimedData(dataId, '22222','[EDITED UNITTEST Content Added]', 'imgPoint', '2016-10-03 18:38:48', '/usr/logger/v2/dss-logger-pluggable/plugins/collectors/pykeylogger/raw/click_images/1474038815.78_TESTING_UPDATE.png', 'point')
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

#python -m unittests.test_pyTimed
