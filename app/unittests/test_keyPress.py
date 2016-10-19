import unittest
from core.apis.datasource.pyKeyLogger import PyKeyLogger
from pprint import pprint

class PyKeyLoggerTest(unittest.TestCase):

    def test_monolithicTestCase(self):
        # select by date
        jsonData = PyKeyLogger().selectKeyPressData('2016-10-15 11:58:35', '2016-10-15 11:58:40')
        dataId = jsonData[0]["id"]
        self.assertEqual(2, len(jsonData))

        # select by Id
        jsonData = PyKeyLogger().selectKeyPressDataById(dataId)
        pprint(jsonData)
        self.assertEqual(1, len(jsonData))

        # test Annotations
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
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # insert Fixed Data
        jsonData = PyKeyLogger().insertFixedKeyPressData(dataId, '57edcee5231bad04bccd2c0a', '[New Content Added]', 'Keypresses', '2016-10-15 17:58:31')
        self.assertIsNotNone(jsonData)

        # update Fixed Data
        jsonData = PyKeyLogger().updateFixedKeyPressData(dataId, '57edcee5231bad04bccd2c0a', '[Edited Content Added]', 'Keypresses', '2016-10-02 18:28:00')
        self.assertIsNotNone(jsonData)

        # delete Fixed Data
        jsonData = PyKeyLogger().deleteFixedKeyPressData(dataId, '57edcee5231bad04bccd2c0a')
        self.assertIsNotNone(jsonData)

        # add Annotation to Timeline
        objectId = PyKeyLogger().addAnnotationToKeyPressTimeline('2016-09-16 09:13:57', "here's a Keypress timeline annotation")
        addtimelineAnnotation = PyKeyLogger().selectKeyPressDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertIsNotNone(addtimelineAnnotation)

if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_keyPress
