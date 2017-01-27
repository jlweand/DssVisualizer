import re


class FixTime:
    
    def removeDashNumber(self, dateTime):
        """
        Removes unusual '-0700' item from end of snoopyData.json 
        date parameter
        
        :param dateTime: string with -0700 at end of date 
        :type dateTime: string
        :returns: string without -07000 at end of date
        """
        
        dateString = re.sub(r'\-\d+$','',dateTime)
        return dateString

#dateString = "2017-01-25T18:49:12-0700"
#print(FixTime().removeDashNumber(dateString))
