import unittest
from core.apis.datasource.pyKeyLogger import PyKeyLogger
from pprint import pprint

class PyKeyLoggerTest(unittest.TestCase):

    # Get an objectID of each type of data and update the variables in the main method at the end of this class

    def test_selectClickData(self):
        jsonData = PyKeyLogger().selectClickData('2016-09-01 00:00:00', '2016-09-20 00:00:00')
        # pprint(jsonData)
        self.assertEqual(12, len(jsonData))

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
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

    def test_insertFixedClickData(self):
        jsonData = PyKeyLogger().insertFixedClickData(clickDataId, '[New Content Added]', 'imgPoint', '2016-10-02 17:35:51', '2016-10-02 17:35:51', '/usr/logger/v2/dss-logger-pluggable/plugins/collectors/pykeylogger/raw/click_images/1474038815.78_TESTING.png', 'point')
        self.assertIsNotNone(jsonData)

    def test_updateFixedClickData(self):
        jsonData = PyKeyLogger().updateFixedClickData(clickDataId, '57f18727231bad12ecba99e4','[EDITED UNITTEST Content Added]', '2016-10-02 19:35:51','2016-10-02 19:35:51', '/usr/logger/v2/dss-logger-pluggable/plugins/collectors/pykeylogger/raw/click_images/1474038815.78_TESTING_UPDATE.png', 'point')
        self.assertIsNotNone(jsonData)

    def test_deleteFixedClickData(self):
        jsonData = PyKeyLogger().deleteFixedClickData(clickDataId, '57f18727231bad12ecba99e4')
        self.assertIsNotNone(jsonData)

    def test_addAnnotationToClickTimeline(self):
        objectId = PyKeyLogger().addAnnotationToClickTimeline('2016-08-01 10:00:00', "here's a Click timeline annotation")
        changedAnn = PyKeyLogger().selectClickDataById(objectId)
        self.assertIsNotNone(changedAnn)


if __name__ == '__main__':
    clickDataId = '5802996d578ad8b73cae817c'
    unittest.main()

#python -m unittests.test_click
