
# >>>>> DATE TIME <<<<< # :
''' A date in Python is not a data type of its own, but we can 
import a module named datetime to work with dates as date objects. '''

import datetime

x = datetime.datetime.now() # (shows current) 
print(x) # Output: (year-month-day, hour:minute:second.microsecond)  
print("\n")



# >>>>> DATE OUTPUT <<<<< # :
''' 
The date contains year, month, day, hour, minute, second, and microsecond.
The datetime module has many methods to return information about the date object. 
'''

import datetime

x = datetime.datetime
print(x.now())
print(x.year)
print(x.month)
print(x.day)    # "We used the .now() function, so it will show current data."
print("\n")



# >>>>> CREATING DATE OBJECTS <<<<< # :
''' 
To create a date, we can use the datetime() class (constructor) of the datetime module.
The datetime() class requires three parameters to create a date: year, month, day.
'''

import datetime

x = datetime.datetime(2020, 5, 17)
print(x) # Output: year-month-day 00:00:00
print("\n")


''' The datetime() class also takes parameters for time and timezone (hour, minute, second,
microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone). '''

import datetime
from zoneinfo import ZoneInfo  # Only in Python 3.9+

x = datetime.datetime(2025, 5, 20, 12, 24, 48, tzinfo = ZoneInfo("America/New_York"))
print(x) # Output: 2025-05-20 12:24:48-04:00
print("\n")



# >>>>> THE STRFTIME() MATHOD <<<<< # :
'''
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify 
the format of the returned string:
'''

import datetime

x = datetime.datetime.now()
# "We used the .now() function, so it will show current data."

print(x.strftime("%B")) # Output: corrent month
print(x.strftime("%A")) # Output: corrent week 


y = datetime.datetime(2003, 5, 12)
# "We created date object, so it will show created data."

print(y.year) # Output: 2003
print(y.day) # Output: 5
print(y.month) # Output: 12



# >>>>> LEGAL FORMAT CODES <<<<< # :
''' 
[DIRECTIVE]           [DESCRIPTION]                                              [EXAMPLE]

    %a	         Weekday, short version	                                            Wed	
    %A	         Weekday, full version	                                            Wednesday	

    %w	         Weekday as a number 0-6, 0 is Sunday	                            3 (Wednesday)

    %d	         Day of month 01-31	                                                31

    %b	         Month name, short version	                                        Dec	
    %B	         Month name, full version	                                        December

    %m	         Month as a number 01-12	                                        12	

    %y	         Year, short version, without century	                            18	
    %Y	         Year, full version	                                                2018

    %H	         Hour 00-23	                                                        17	
    %I	         Hour 00-12	                                                        05	

    %p	         AM/PM	                                                            PM	

    %M	         Minute 00-59	                                                    41	
    %S	         Second 00-59	                                                    08	
    %f	         Microsecond 000000-999999	                                        548513	

    %z	         UTC offset	                                                        +0100

    %Z	         Timezone	                                                        CST	

    %j	         Day number of year 001-366	                                        365	

    %U	         Week number of year, Sunday as the first day of week, 00-53	    52	
    %W	         Week number of year, Monday as the first day of week, 00-53	    52	

    %c	         Local version of date and time	                                    Mon Dec 31 17:41:00 2018

    %C	         Century	                                                        20	

    %x	         Local version of date	                                            12/31/18	
    %X	         Local version of time	                                            17:41:00

    %%	         A % character	                                                    %	

    %G	         ISO 8601 year	                                                    2018	
    %u	         ISO 8601 weekday (1-7)	                                            1	
    %V	         ISO 8601 weeknumber (01-53)	                                    01
 ''' 