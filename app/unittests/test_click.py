import unittest
from core.apis.datasource.pyKeyLogger import PyKeyLogger
from pprint import pprint

class PyKeyLoggerTest(unittest.TestCase):

    def test_monolithicTestCase(self):
        # select by date
        jsonData = PyKeyLogger().selectClickData('2016-09-11 11:37:14', '2016-09-11 11:37:20')
        dataId = jsonData[0]["id"]
        self.assertEqual(1, len(jsonData))

        # select by Id
        jsonData = PyKeyLogger().selectClickDataById(dataId)
        pprint(jsonData)
        self.assertEqual(1, len(jsonData))

        # test Annotations
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
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # insert Fixed Data
        modifiedCount = PyKeyLogger().insertFixedClickData(dataId, '2222', '[New Content Added]', 'imgPoint', '2016-09-11 17:37:14', '/usr/logger/v2/dss-logger-pluggable/plugins/collectors/pykeylogger/raw/click_images/1474038815.78_TESTING.png', 'point')
        self.assertEqual(1, modifiedCount)

        # update Fixed Data
        modifiedCount = PyKeyLogger().updateFixedClickData(dataId, '1111','[EDITED UNITTEST Content Added]',' imgPoint', '2016-10-02 19:35:51', '/usr/logger/v2/dss-logger-pluggable/plugins/collectors/pykeylogger/raw/click_images/1474038815.78_TESTING_UPDATE.png', 'point')
        self.assertEqual(1, modifiedCount)

        # delete Fixed Data
        modifiedCount = PyKeyLogger().deleteFixedClickData(dataId)
        self.assertEqual(1, modifiedCount)

        # add Annotation to Timeline
        objectId = PyKeyLogger().addAnnotationToClickTimeline('2016-09-11 17:37:14', "here's a Click timeline annotation")
        addtimelineAnnotation = PyKeyLogger().selectClickDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertIsNotNone(addtimelineAnnotation)


if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_click
