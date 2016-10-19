import unittest
from core.apis.datasource.pyKeyLogger import PyKeyLogger
from pprint import pprint

class PyKeyLoggerTest(unittest.TestCase):

    def test_monolithicTestCase(self):
        # select by date
        jsonData = PyKeyLogger().selectTimedData('2016-09-16 09:16:34', '2016-09-16 09:16:40')
        dataId = jsonData[0]["id"]
        self.assertEqual(1, len(jsonData))

        # select by Id
        jsonData = PyKeyLogger().selectTimedDataById(dataId)
        pprint(jsonData)
        self.assertEqual(1, len(jsonData))

        # test Annotations
        PyKeyLogger().addAnnotationTimed(dataId, 'test')
        PyKeyLogger().addAnnotationTimed(dataId, 'test test')
        PyKeyLogger().addAnnotationTimed(dataId, 'test test test')
        PyKeyLogger().addAnnotationTimed(dataId, 'test test test')
        addedAnns = PyKeyLogger().selectTimedDataById(dataId)

        PyKeyLogger().editAnnotationTimed(dataId, 'test test', 'updated annotation!!')
        changedAnn = PyKeyLogger().selectTimedDataById(dataId)

        PyKeyLogger().deleteAnnotationTimed(dataId, 'updated annotation!!')
        deletedChanged = PyKeyLogger().selectTimedDataById(dataId)

        PyKeyLogger().deleteAllAnnotationsForTimed(dataId)
        deletedAll = PyKeyLogger().selectTimedDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # insert Fixed Data
        jsonData = PyKeyLogger().insertFixedTimedData(dataId, '57f18796231bad0be406afde', '[New Content Added]', 'imgPoint', '2016-09-16 15:16:35', 'http://localhost/dssserver/logs/timed_screenshots/1465515528.8_screenshotTIMED_TESTING.png', 'point')
        self.assertIsNotNone(jsonData)

        # update Fixed Data
        jsonData = PyKeyLogger().updateFixedTimedData(dataId, '57f18796231bad0be406afde','[EDITED UNITTEST Content Added]', 'imgPoint', '2016-10-03 18:38:48', '/usr/logger/v2/dss-logger-pluggable/plugins/collectors/pykeylogger/raw/click_images/1474038815.78_TESTING_UPDATE.png', 'point')
        self.assertIsNotNone(jsonData)

        # delete Fixed Data
        jsonData = PyKeyLogger().deleteFixedTimedData(dataId, '57f18796231bad0be406afde')
        self.assertIsNotNone(jsonData)

        # add Annotation to Timeline
        objectId = PyKeyLogger().addAnnotationToTimedTimeline('2016-09-16 15:16:34', "here's a Timed timeline annotation")
        addtimelineAnnotation = PyKeyLogger().selectTimedDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertIsNotNone(addtimelineAnnotation)


if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_timed