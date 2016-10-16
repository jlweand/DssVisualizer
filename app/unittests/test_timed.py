import unittest
from core.apis.datasource.pyKeyLogger import PyKeyLogger
import ujson
from pprint import pprint

class PyKeyLoggerTest(unittest.TestCase):

    # Get an objectID of each type of data and update the variables in the main method at the end of this class
    def test_selectTimedData(self):
        jsonData = PyKeyLogger().selectTimedData('2016-09-01 00:00:00', '2016-09-20 00:00:00')
        # pprint(jsonData)
        self.assertEqual(21, len(jsonData))

    def test_selectTimedDataById(self):
        jsonData = PyKeyLogger().selectTimedDataById(timedDataId)
        self.assertEqual(1, len(jsonData))

    def test_timedAnnotations(self):
        PyKeyLogger().addAnnotationTimed(timedDataId, 'test')
        PyKeyLogger().addAnnotationTimed(timedDataId, 'test test')
        PyKeyLogger().addAnnotationTimed(timedDataId, 'test test test')
        PyKeyLogger().addAnnotationTimed(timedDataId, 'test test test')
        addedAnns = PyKeyLogger().selectTimedDataById(timedDataId)

        PyKeyLogger().editAnnotationTimed(timedDataId, 'test test', 'updated annotation!!')
        changedAnn = PyKeyLogger().selectTimedDataById(timedDataId)

        PyKeyLogger().deleteAnnotationTimed(timedDataId, 'updated annotation!!')
        deletedChanged = PyKeyLogger().selectTimedDataById(timedDataId)

        PyKeyLogger().deleteAllAnnotationsForTimed(timedDataId)
        deletedAll = PyKeyLogger().selectTimedDataById(timedDataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

    def test_insertFixedTimedData(self):
        jsonData = PyKeyLogger().insertFixedTimedData(timedDataId, '[New Content Added]', 'imgPoint', '2016-09-09 18:38:48', '2016-09-09 18:38:48', 'http://localhost/dssserver/logs/timed_screenshots/1465515528.8_screenshotTIMED_TESTING.png', 'point')
        self.assertIsNotNone(jsonData)

    def test_updateFixedTimedData(self):
        jsonData = PyKeyLogger().updateFixedTimedData(timedDataId, '57f18796231bad0be406afde','[EDITED UNITTEST Content Added]', '2016-10-03 18:38:48','2016-10-03 18:38:48', '/usr/logger/v2/dss-logger-pluggable/plugins/collectors/pykeylogger/raw/click_images/1474038815.78_TESTING_UPDATE.png', 'point')
        self.assertIsNotNone(jsonData)

    def test_deleteFixedTimedData(self):
        jsonData = PyKeyLogger().deleteFixedTimedData(timedDataId, '57f18796231bad0be406afde')
        self.assertIsNotNone(jsonData)

    def test_addAnnotationToTimedTimeline(self):
        objectId = PyKeyLogger().addAnnotationToTimedTimeline('2016-08-01 10:00:00', "here's a Timed timeline annotation")
        changedAnn = PyKeyLogger().selectTimedDataById(objectId)
        self.assertIsNotNone(changedAnn)


if __name__ == '__main__':
    timedDataId = '5802996d578ad8b73cae8193'
    unittest.main()

#python -m unittests.test_timed