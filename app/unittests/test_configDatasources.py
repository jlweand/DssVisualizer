import unittest
from core.config.configDatasources import ConfigDatasources

class ConfigDatasourcesTest(unittest.TestCase):

    def test_addDatasource(self):
        output = ConfigDatasources().addDatasource("newName", "here's the location")
        self.assertEqual(output, "newName")

        # test adding duplicate datasource
        output = ConfigDatasources().addDatasource("newName", "here's the location")
        self.assertEqual(output, "Duplicate datasource name. Unable to add this datasource plugin.")

    def test_getListOfDatasources(self):
        output = ConfigDatasources().getListOfDatasources()
        self.assertEqual(len(output), 3)

    def test_removeDatasource(self):
        #test removing nonexistant datasource
        output = ConfigDatasources().removeDatasource("dummyName")
        self.assertEqual(output, "Failed to find datasource plugin named dummyName")

        #test removing default datasource
        output = ConfigDatasources().removeDatasource("MongoDB")
        self.assertEqual(output, "Sorry, this plugin cannot be deleted. It is currently in use. Please choose another default plugin before deleting this one.")

        #test removing datasource
        output = ConfigDatasources().removeDatasource("newName")
        self.assertEqual(output, "newName")

    def test_setDefaultDatasource(self):
        output = ConfigDatasources().setDefaultDatasource("Elasticsearch")
        self.assertEqual(output, "Elasticsearch")

        # test setting nonexistant default datasource
        output = ConfigDatasources().setDefaultDatasource("dummyName")
        self.assertEqual(output, "No datasource plugin has been imported for dummyName")

        # set it back to MongoDB
        output = ConfigDatasources().setDefaultDatasource("MongoDB")
        self.assertEqual(output, "MongoDB")

if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_configDatasources
