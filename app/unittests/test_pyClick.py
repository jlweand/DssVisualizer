import unittest
from core.apis.datasource.pyClick import PyClick
from pprint import pprint

class PyKeyLoggerTest(unittest.TestCase):

    def test_monolithicTestCase(self):
        # select by date
        jsonData = PyClick().selectClickData('2016-10-18 18:25:34', '2016-10-18 18:25:34')
        dataId = jsonData[0]["id"]
        self.assertEqual(1, len(jsonData))

        # select by Id
        jsonData = PyClick().selectClickDataById(dataId)
        pprint(jsonData)
        self.assertEqual(1, len(jsonData))

        # test Annotations
        PyClick().addAnnotationClick(dataId, 'test')
        PyClick().addAnnotationClick(dataId, 'test test')
        PyClick().addAnnotationClick(dataId, 'test test test')
        PyClick().addAnnotationClick(dataId, 'test test test')
        addedAnns = PyClick().selectClickDataById(dataId)

        PyClick().editAnnotationClick(dataId, 'test test', 'updated annotation!!')
        changedAnn = PyClick().selectClickDataById(dataId)

        PyClick().deleteAnnotationClick(dataId, 'updated annotation!!')
        deletedChanged = PyClick().selectClickDataById(dataId)

        PyClick().deleteAllAnnotationsForClick(dataId)
        deletedAll = PyClick().selectClickDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # insert Fixed Data
        modifiedCount = PyClick().insertFixedClickData(dataId, '2222', '[New Content Added]', 'imgPoint', '2016-09-11 17:37:14', '/usr/logger/v2/dss-logger-pluggable/plugins/collectors/pykeylogger/raw/click_images/1474038815.78_TESTING.png', 'point')
        self.assertEqual(1, modifiedCount)

        # update Fixed Data
        modifiedCount = PyClick().updateFixedClickData(dataId, '1111','[EDITED UNITTEST Content Added]',' imgPoint', '2016-10-02 19:35:51', '/usr/logger/v2/dss-logger-pluggable/plugins/collectors/pykeylogger/raw/click_images/1474038815.78_TESTING_UPDATE.png', 'point')
        self.assertEqual(1, modifiedCount)

        # delete Fixed Data
        modifiedCount = PyClick().deleteFixedClickData(dataId)
        self.assertEqual(1, modifiedCount)

        # add Annotation to Timeline
        objectId = PyClick().addAnnotationToClickTimeline('2016-09-11 17:37:14', "here's a Click timeline annotation")
        addtimelineAnnotation = PyClick().selectClickDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertIsNotNone(addtimelineAnnotation)


if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_pyClick
