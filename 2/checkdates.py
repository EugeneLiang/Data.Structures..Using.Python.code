# Extracts a collection of birth dates from the user and determines
# if each individual is at least 21 years of age.
from date import Date

def main():
# Date before which a person must have been born to be 21 or older.
    bornBefore = Date(6, 1, 1988)

# Extract birth dates from the user and determine if 21 or older.
    date = promptAndExtractDate()

    printCalendar(date)

def printCalendar(date):
    title1 = date.monthName() + ' ' + str(date.year()) 
    title2 = "Su Mo Tu We Th Fr Sa" 
    print " "*((len(title2) - len(title1))/2) + title1
    print title2



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
