# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]

f = open("student_data.csv")
csv = f.readlines()[1:]
# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3
averages = []
for line in csv:
    columns = line.split(",")
    averages.append(columns[1]+ ": "+ str(round(((int(columns[2])+int(columns[3])+int(columns[4]))/3),2)))
f.close()
# Open a file called 'report.txt'
f = open("report.txt","w")
for average in averages:
    f.write(average+"\n")
f.close()

# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
