
from array import Array2D

# Open the text file for reading.
gradeFile = open( "grade.txt" , "r" )

# Extract the first two values which indicate the size of the array.
numExams = int( gradeFile.readline() )
numStudents = int( gradeFile.readline() )

print numExams
print numStudents

# Create the 2-D array to store the grades.
examGrades = Array2D( numStudents, numExams )

# Extract the grades from the remaining lines.
i = 0
for student in gradeFile :
    grades = student.split()
    print grades
    j = 0
    for j in range(3):
        examGrades[i,j] = int( grades[j] )
    i += 1

for i in range(numStudents) :
    for j in range(numExams) :
        print examGrades[i, j]
# Close the text file.
gradeFile.close()

# Compute each student's average exam grade.
for i in range( numStudents ) :
# Tally the exam grades for the ith stvudent.
    total = 0
    for j in range( numExams ) :
        total += examGrades[i,j]

# Compute average for the ith student.
    examAvg = float(total) / float(numExams)
    print( "%2d: %6.2f" % (i+1, examAvg) )




