import unittest
from core.apis.datasource.pyKeyLogger import PyKeyLogger
from pprint import pprint

class PyKeyLoggerTest(unittest.TestCase):

    # Get an objectID of each type of data and update the variables in the main method at the end of this class

    def test_selectKeyPressData(self):
        jsonData = PyKeyLogger().selectKeyPressData('2016-09-01 00:00:00', '2016-09-20 00:00:00')
        # pprint(jsonData)
        self.assertEqual(24, len(jsonData))

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
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

    def test_insertFixedKeyPressData(self):
        jsonData = PyKeyLogger().insertFixedKeyPressData(keyPressDataId, '[New Content Added]', 'Keypresses', '2016-10-02 17:15:00')
        self.assertIsNotNone(jsonData)

    def test_updateFixedKeyPressData(self):
        jsonData = PyKeyLogger().updateFixedKeyPressData(keyPressDataId, '57edcee5231bad04bccd2c0a', '[Edited Content Added]', '2016-10-02 18:28:00')
        self.assertIsNotNone(jsonData)

    def test_deleteFixedKeyPressData(self):
        jsonData = PyKeyLogger().deleteFixedKeyPressData(keyPressDataId, '57edcee5231bad04bccd2c0a')
        self.assertIsNotNone(jsonData)

    def test_addAnnotationToKeyPressTimeline(self):
        objectId = PyKeyLogger().addAnnotationToKeyPressTimeline('2016-08-01 10:00:00', "here's a Keypress timeline annotation")
        changedAnn = PyKeyLogger().selectKeyPressDataById(objectId)
        self.assertIsNotNone(changedAnn)

if __name__ == '__main__':
    keyPressDataId = '5802996d578ad8b73cae815e'
    unittest.main()

#python -m unittests.test_keyPress
