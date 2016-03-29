import accessScores
import random

i=0
while i<10:
    accessScores.addScore("Bob",random.randint(0,100)) #add some random scores
    i+=1

print(accessScores.getScores()) #print them all out

accessScores.clearScores() #remove everything

print(accessScores.getScores()) #print now empty database
