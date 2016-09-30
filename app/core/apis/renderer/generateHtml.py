from core.config.configReader import ConfigReader

class GenerateHtml:

    def getPluginFile(self, fileName):
        location = ConfigReader().getRendererPluginLocation()
        thefile = location.replace('.', '/') + fileName
        return thefile

    def generatHtml(self):
        # read html file
        html = '';
        with open('viewmanager/index.html.template', 'r') as htmlFile:
            html = htmlFile.read()

        # get the scripts file
        scriptPlugin = self.getPluginFile('scripts.txt')
        with open(scriptPlugin, 'r') as scriptFile:
            scripts = scriptFile.read()

        # add the scripts to the HTML and dump it back into the file.
        html = html.replace('<SCRIPTS GO HERE>', scripts)
        with open('viewmanager/index.html', 'w') as htmlFile:
            htmlFile.write(html)
            htmlFile.close()
