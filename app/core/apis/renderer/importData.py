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

from urllib.parse import parse_qs
from time import strftime
from core.config.dataImport import DataImport


class ImportData:

    def importData(self, query):
        """Based on what the UI has selected, export the data"""
        importInfo = parse_qs(query)
        techI = importInfo['tech'][0]
        locationI = importInfo['location'][0]
        commentI = importInfo['comment'][0]
        eventI = importInfo['event'][0]

        copyImagesI = False
        if 'copyImages' in importInfo:
            copyImagesI = True

        if 'date' in importInfo:
            dateI = importInfo['date'][0]
        else:
            dateI = strftime("%Y-%m-%d %H:%M:%S")

        importer = DataImport()
        importer.importAllDataFromFiles(locationI, techI, eventI, commentI, dateI, copyImagesI)
