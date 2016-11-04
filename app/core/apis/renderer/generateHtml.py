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

from core.config.configReader import ConfigReader

class GenerateHtml:

    def getPluginFile(self):
        """Get the file where the scripts for the current active renderer plugin live."""
        plugin = ConfigReader().getRedererPluginForPyKeyLogger()
        location = plugin["location"].replace('.', '/') + "/"
        thefile = location + plugin["scripts"]
        return thefile

    def generateHtml(self):
        """This method generates the index.html page based on the current active renderer plugin."""
        # read html file
        html = ''
        with open('viewmanager/index.html.template', 'r') as htmlFile:
            html = htmlFile.read()

        # get the scripts file
        scriptPlugin = self.getPluginFile()
        with open(scriptPlugin, 'r') as scriptFile:
            scripts = scriptFile.read()

        # add the scripts to the HTML and dump it back into the file.
        html = html.replace('<SCRIPTS GO HERE>', scripts)
        with open('viewmanager/index.html', 'w') as htmlFile:
            htmlFile.write(html)
            htmlFile.close()
