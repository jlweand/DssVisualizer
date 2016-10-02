import unittest
from core.apis.datasource.pyKeyLogger import PyKeyLogger
import ujson
from pprint import pprint

class PyKeyLoggerTest(unittest.TestCase):

    def test_selectKeyPressData(self):
        jsonData = PyKeyLogger().selectKeyPressData('2016-08-01 00:00:00', '2016-08-20 00:00:00')
        self.assertEqual(9, len(jsonData))

    def test_selectKeyPressDataById(self):
        jsonData = PyKeyLogger().selectKeyPressDataById('57f19062578ad8ca217b212d')
        self.assertEqual(1, len(jsonData))

    def test_keyPressAnnotations(self):
        dataId = '57f19062578ad8ca217b212d'
        PyKeyLogger().addAnnotationKeyPress(dataId, 'test')
        PyKeyLogger().addAnnotationKeyPress(dataId, 'test test')
        PyKeyLogger().addAnnotationKeyPress(dataId, 'test test test')
        PyKeyLogger().addAnnotationKeyPress(dataId, 'test test test')
        addedAnns = PyKeyLogger().selectKeyPressDataById(dataId)

        PyKeyLogger().editAnnotationKeyPress(dataId, 'test test', 'updated annotation!!')
        changedAnn = PyKeyLogger().selectKeyPressDataById(dataId)

        PyKeyLogger().deleteAnnotationKeyPress(dataId, 'updated annotation!!')
        deletedChanged = PyKeyLogger().selectKeyPressDataById(dataId)

        PyKeyLogger().deleteAllAnnotationsForKeyPress(dataId)
        deletedAll = PyKeyLogger().selectKeyPressDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertEqual(0, len(deletedAll[0]["annotations"]))

#Click#
    def test_selectClickData(self):
        jsonData = PyKeyLogger().selectClickData('2016-09-01 00:00:00', '2016-09-20 00:00:00')
        self.assertEqual(8, len(jsonData))

    def test_selectClickDataById(self):
        jsonData = PyKeyLogger().selectClickDataById('57f19062578ad8ca217b210d')
        self.assertEqual(1, len(jsonData))

    def test_clickAnnotations(self):
        dataId = '57f19062578ad8ca217b210d'
        PyKeyLogger().addAnnotationClick(dataId, 'test')
        PyKeyLogger().addAnnotationClick(dataId, 'test test')
        PyKeyLogger().addAnnotationClick(dataId, 'test test test')
        PyKeyLogger().addAnnotationClick(dataId, 'test test test')
        addedAnns = PyKeyLogger().selectClickDataById(dataId)

        PyKeyLogger().editAnnotationClick(dataId, 'test test', 'updated annotation!!')
        changedAnn = PyKeyLogger().selectClickDataById(dataId)

        PyKeyLogger().deleteAnnotationClick(dataId, 'updated annotation!!')
        deletedChanged = PyKeyLogger().selectClickDataById(dataId)

        PyKeyLogger().deleteAllAnnotationsForClick(dataId)
        deletedAll = PyKeyLogger().selectClickDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertEqual(0, len(deletedAll[0]["annotations"]))

#Timed#
    def test_selectTimedData(self):
        jsonData = PyKeyLogger().selectTimedData('2016-09-01 00:00:00', '2016-09-20 00:00:00')
        self.assertEqual(21, len(jsonData))

    def test_selectTimedDataById(self):
        jsonData = PyKeyLogger().selectTimedDataById('57f19062578ad8ca217b2123')
        self.assertEqual(1, len(jsonData))

    def test_timedAnnotations(self):
        dataId = '57f19062578ad8ca217b2123'
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
        self.assertEqual(0, len(deletedAll[0]["annotations"]))

if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_pyKeyLogger
