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

import argparse
import os
import subprocess
from sys import platform as _platform
from datetime import datetime
from core.config.dataImport import DataImport
from core.config.dataExport import DataExport


class CommandLine:

    def main():

        # Nesting Parsers
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(help='commands', dest='command')

        # import functionality
        importParser = subparsers.add_parser("import", help="Data will be imported from -d")
        importParser.add_argument("-dir", "--directory", action='store', dest='directory', help="The top level directory to search and import JSON files.")
        importParser.add_argument('-e', "--eventname", default='', action='store', dest='eventname', help='Name of the event to add as metadata to imported data.')
        importParser.add_argument('-t', "--techname", default='', action='store', dest='techname', help='Name of the technician to add as metadata to imported data.')
        importParser.add_argument('-c', "--comments", default='', action='store', dest='comments', help='Comments about data to add as metadata to imported data.')
        importParser.add_argument('-id', "--importdate", action='store', dest='importDate', help='Datetime the data was imported.  If not specified, current datetime will be used.')
        importParser.add_argument('-cp', "--copy", action="store_true", dest='copyimages', help='Flag to copy the images on import. Images will be copied into DssVisualizers file structure')

        # export functionality
        exportParser = subparsers.add_parser("export", help="Data will be exported to -d")
        exportParser.add_argument("-dir", "--directory", action='store', dest='directory', help="The destination for the exported data.")
        exportParser.add_argument('-sd', "--startdate", action='store', dest='startdate', help='The start datetime to search on and return data to export.')
        exportParser.add_argument('-ed', "--enddate", default='', action='store', dest='enddate', help='The end datetime to search on and return data to export.')
        exportParser.add_argument('-e', "--eventname", default='', action='store', dest='eventname', help='Name of the event to search on and return data to export.')
        exportParser.add_argument('-t', "--techname", action='store', dest='techname', help='Name of the technician to search on and return data to export.')
        exportParser.add_argument('-cp', "--copy", action="store_true", dest='copyimages', help='Flag to copy the images on export. Images will be copied to the export directory.')

        # command to start the UI
        startParser = subparsers.add_parser("start", help="Start the DSS Visualizer")

        args = vars(parser.parse_args())
        # print(args)
        if args["command"] == "import":
            try:
                importDate = args["importdate"]
            except KeyError:
                now = datetime.now()
                importDate = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')

            DataImport().importAllDataFromFiles(args["directory"], args["techname"], args["eventname"], args["comments"], importDate, args["copyimages"])

        elif args["command"] == "export":
            DataExport().exportAllData(args["startdate"], args["enddate"], args["techname"], args["eventname"], args["copyimages"], args["directory"])

        elif args["command"] == "start" or args["command"] is None:
            if _platform == "linux" or _platform == "linux2":
                subprocess.call(["mongod --repair"], shell=True)
                subprocess.Popen(["gnome-terminal -e mongod"], shell=True)
                os.system('python3 -m viewmanager.dssvisualizer')
            elif _platform == "win32":
                subprocess.call(["mongod", "--repair"], shell=True)
                subprocess.Popen(["mongod"], shell=True)
                os.system('python -m viewmanager.dssvisualizer')


    if __name__ == "__main__":
        main()

# python dssviz.py import -t "Julie" -e "Julie's event" -dir "C:\temp\json" -c "someComments"
# python dssviz.py export -sd "2016-10-18 00:00:00" -ed "2016-10-18 23:59:59" -t "Julie" -cp -dir "C:\temp\export"
# python dssviz.py start

# python dssviz.py import -t "Juan" -e "Linux Juan Event" -dir "C:\Users\janis\Desktop\json" -c "ugh.. work"
