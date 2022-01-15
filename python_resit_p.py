import csv
import numpy as np

#Import csv file
reviews = open('userreviews.csv', newline='', encoding="utf8")
reader = csv.reader(reviews, delimiter=",")
userreviews = list(reader)

#lists
x = []
y = []
z = []


movie = 'the-emoji-movie'

#Create columns

#list x
for row in userreviews:
    x.append(row[0].split(';')[2]) #list X by author

#List compute score

#All the scores movie in one list
for j in userreviews:
    if (j[0].split(';')[0]) == movie:
        z.append(int(j[0].split(';')[1])) #list of scores (int is to make words a number)
#print(m)

#Calculate average score
m = sum(z)/len(z) 
print (m)

#list y
#list of authors that saw my favorite movie
for i in userreviews:
    if (i[0].split(';')[0]) == movie:
        y.append(i[0].split(';')[2]) #list y by author for fav movie

print(y)

#score greator or equal to m
author = str(y)
average = str(m)
moviereviewer = []

for l in userreviews:
    if (l[0].split(';')[1]) >= average:
        if (l[0].split(';')[2]) in author:
            if (l[0].split(';')[0]) != movie: #to remove the emoji movie film in recommendation list
                moviereviewer.append(l[0].split(';')[0])

moviereviewer = list(dict.fromkeys(moviereviewer))
print(moviereviewer)

#save file
np.savetxt("python_resit_output.csv", moviereviewer,fmt='% s')
