import json
import csv

genres={}
with open('movies.csv', encoding='utf-8') as file:
    reader=csv.DictReader(file)
    for row in reader:
        column= row['genres']
        column2=column.replace("'", '"')
        genresfixed=json.loads(column2)
        
        for i in range(len(genresfixed)): # for each genre for this movie
            single_genre=genresfixed[i]['name']
            if single_genre in genres:
                genres[single_genre].append(row['original_title'])
            else:
                 genres[single_genre]= [row['original_title']]
            
            
print (len(genres['Comedy']))

'''
genres = {
    'Action': ['James Bond'
}

'''

