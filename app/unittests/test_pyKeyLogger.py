import unittest
from core.apis.datasource.pyKeyLogger import PyKeyLogger
import ujson
from pprint import pprint

class PyKeyLoggerTest(unittest.TestCase):

    # Get an objectID of each type of data and update the variables in the main method at the end of this class

    def test_selectKeyPressData(self):
        jsonData = PyKeyLogger().selectKeyPressData('2016-08-01 00:00:00', '2016-08-20 00:00:00')
        self.assertEqual(9, len(jsonData))

    def test_selectKeyPressDataById(self):
        jsonData = PyKeyLogger().selectKeyPressDataById(keyPressDataId)
        self.assertEqual(1, len(jsonData))

    def test_keyPressAnnotations(self):
        PyKeyLogger().addAnnotationKeyPress(keyPressDataId, 'test')
        PyKeyLogger().addAnnotationKeyPress(keyPressDataId, 'test test')
        PyKeyLogger().addAnnotationKeyPress(keyPressDataId, 'test test test')
        PyKeyLogger().addAnnotationKeyPress(keyPressDataId, 'test test test')
        addedAnns = PyKeyLogger().selectKeyPressDataById(keyPressDataId)

        PyKeyLogger().editAnnotationKeyPress(keyPressDataId, 'test test', 'updated annotation!!')
        changedAnn = PyKeyLogger().selectKeyPressDataById(keyPressDataId)

        PyKeyLogger().deleteAnnotationKeyPress(keyPressDataId, 'updated annotation!!')
        deletedChanged = PyKeyLogger().selectKeyPressDataById(keyPressDataId)

        PyKeyLogger().deleteAllAnnotationsForKeyPress(keyPressDataId)
        deletedAll = PyKeyLogger().selectKeyPressDataById(keyPressDataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertEqual(0, len(deletedAll[0]["annotations"]))

    def test_insertFixedKeyPressData(self):
        jsonData = PyKeyLogger().insertFixedKeyPressData(keyPressDataId, '[New Content Added]', 'Keypresses', '2016-10-02 17:15:00')
        self.assertIsNotNone(jsonData)

    def test_updateFixedKeyPressData(self):
        jsonData = PyKeyLogger().updateFixedKeyPressData(keyPressDataId, '[Edited Content Added]', '2016-10-02 18:28:00')
        self.assertIsNotNone(jsonData)

    def test_deleteFixedKeyPressData(self):
        jsonData = PyKeyLogger().deleteFixedKeyPressData(keyPressDataId)
        self.assertIsNotNone(jsonData)

    def test_addAnnotationToKeyPressTimeline(self):
        objectId = PyKeyLogger().addAnnotationToKeyPressTimeline('2016-08-01 10:00:00', "here's a Keypress timeline annotation")
        changedAnn = PyKeyLogger().selectKeyPressDataById(objectId)
        self.assertIsNotNone(changedAnn)

#Click#
    def test_selectClickData(self):
        jsonData = PyKeyLogger().selectClickData('2016-09-01 00:00:00', '2016-09-20 00:00:00')
        self.assertEqual(8, len(jsonData))

    def test_selectClickDataById(self):
        jsonData = PyKeyLogger().selectClickDataById(clickDataId)
        self.assertEqual(1, len(jsonData))

    def test_clickAnnotations(self):
        PyKeyLogger().addAnnotationClick(clickDataId, 'test')
        PyKeyLogger().addAnnotationClick(clickDataId, 'test test')
        PyKeyLogger().addAnnotationClick(clickDataId, 'test test test')
        PyKeyLogger().addAnnotationClick(clickDataId, 'test test test')
        addedAnns = PyKeyLogger().selectClickDataById(clickDataId)

        PyKeyLogger().editAnnotationClick(clickDataId, 'test test', 'updated annotation!!')
        changedAnn = PyKeyLogger().selectClickDataById(clickDataId)

        PyKeyLogger().deleteAnnotationClick(clickDataId, 'updated annotation!!')
        deletedChanged = PyKeyLogger().selectClickDataById(clickDataId)

        PyKeyLogger().deleteAllAnnotationsForClick(clickDataId)
        deletedAll = PyKeyLogger().selectClickDataById(clickDataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertEqual(0, len(deletedAll[0]["annotations"]))

    def test_insertFixedKeyPressData(self):
        jsonData = PyKeyLogger().insertFixedClickData(clickDataId, '[New Content Added]', 'imgPoint', '2016-10-02 17:35:51', '2016-10-02 17:35:51', '/usr/logger/v2/dss-logger-pluggable/plugins/collectors/pykeylogger/raw/click_images/1474038815.78_TESTING.png', 'point')
        self.assertIsNotNone(jsonData)

    def test_updateFixedClickData(self):
        jsonData = PyKeyLogger().updateFixedClickData(clickDataId, '[EDITED UNITTEST Content Added]', '2016-10-02 19:35:51','2016-10-02 19:35:51', '/usr/logger/v2/dss-logger-pluggable/plugins/collectors/pykeylogger/raw/click_images/1474038815.78_TESTING_UPDATE.png', 'point')
        self.assertIsNotNone(jsonData)

    def test_deleteFixedKeyPressData(self):
        jsonData = PyKeyLogger().deleteFixedClickData(clickDataId)
        self.assertIsNotNone(jsonData)

    def test_addAnnotationToClickTimeline(self):
        objectId = PyKeyLogger().addAnnotationToClickTimeline('2016-08-01 10:00:00', "here's a Click timeline annotation")
        changedAnn = PyKeyLogger().selectClickDataById(objectId)
        self.assertIsNotNone(changedAnn)

#Timed#
    def test_selectTimedData(self):
        jsonData = PyKeyLogger().selectTimedData('2016-09-01 00:00:00', '2016-09-20 00:00:00')
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
        self.assertEqual(0, len(deletedAll[0]["annotations"]))

    def test_insertFixedTimedData(self):
        jsonData = PyKeyLogger().insertFixedTimedData(timedDataId, '[New Content Added]', 'imgPoint', '2016-09-09 18:38:48', '2016-09-09 18:38:48', 'http://localhost/dssserver/logs/timed_screenshots/1465515528.8_screenshotTIMED_TESTING.png', 'point')
        self.assertIsNotNone(jsonData)

    def test_updateFixedTimedData(self):
        jsonData = PyKeyLogger().updateFixedTimedData(timedDataId, '[EDITED UNITTEST Content Added]', '2016-10-03 18:38:48', '2016-10-03 18:38:48', '/usr/logger/v2/dss-logger-pluggable/plugins/collectors/pykeylogger/raw/click_images/1474038815.78_TESTING_UPDATE.png', 'point')
        self.assertIsNotNone(jsonData)

    def test_deleteFixedTimedData(self):
        jsonData = PyKeyLogger().deleteFixedTimedData(timedDataId)
        self.assertIsNotNone(jsonData)

    def test_addAnnotationToTimedTimeline(self):
        objectId = PyKeyLogger().addAnnotationToTimedTimeline('2016-08-01 10:00:00', "here's a Timed timeline annotation")
        changedAnn = PyKeyLogger().selectTimedDataById(objectId)
        self.assertIsNotNone(changedAnn)


if __name__ == '__main__':
    keyPressDataId = '57f19062578ad8ca217b212d'
    clickDataId = '57f19062578ad8ca217b210d'
    timedDataId = '57f19062578ad8ca217b2123'
    unittest.main()

#python -m unittests.test_pyKeyLogger
