#  Copyright (C) 2016  Jamie Acosta, Jennifer Weand, Juan Soto, Mark Eby, Mark Smith, Andres Olivas
#
# This file is part of DssVisualizer.
#
# DssVisualizer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DssVisualizer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DssVisualizer.  If not, see <http://www.gnu.org/licenses/>.

import unittest
from core.config.configDatasources import ConfigDatasources

class ConfigDatasourcesTest(unittest.TestCase):

    def test_addDatasource(self):
        output = ConfigDatasources().addDatasource("newName", "here's the location")
        self.assertEqual(output, "newName")

        # test adding duplicate datasource
        output = ConfigDatasources().addDatasource("newName", "here's the location")
        self.assertEqual(output, "Duplicate datasource name. Unable to add this datasource plugin.")

    def test_removeDatasource(self):
        # test removing nonexistant datasource
        output = ConfigDatasources().removeDatasource("dummyName")
        self.assertEqual(output, "Failed to find datasource plugin named dummyName")

        # test removing default datasource
        output = ConfigDatasources().removeDatasource("MongoDB")
        self.assertEqual(output,
                         "Sorry, this plugin cannot be deleted. It is currently in use. Please choose another default plugin before deleting this one.")

        # test removing datasource
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

# python -m unittests.test_configDatasources
