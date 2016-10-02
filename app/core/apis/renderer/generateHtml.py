from core.config.configReader import ConfigReader

class GenerateHtml:

    def getPluginFile(self, fileName):
        """Get the file where the scripts for the current active renderer plugin live."""
        location = ConfigReader().getRendererPluginLocation()
        thefile = location.replace('.', '/') + 'scripts.txt'
        return thefile

    def generatHtml(self):
        """This method generates the index.html page based on the current active renderer plugin."""
        # read html file
        html = '';
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
