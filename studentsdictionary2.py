import json
filename = 'students (1).csv'
students= {}

with open(filename) as file:
    file.readline()
    for line in file:
        split= line.strip().split(',')
        other= {}
        other['LastName']=split [1]
        other['Adjective']=split[0]
        other['Email']=split [3]
        students[split[2]] = other
print(students)
        
with open ('studentdictionary.json', 'w' ) as file:
    json.dump(students, file, indent=4)

#adjective, last_name, first_name, email=line.split(',')
#students[first_name.strip()]=
#other={}
#other['LastName']=last_name
#other[Adjective]=adjective
#other['email']=email