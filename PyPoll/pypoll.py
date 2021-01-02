import os 
import csv 

total_vote=[]
csvfilepath=os.path.join("..", "..", "PyPoll", "Resources", "election_data.csv" )

with open(csvfilepath, "r") as csvfile: 
    csvreader=csv.reader(csvfile, delimiter=',')
    csvheader=next(csvreader)
    print(csvheader)

    for row in csvreader: 
        total_vote.append(row[2])
print(len(total_vote))
