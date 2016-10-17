import unittest
from core.apis.datasource.pyKeyLogger import PyKeyLogger

class PyKeyLoggerTest(unittest.TestCase):

    def test_monolithicTestCase(self):
        # select by date
        jsonData = PyKeyLogger().selectClickData('2016-09-01 00:00:00', '2016-09-20 00:00:00')
        dataId = jsonData[0]["id"]
        self.assertEqual(12, len(jsonData))

        # select by Id
        jsonData = PyKeyLogger().selectClickDataById(dataId)
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
        jsonData = PyKeyLogger().insertFixedClickData(dataId, '[New Content Added]', 'imgPoint', '2016-10-02 17:35:51', '2016-10-02 17:35:51', '/usr/logger/v2/dss-logger-pluggable/plugins/collectors/pykeylogger/raw/click_images/1474038815.78_TESTING.png', 'point')
        self.assertIsNotNone(jsonData)

        # update Fixed Data
        jsonData = PyKeyLogger().updateFixedClickData(dataId, '57f18727231bad12ecba99e4','[EDITED UNITTEST Content Added]', '2016-10-02 19:35:51','2016-10-02 19:35:51', '/usr/logger/v2/dss-logger-pluggable/plugins/collectors/pykeylogger/raw/click_images/1474038815.78_TESTING_UPDATE.png', 'point')
        self.assertIsNotNone(jsonData)

        # delete Fixed Data
        jsonData = PyKeyLogger().deleteFixedClickData(dataId, '57f18727231bad12ecba99e4')
        self.assertIsNotNone(jsonData)

        # add Annotation to Timeline
        objectId = PyKeyLogger().addAnnotationToClickTimeline('2016-08-01 10:00:00', "here's a Click timeline annotation")
        changedAnn = PyKeyLogger().selectClickDataById(objectId)
        self.assertIsNotNone(changedAnn)


if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_click
