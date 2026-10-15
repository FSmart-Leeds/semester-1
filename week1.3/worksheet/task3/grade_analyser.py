# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file
filename = input("What is the filename of the student file?: ")

# open the file
with open(filename) as f:
    gradebook = f.readlines()
gradebook = gradebook[1:]

# read in the data, and for each student calculate their average grade and classification
newtable = []
for studentfile in gradebook:
    spliced_file = studentfile.split(",")
    sID = spliced_file[0]
    spliced_file = spliced_file[1:]
    modules = []
    for record in spliced_file:
        if record != "" and record != "\n":
            modules.append(int(record))
    avg = sum(modules) / len(modules)
    if avg >= 70:
        grade = "1"
    elif avg >= 60:
        grade = "2:1"
    elif avg >= 50:
        grade = "2:2"
    elif avg >= 40:
        grade = "3"
    else:
        grade = "F"
    avg = f"{avg:.2F}"
    newtable.append(sID+","+avg+","+grade)
print(newtable)

# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'
with open(filename+"_out.csv","w") as f:
    for line in newtable:
        f.write(line+"\n")
# You can compare your output files with the 4 example files in example_outfiles folder