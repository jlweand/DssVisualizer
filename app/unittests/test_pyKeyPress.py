import unittest
from core.apis.datasource.pyKeyPress import PyKeyPress
from pprint import pprint

class PyKeyLoggerTest(unittest.TestCase):

    def test_monolithicTestCase(self):
        # select by date
        jsonData = PyKeyPress().selectKeyPressData('2016-10-15 11:58:35', '2016-10-15 11:58:40')
        dataId = jsonData[0]["id"]
        self.assertEqual(2, len(jsonData))

        # select by Id
        jsonData = PyKeyPress().selectKeyPressDataById(dataId)
        pprint(jsonData)
        self.assertEqual(1, len(jsonData))

        # test Annotations
        PyKeyPress().addAnnotationKeyPress(dataId, 'test')
        PyKeyPress().addAnnotationKeyPress(dataId, 'test test')
        PyKeyPress().addAnnotationKeyPress(dataId, 'test test test')
        PyKeyPress().addAnnotationKeyPress(dataId, 'test test test')
        addedAnns = PyKeyPress().selectKeyPressDataById(dataId)

        PyKeyPress().editAnnotationKeyPress(dataId, 'test test', 'updated annotation!!')
        changedAnn = PyKeyPress().selectKeyPressDataById(dataId)

        PyKeyPress().deleteAnnotationKeyPress(dataId, 'updated annotation!!')
        deletedChanged = PyKeyPress().selectKeyPressDataById(dataId)

        PyKeyPress().deleteAllAnnotationsForKeyPress(dataId)
        deletedAll = PyKeyPress().selectKeyPressDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # insert Fixed Data
        modifiedCount = PyKeyPress().insertFixedKeyPressData(dataId, '11111', '[New Content Added]', 'Keypresses', '2016-10-15 17:58:31')
        self.assertEqual(1, modifiedCount)

        # update Fixed Data
        modifiedCount = PyKeyPress().updateFixedKeyPressData(dataId, '222222', '[Edited Content Added]', 'Keypresses', '2016-10-02 18:28:00')
        self.assertEqual(1, modifiedCount)

        # delete Fixed Data
        modifiedCount = PyKeyPress().deleteFixedKeyPressData(dataId)
        self.assertEqual(1, modifiedCount)

        # add Annotation to Timeline
        objectId = PyKeyPress().addAnnotationToKeyPressTimeline('2016-09-16 09:13:57', "here's a Keypress timeline annotation")
        addtimelineAnnotation = PyKeyPress().selectKeyPressDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertIsNotNone(addtimelineAnnotation)

if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_pyKeyPress
