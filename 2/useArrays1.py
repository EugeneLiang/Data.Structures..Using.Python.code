#Count the number of occurrences of each letter in a text file.
from array import Array

# Create an array for the counters and initialize each element to 0.
theCounters = Array( 127 )
theCounters.clear( 0 )

# Open the text file for reading and extract each line from the file
# and iterate over each character in the line.
theFile = open( 'atextfile.txt', 'r' )
for line in theFile :
    for letter in line :
        code = ord( letter )
        theCounters[code] += 1

# Close the file
theFile.close()

# Print the results. The uppercase letters have ASCII values in the
# range 65..90 and the lowercase letters are in the range 97..122.
for i in range( 26 ) :
    print( "%c - %4d %c - %4d" % \
    (chr(65+i), theCounters[65+i], chr(97+i), theCounters[97+i]) )
j = 0
for i in theCounters:
    print "%3d %d" % (j, i)
    j += 1

