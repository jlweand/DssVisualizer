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

import pytz
from tzlocal import get_localzone
from datetime import datetime

class Common:

    def formatDateStringToUTC(self, dateString):
        """Takes a date string in local time and converts it into UTC time.  Used to format dates coming from the UI into UTC dates.

        :param dateString: A date string in local time
        :type dateString: str
        :returns: UTC date (GMT)
        """
        _date = datetime.strptime(dateString, '%Y-%m-%d %H:%M:%S')
        local_tz = get_localzone()
        local_dt = local_tz.localize(_date)
        return local_dt.astimezone(pytz.utc)


    def addUTCToDate(self, dateString):
        """Takes a date string in local time and converts it into UTC time. Used to format dates in the JSON files into UTC dates.

        :param dateString: A date string in UTC time
        :type dateString: str
        :returns: UTC date (GMT)
        """

        _date = datetime.strptime(dateString, '%Y-%m-%dT%H:%M:%S')
        utc = pytz.utc
        local_dt = utc.localize(_date)
        return local_dt.astimezone(pytz.utc)
