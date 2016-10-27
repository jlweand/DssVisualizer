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

from core.apis.datasource.annotations import Annotations

class RAnnotations:

    # return all annotations for the dataObjectId
    def getAnnotations(self, dataObjectId):
        # get the datasource plugin.
        annotationPlugin = self.getInstacneOfPlugin()

        # call the insert method.
        annotations = annotationPlugin.getAnnotations(dataObjectId)
        return annotations

    # add an annotation for the dataObjectId
    def addAnnotation(self, dataObjectId, text):
        return Annotations().addAnnotation(dataObjectId, text);
