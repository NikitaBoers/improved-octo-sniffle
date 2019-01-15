
filename = 'students (1).csv'
students= []
with open(filename) as file:
    file.readline()
    for line in file:
        split= line.strip().split(',')
        student = {}
        student['Adjective'] = split[0]
        student['LastName'] = split [1]
        student['FirstName'] = split [2]
        student['Email']= split [3]
        students.append(student)
print(students)
        
# import csv
# students= []
# with open...
#reader= csv.Dictreader(file)
#for line in reader:
#students.append(line)