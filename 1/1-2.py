# Extracts a collection of birth dates from the user and determines
# if each individual is at least 21 years of age.
from date import Date
import calendar

def main():
    date = promptAndExtractDate()

    printCalendar(date)

def printCalendar(date):
    (wday, mdays) = calendar.monthrange(date.year(), date.month())
    title1 = date.monthName() + ' ' + str(date.year()) 
    title2 = "Su Mo Tu We Th Fr Sa" 
    print " "*((len(title2) - len(title1))/2) + title1
    print title2,

    days = range(1, mdays+1)

    # 1/2 letter's diff
    if date.day() > 9:
        days[date.day()-1] = "\x1b[7m%d\x1b[27m" % date.day()
    else:
        days[date.day()-1] = " \x1b[7m%d\x1b[27m" % date.day()
    
    # head " " 
    if wday < 6:
        for i in range(wday+1):
            days.insert(0, " ")

    for i in range(len(days)):
        if (i % 7 == 0):
            print ""
        print "%2s" % days[i],

    print "\n"

# Prompts for and extracts the Gregorian date components. Returns a
# Date object or None when the user has finished entering dates.
def promptAndExtractDate():
    print( "Enter a date." )
    month = int( input("month (0 to quit): ") )
    day = int( input("day: ") )
    year = int( input("year: ") )
    return Date( month, day, year )

# Call the main routine.
main()
