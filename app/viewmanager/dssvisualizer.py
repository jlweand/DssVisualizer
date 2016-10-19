import gi
import logging
import os
import ujson
from urllib.parse import parse_qs
# from core.apis.renderer.annotations import Annotations

# Only use files from core.  DO NOT use files from plugins.
from core.apis.renderer.generateHtml import GenerateHtml
from core.apis.datasource.pyKeyLogger import PyKeyLogger
from core.apis.renderer.pluginImporter import PluginImporter
from core.config.configDatasources import ConfigDatasources
from core.config.configRenderers import ConfigRenderers
from core.apis.datasource.multiExcludeThroughput import MultiExcludeThroughput
from core.apis.datasource.multiIncludeThroughput import MultiIncludeThroughput
from core.apis.datasource.tsharkThroughput import TsharkThroughput
from core.apis.datasource.multiExcludeProtocol import MultiExcludeProtocol
from core.apis.datasource.multiIncludeProtocol import MultiIncludeProtocol
from core.apis.datasource.tsharkProtocol import TsharkProtocol

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit", "3.0")
from gi.repository import Gtk
from gi.repository import WebKit



def handle(web_view,web_frame,web_resource,request,response):
	##'query' contains the data sent from the jquery.get method

	query = request.get_message().get_uri().get_query()
	uri = request.get_uri()

	if('installDatasources' in uri or 'adminset' in uri):
		load_uninstalled_plugins(query,"datasource")

	if('installRends' in uri or 'adminset' in uri):
		load_uninstalled_plugins(query,"renderer")

	if not query:
		return
	else:

		queryDict = parse_qs(query)
		if('request' in queryDict):
			if(queryDict['request'][0] == 'keypressData'):
				startDate = queryDict['startDate'][0]
				endDate = queryDict['endDate'][0]
				keyData = PyKeyLogger().selectKeyPressData(startDate, endDate)
				clickData = PyKeyLogger().selectClickData(startDate, endDate)
				timedData = PyKeyLogger().selectTimedData(startDate, endDate)
				js = "visData(%s, %s, %s);" % (keyData, clickData, timedData)
				webKitWebView.execute_script(js)
			elif(queryDict['request'][0] == 'pcapData'):
				startDate = queryDict['startDate'][0]
				endDate = queryDict['endDate'][0]
				multiEx = MultiExcludeThroughput().selectMultiExcludeThroughputData(startDate, endDate)
				multiInc = MultiIncludeThroughput().selectMultiIncludeThroughputData(startDate, endDate)
				tshark = TsharkThroughput().selectTsharkThroughputData(startDate, endDate)
				multiExProt = MultiExcludeProtocol().selectMultiExcludeProtocolData(startDate, endDate)
				multiIncProt = MultiIncludeProtocol().selectMultiIncludeProtocolData(startDate, endDate)
				tsharkProt = TsharkProtocol().selectTsharkProtocolData(startDate, endDate)
				js = "visPCAPData(%s, %s, %s, %s, %s, %s);" % (multiEx, multiExProt, multiInc, multiIncProt, tshark, tsharkProt)
				webKitWebView.execute_script(js)

		elif('submission' in queryDict):
			if(queryDict['submission'][0] == 'annotation'):
				itemID = queryDict['itemID'][0]
				itemType = queryDict['type'][0]
				annotation = queryDict['annotation'][0]
				if(itemType == 'keypress'):
					PyKeyLogger().addAnnotationKeyPress(itemID, annotation)
				elif(itemType == 'click'):
					PyKeyLogger().addAnnotationClick(itemID, annotation)
				elif(itemType == 'timed'):
					PyKeyLogger().addAnnotationTimed(itemID, annotation)
		elif('adminRequest' in queryDict):
			if(queryDict['adminRequest'][0] == 'availablePlugins'):
				load_available_renderers()
		elif('adminSubmission' in queryDict):
			if(queryDict['adminSubmission'][0] == 'pluginChanges'):

				database = queryDict['database'][0]
				pcapDataProtocol= queryDict['pcapDataProtocol'][0]
				pcapThroughput= queryDict['pcapThroughput'][0]
				pyKeyLogger= queryDict['pyKeyLogger'][0]
				screenshots= queryDict['screenshots'][0]
				scriptFile = "scripts.txt"
				ConfigDatasources().setDefaultDatasource(database)
				ConfigRenderers().setDefaultRenderer("pcapDataProtocol",pcapDataProtocol,scriptFile)
				ConfigRenderers().setDefaultRenderer("pcapThroughput",pcapThroughput,scriptFile)
				ConfigRenderers().setDefaultRenderer("pyKeyLogger",pyKeyLogger,scriptFile)
				ConfigRenderers().setDefaultRenderer("screenshots",screenshots,scriptFile)

				print ("updating plugin")
	return

def getJson(file):
	with open(file) as json_data:
		d = ujson.load(json_data)
		return(d)

def load_available_renderers():

	jsonFile=getJson("core/config/config.JSON")
	allFile= ujson.dumps(jsonFile)
	js= "createRadioButtons(%s)" % (allFile)
	webKitWebView.execute_script(js)

def load_uninstalled_plugins(query,type):
	folder = "plugins/renderer/"
	tagID = "installRends"
	if type is "datasource":
		folder = "plugins/datasource/"
		tagID = "installDatasources"

	importer = PluginImporter(folder) #diff
	newPlugins = importer.getUninstalledPlugins()
	if not query:
		for plugin in newPlugins:
			modify_uninstalled_plugin_html(plugin,tagID)
	else:
		importer.importPlugin(query)
		script = 'document.getElementById("'+tagID+'").innerHTML = "";'#diff
		webKitWebView.execute_script(script)
		load_uninstalled_plugins(None,type)

def modify_uninstalled_plugin_html(plugin,tagID):
	if plugin:
		script = 'var element = document.createElement("option");'
		script = script + 'element.innerHTML = "' + plugin + '";'
		script = script + 'document.getElementById("'+tagID+'").appendChild(element);'
	else:
		script = 'document.getElementById("'+tagID+'").innerHTML = "";'
	webKitWebView.execute_script(script)

# def handle_url(request):
# 	print(request.get('annotation'))

gtkWindow = Gtk.Window()
webKitWebView = WebKit.WebView()
gtkScrolledWindow = Gtk.ScrolledWindow()
gtkScrolledWindow.add(webKitWebView)
gtkWindow.add(gtkScrolledWindow)
gtkWindow.connect("delete-event", Gtk.main_quit)

gtkWindow.set_size_request(1000,800)

# generate the index.html page based on the renderer plugin
GenerateHtml().generatHtml()
uri = "file:///" + os.getcwd() + "/viewmanager/index.html"

webKitWebView.load_uri(uri)
webKitWebView.connect("resource-request-starting", handle)


gtkWindow.show_all()
Gtk.main()
