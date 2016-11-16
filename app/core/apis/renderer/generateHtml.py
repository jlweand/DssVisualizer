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

    def getPluginFile(self, filelocation):
        """Get the file where the scripts for the current active renderer plugin live."""
        with open(filelocation, 'r') as scriptFile:
            scripts = scriptFile.read()
            return scripts


    def compileScriptsForRenderers(self):
        distinctActiveRends = ConfigReader().getDistinctListOfActiveRenderers()
        installedRends = ConfigReader().getListOfRenderers()
        rendScripts = ""
        for drend in distinctActiveRends:
            for rend in installedRends:
                if rend["name"] == drend:
                    rendScripts += self.getPluginFile(rend["location"].replace('.', '/') + "/importScripts/scripts.txt")

        rendScripts += self.getPluginFile(ConfigReader().getRedererPluginForPyKeyLogger()+ "/importScripts/keyloggerScript.txt")
        rendScripts += self.getPluginFile(ConfigReader().getRedererPluginForPcap()+ "/importScripts/pcapScript.txt")
        rendScripts += self.getPluginFile(ConfigReader().getRedererPluginForScreenshots()+ "/importScripts/screenshotScript.txt")
        return rendScripts

    def generateHtml(self):
        """This method generates the index.html page based on the current active renderer plugin."""
        # read html file
        html = ''
        with open('viewmanager/index.html.template', 'r') as htmlFile:
            html = htmlFile.read()

        # get the scripts file(s)
        pluginScripts = self.compileScriptsForRenderers()

        # add the scripts to the HTML and dump it back into the file.
        html = html.replace('<SCRIPTS GO HERE>', pluginScripts)
        with open('viewmanager/index.html', 'w') as htmlFile:
            htmlFile.write(html)
            htmlFile.close()
