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

import sys, getopt, argparse
# https://docs.python.org/3/howto/argparse.html
# https://pymotw.com/2/argparse/
class CommandLine:

    def main():

        # look into Nesting Parsers
        parser = argparse.ArgumentParser()
        parser.add_argument("-dir", "--directory", action='store', dest='directory', help="When used with -in, the top level directory to search and import JSON files.  When used with -ex, the destination of exported data.")
        parser.add_argument("-in","--import", action="store_true", dest='import', help="Data will be imported from -d")
        parser.add_argument("-ex","--export", action="store_true", dest='export', help="Data will be exported to -d")
        parser.add_argument('-e', "--eventname", action='store', dest='eventName', help='Name of the event. Used for importing and exporting data.')
        parser.add_argument('-t', "--techname", action='store', dest='techName', help='Name of the technician. Used for importing and exporting data.')
        parser.add_argument('-c', "--comments", action='store', dest='comments', help='Comments about data. Used for importing data.')
        parser.add_argument('-id', "--importdate", action='store', dest='importDate', help='Datetime the data was imported.  If not specified, current datetime will be used.')
        parser.add_argument('-cp', "--copy", action="store_true", dest='copyImages', help='Flag to copy the images on import or export')
        parser.add_argument('-sd', "--startdate", action='store', dest='startDate', help='The datetime to start exporting data.  Only used for exporting data.')
        parser.add_argument('-ed', "--enddate", action='store', dest='endDate', help='The datetime to stop exporting data.  Only used for exporting data.')
        parser.add_argument("-v", "--verbose", action='store_true', dest='verbose', help="Increase output verbosity")

        args = parser.parse_args()
        print(args)

        # inputfile = ''
        # outputfile = ''
        # try:
        #     opts, args = getopt.argparse(argv, "hi:o:", ["ifile=", "ofile="])
        # except getopt.GetoptError:
        #     print('test.py -i <inputdir> -o <outputfile>')
        #     sys.exit(2)
        # for opt, arg in opts:
        #     if opt == '-h':
        #         print('test.py -i <inputdir> -o <outputfile>')
        #         sys.exit()
        #     elif opt in ("-i", "--ifile"):
        #         inputfile = arg
        #     elif opt in ("-o", "--ofile"):
        #         outputfile = arg
        #     elif opt in ("-t", "--ofile"):
        #         outputfile = arg
        #     elif opt in ("-e", "--ofile"):
        #         outputfile = arg
        #     elif opt in ("-c", "--ofile"):
        #         outputfile = arg
        #
        # print('Input file is "', inputfile)
        # print('Output file is "', outputfile)

    if __name__ == "__main__":
        main()
