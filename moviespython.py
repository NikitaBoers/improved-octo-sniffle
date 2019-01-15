import json
import csv
#number of fantasy movies

with open('movies.csv', encoding='utf-8') as file:
    reader=csv.DictReader(file)
    fantasy='Fantasy'
    amount=0
    for row in reader:
            if fantasy in row['genres']:
                amount= amount+1
   
print (f'there are {amount} fanatasy movies in this file')


    

