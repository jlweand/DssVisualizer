import unittest
import time
from core.config.configDatasources import ConfigDatasources

class ConfigDatasourcesTest(unittest.TestCase):

    def test_addDatasource(self):
        output = ConfigDatasources().addDatasource("newName", "here's the location")
        self.assertEqual(output, "newName")
        time.sleep(0)

    def test_addDuplicateDatasource(self):
        output = ConfigDatasources().addDatasource("newName", "here's the location")
        self.assertEqual(output, "Duplicate datasource name. Unable to add this datasource plugin.")
        time.sleep(0)

    def test_getListOfDatasources(self):
        output = ConfigDatasources().getListOfDatasources()
        self.assertEqual(len(output), 3)
        time.sleep(0)

    def test_setDefaultDatasource(self):
        output = ConfigDatasources().setDefaultDatasource("newName")
        self.assertEqual(output, "newName")
        time.sleep(0)

    def test_setDefaultDatasource(self):
        output = ConfigDatasources().setDefaultDatasource("dummyName")
        self.assertEqual(output, "No datasource plugin has been imported for dummyName")
        time.sleep(0)

    def test_setDefaultDatasource(self):
        output = ConfigDatasources().setDefaultDatasource("MongoDB")
        self.assertEqual(output, "MongoDB")
        time.sleep(0)

    def test_removeDatasource(self):
        output = ConfigDatasources().removeDatasource("newName")
        self.assertEqual(output, "newName")
        time.sleep(0)

    def test_removeNonexistantDatasource(self):
        output = ConfigDatasources().removeDatasource("newName")
        self.assertEqual(output, "Failed to find datasource plugin named newName")
        time.sleep(0)

    def test_removeDefaultDatasource(self):
        output = ConfigDatasources().removeDatasource("MongoDB")
        self.assertEqual(output, "Sorry, this plugin cannot be deleted. It is currently in use. Please choose another default plugin before deleting this one.")

if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_configDatasources
