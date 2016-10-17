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
